import {readFileSync,existsSync} from 'node:fs';
import assert from 'node:assert/strict';
const base=new URL('../',import.meta.url);const read=name=>JSON.parse(readFileSync(new URL(`src/data/${name}.json`,base)));
const menus=read('menus'),locations=read('locations'),products=read('products');
assert.equal(locations.length,12);
for(const l of locations){const m=menus[l.id];assert(m);assert(l.menuUrl.startsWith('https://gallogiro.com/menu/'));assert.equal(l.orderUrl,l.menuUrl);assert(l.phone&&l.address);assert.equal(m.collectedAt,'2026-10-25');const ids=new Set();for(const p of m.items){assert(!ids.has(p.id));ids.add(p.id);assert.equal(p.restaurantId,l.id);assert(p.source.startsWith('https://gallogiro.com/'));assert(p.price===null||p.price>0,'Never import placeholder $0 prices');assert(p.description.en===''||p.description.es);assert(p.nameEs);}}
assert.equal(menus['santa-ana'].items.length,89);assert.equal(menus.fontana.items.length,79);assert.equal(menus['san-fernando'].status,'unavailable');assert.equal(menus['san-fernando'].items.length,0,'No fallback prices from another restaurant');
for(const p of products){assert.equal(p.restaurantId,'santa-ana');if(p.image)assert(existsSync(new URL('public'+p.image,base)));for(const g of p.groups){assert(g.nameEs);assert(g.options.every(o=>o.nameEs&&(o.price===null||o.price>=0)))}}
console.log('PASS: provenance, per-location menus, translations, positive prices, missing-data behavior and image files');
