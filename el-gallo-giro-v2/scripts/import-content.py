"""Build a dated local snapshot from the public-page captures in research/. No API connection."""
from pathlib import Path
import json,re,urllib.request,concurrent.futures
ROOT=Path(__file__).resolve().parents[1]
DATE='2026-10-25'
raw=json.loads((ROOT/'research/products.json').read_text())
extra=json.loads((ROOT/'research/extra.json').read_text())
for x in extra:
 if x['type']=='retry' and not x.get('result','').startswith('Internal'):raw[str(x['id'])]=x['result']
def lines(s):return [re.sub(r'^L\d+: ?', '',l).strip() for l in s.splitlines() if re.match(r'^L\d+:',l)]
def url(s):
 m=re.search(r'https://gallogiro.com/[^\s)]+',s)
 return m[0].rstrip(':') if m else None
def slug(s):return re.sub('[^a-z0-9]+','-',s.lower()).strip('-')
def dump(name,data): (ROOT/'src/data'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
# Product identity, detail groups and image provenance are tied to Santa Ana.
products={}
images={str(x['id']):re.search(r'https://d1w7312wesee68.cloudfront.net/[^\s)]+',x['result']) for x in extra if x['type']=='image'}
for k,r in raw.items():
 u=url(r)
 name=next((l[3:] for l in lines(r) if l.startswith('## ') and 'Locations' not in l),None)
 if not name and u:name=re.search(r'/item-(.+)_[a-z0-9-]+$',u)[1].replace('-',' ')
 if not name:continue
 groups=[];group=None;pending=None
 for l in lines(r):
  if l.startswith('## El Gallo'):break
  if l.startswith('### '):
   group={'name':l[4:],'required':False,'selection':None,'options':[]};groups.append(group);pending=None
  elif group:
   if l=='Required':group['required']=True
   elif l.startswith('Select '):group['selection']=l
   elif l=='[Input]':pending=True
   elif pending is True and l:
    group['options'].append({'name':l,'price':None});pending=False
   elif l.startswith('+$') and group['options']:group['options'][-1]['price']=float(l[2:])
 image=images.get(k)
 products[k]={'id':slug(name),'name':name,'detailSource':u,'restaurantId':'santa-ana','collectedAt':DATE,'detailStatus':'unavailable' if r.startswith('Internal') else 'captured','groups':groups,'imageSource':image[0].rstrip(':') if image else None,'image':None}
# Parse every location independently: no shared prices or stock assumptions.
menus={};locations=[]
location_names=['Claremont','Anaheim','Bellflower','Canoga Park','East LA','Fontana','Huntington Park','Lynwood','Panorama City','San Fernando','Santa Ana','Van Nuys']
source_menu=(ROOT/'research/santa-ana-menu.txt').read_text()
source_lines=lines(source_menu)
for ix,name in enumerate(location_names):
 id=15+ix*2;r=next(x['result'] for x in extra if x['type']=='menu' and x['id']==id)
 locid=slug(name);mu=url(r)
 if name=='Bellflower':
  fallback=(ROOT/'research/default-menu.txt').read_text()
  if '9009 Alondra Boulevard, Bellflower, CA[Button: Change location]' in fallback:
   r=fallback
 # Footer contains address and phone as displayed, including source ambiguities.
 footer=source_lines[source_lines.index('## El Gallo Giro Locations and Hours'):]
 label='888 S Indian Hill Blvd' if name=='Claremont' else name
 start=next(i for i,l in enumerate(footer) if re.match(r'### 【\d+†'+re.escape(label)+'】',l))
 chunk=footer[start:start+10]
 phone=next(l for l in chunk if re.match(r'\(\d{3}\)',l))
 address=next(re.search(r'【\d+†(.+)†google.com】',l)[1] for l in chunk if '†google.com】' in l)
 locations.append({'id':locid,'name':name,'officialLabel':label,'address':address,'phone':phone,'menuUrl':mu,'orderUrl':mu,'hours':None,'hoursSource':mu,'source':'https://gallogiro.com/','collectedAt':DATE,'notes':('Phone repeats Fontana; verify before production.' if name=='Claremont' else 'Street number not provided by source.' if name=='East LA' else None)})
 items=[];category=None;section=None
 for l in lines(r):
  if l.startswith('## El Gallo'):break
  if l.startswith('## '):section=l[3:];category=section
  if l.startswith('### '):category=l[4:]
  match=re.match(r'\* 【(\d+)†(.+)】',l)
  if not match or section=='Best Sellers' or section=='Menu':continue
  text=match[2];out='OUT OF STOCK' in text;text=text.replace('OUT OF STOCK','')
  price=re.search(r'\$(\d+(?:\.\d+)?)$',text);price=float(price[1]) if price else None
  text=re.sub(r'\$\d+(?:\.\d+)?$','',text)
  split=re.search(r' (?=Our |A |Made |Fresh|Traditional |Feeds |Choose |Four |The original|Pure,|Bright,)',text)
  title=text[:split.start()] if split else text
  desc=text[split.end():] if split else ''
  key=slug(title)
  detail=next((p for p in products.values() if p['id']==key),None)
  items.append({'id':key,'name':title,'description':{'en':desc},'category':category,'section':section,'price':price,'currency':'USD','outOfStockAtCollection':out,'source':('https://gallogiro.com/menu' if name=='Bellflower' else mu),'collectedAt':DATE,'restaurantId':locid,'detailSource':detail['detailSource'] if detail and locid=='santa-ana' else None})
 menus[locid]={'restaurantId':locid,'source':('https://gallogiro.com/menu' if name=='Bellflower' else mu),'collectedAt':DATE,'status':'captured' if items else 'unavailable','items':items}
for p in products.values():
 p['imagePageSource']=p['detailSource'] if p['imageSource'] else None
 p['imageRestaurantId']='santa-ana' if p['imageSource'] else None
for addition in json.loads((ROOT/'research/supplemental-images.json').read_text()):
 p=next(p for p in products.values() if p['id']==addition['id'])
 p.update(addition)
# Download only actual product images. Missing photographs remain absent, never substituted with another dish.
assets=ROOT/'public/assets/menu';assets.mkdir(exist_ok=True)
def download(p):
 if not p['imageSource']:return
 target=assets/(p['id']+('.webp' if 'ext%3Awebp' in p['imageSource'] else '.jpg'))
 try:
  if not target.exists():urllib.request.urlretrieve(p['imageSource'],target)
  if target.stat().st_size<100:raise ValueError('empty image')
  p['image']='/assets/menu/'+target.name
 except Exception as e:p['imageError']=str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:list(pool.map(download,products.values()))
dump('products.json',list(products.values()));dump('locations.json',locations);dump('menus.json',menus)
print('Menus:',{k:len(v['items']) for k,v in menus.items()});print('Images:',sum(bool(p['image']) for p in products.values()));print('Groups:',sum(len(p['groups']) for p in products.values()))
