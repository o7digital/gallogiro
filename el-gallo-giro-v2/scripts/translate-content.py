"""Editorial Spanish translations; English names and source text remain preserved."""
import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'src/data'
m=json.loads((D/'menus.json').read_text())
es={
'4 Torta Box':'Elige cuatro tortas, cada una preparada al momento en telera tostada con ingredientes auténticos y verduras frescas, para compartir una comida variada.',
'Cubana Torta':'Nuestra torta de la casa y la más vendida, preparada al momento en telera tostada con lomo de cerdo marinado, milanesa de res, jamón, queso de puerco, queso panela, frijoles refritos, aguacate, lechuga, tomate, jalapeños, cebolla marinada y mayonesa.',
'4 Tacos Combo':'Cuatro tacos con la proteína que elijas, acompañados de arroz mexicano, frijoles refritos, cebolla, cilantro y salsa.',
'4 Burrito Box':'Elige cuatro burritos, cada uno preparado al momento con arroz, frijoles, cilantro y cebolla, envueltos en tortilla de harina caliente, para compartir.',
'Bean & Cheese Burrito':'Un clásico vegetariano con frijoles refritos cremosos y queso derretido, envuelto en una tortilla de harina caliente.',
'Huevo Con Jamon Platillo':'Huevos revueltos recién hechos con jamón, acompañados de arroz, frijoles, salsa y tortillas calientes.',
'Ham & Egg Burrito':'Tortilla de harina caliente rellena de huevos, frijoles, arroz y jamón para un desayuno sencillo y satisfactorio.',
'Ham & Egg Torta':'Preparada al momento con huevos, jamón, queso panela y aguacate en telera tostada.',
'Super Gallo Breakfast Torta':'Nuestra torta de desayuno con huevos, jamón, salchicha, queso Monterey Jack, aguacate y salsa de chipotle.',
'Burrito Bowl':'Preparado al momento con la proteína que elijas, arroz, frijoles, lechuga, tomate, queso panela y aguacate, para un bowl abundante de sabor auténtico.',
'Green Salad':'Lechuga crujiente, tomates maduros, queso panela y aguacate cremoso para una ensalada fresca y sabrosa.',
'Mosaico Vaso':'Un postre de gelatina al estilo mexicano, ligero y refrescante.',
'Arroz Con Leche Vaso':'Arroz con leche tradicional preparado con leche y canela para un sabor cremoso y reconfortante.',
'Flan Vaso':'Flan de vainilla de textura sedosa cubierto de caramelo.',
'Agua Horchata':'Agua fresca cremosa y refrescante, preparada diariamente con arroz, canela, leche, agua y azúcar para un sabor tradicional auténtico. Disponible en tamaños de 20, 32 y 44 oz.',
'Agua Mamey':'Agua fresca tropical de textura suave, preparada con mamey maduro, agua y azúcar para un sabor dulce y refrescante. En tamaños de 20, 32 y 44 oz.',
'Agua Jamaica Con Splenda':'Agua fresca agridulce preparada con flores de jamaica en infusión, agua y Splenda, para un sabor mexicano refrescante. En tamaños de 20, 32 y 44 oz.',
'Agua Chia Con Limon':'Mezcla refrescante de jugo de limón, semillas de chía, agua y azúcar que combina sabor cítrico y textura. Disponible en tamaños de 20, 32 y 44 oz.',
'Agua Pepino Con Pina':'Mezcla fresca y refrescante de pepino y piña dulce, preparada para equilibrar sus sabores frutales. Una bebida para acompañar cualquier comida.',
'Agua Mango Dragon Fruit':'Agua fresca tropical de mango, pitahaya, agua y azúcar, de sabor dulce y frutal y color intenso. Disponible en tamaños de 20, 32 y 44 oz.',
'Coke':'El refresco original de sabor dulce y burbujas, servido frío en tamaños de 20, 32 y 44 oz.',
'Diet Coke':'Refresco sin calorías, de sabor intenso y burbujas refrescantes. Disponible en tamaños de 20, 32 y 44 oz.',
'Sprite':'Refresco de lima-limón sin cafeína, de sabor limpio y burbujeante. Disponible en tamaños de 20, 32 y 44 oz.',
'Fanta':'Fanta Naranja, un clásico de color intenso, burbujas y sabor a naranja, servido frío para acompañar la comida.',
'Cafe de Olla':'Café mexicano tradicional preparado con canela y piloncillo para un sabor aromático e intenso. Disponible en tamaños de 12, 20 y 96 oz.',
'Champurrado':'Bebida mexicana de chocolate, caliente y espesa, preparada con masa de maíz, leche, chocolate y canela. Disponible en tamaños de 12, 20 y 96 oz.',
'Bottled Water':'Agua embotellada pura y refrescante, una opción sencilla para acompañar cualquier comida.',
'Bolillo':'Panecillos mexicanos tradicionales horneados durante el día, de interior ligero y corteza dorada.',
'Bigote Danes':'Pan dulce mexicano clásico, untado con mantequilla derretida y cubierto de azúcar.',
'Cuerno Danes':'Pan dulce al estilo mexicano, parecido a un croissant.',
'Feite Guayaba':'Pan suave relleno de pasta dulce de guayaba, horneado diariamente.',
'Elote Fino':'Pan dulce tradicional de textura suave, similar a un pastel, y dulzura delicada.',
'Puerquitos':'Galletas tradicionales con forma de puerquito, sabor a canela y piloncillo.',
'Pan De Muerto Pequeno':'Pan de muerto tradicional recién horneado, de interior suave y esponjoso y sabor a mantequilla.'}
proteins={'Asada':'carne asada a la parrilla','Milanesa':'milanesa de res crujiente','Carnitas':'carnitas cocinadas a fuego lento','Jamon & Queso Panela':'jamón a la plancha','Pollo':'pollo a la parrilla','Pierna Adobada':'pierna de cerdo marinada en adobo','Pastor':'carne de cerdo marinada al pastor','Chorizo':'chorizo mexicano','Fritanga':'una mezcla sazonada de cortes de cerdo','Trompa':'trompa de cerdo sazonada','Buche':'buche de cerdo cocinado a fuego lento','Bean & Cheese':'frijoles refritos cremosos y queso derretido'}
for protein,desc in proteins.items():
 if protein not in ['Chorizo','Fritanga','Trompa','Buche','Bean & Cheese']:
  es[protein+' Torta']='Preparada al momento en telera tostada con '+desc+', queso panela, frijoles refritos, aguacate, lechuga, tomate, jalapeños, cebolla marinada y mayonesa.'
 for size in ['Grande','Regular']:
  es[protein+' Taco '+size]='Taco preparado al momento en tortilla de maíz caliente con '+desc+(' para un sabor vegetariano reconfortante.' if protein=='Bean & Cheese' else ', cilantro y cebolla para un sabor mexicano tradicional.')
 if protein not in ['Milanesa','Jamon & Queso Panela','Pierna Adobada','Bean & Cheese']:
  es[protein+' Burrito']='Preparado al momento con '+desc+', arroz, frijoles, cilantro y cebolla, envueltos en una tortilla de harina caliente.'
for lbs,people in [(1,'2–3'),(2,'5–6'),(3,'7–9'),(5,'12–15')]:
 es[f'{lbs}Lb Family Pack']=f'Para {people} personas, con la proteína que elijas, arroz, frijoles, totopos, salsa, '+('cebolla con cilantro, ' if lbs==2 else '')+'tortillas y chiles asados.'
for name in ['Concha Blanca','Concha Chocolate']:
 es[name]='Pan dulce recién horneado, de centro suave y cubierta crujiente. Nuestras conchas se hornean durante el día y están disponibles hasta agotar existencias. Si el sabor elegido se agota al final del día, lo sustituiremos por otro disponible.'
for menu in m.values():
 for p in menu['items']:
  p['description']['es']=es.get(p['name'],'')
  if p['description']['en'] and not p['description']['es']:raise ValueError('Missing translation: '+p['name'])
  p['translation']='editorial-es-from-official-en'
(D/'menus.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
products=json.loads((D/'products.json').read_text())
terms={'Avocado (Fresh Sliced) 3 Slices':'Aguacate fresco, 3 rebanadas','Avocado (Fresh Sliced)':'Aguacate fresco en rebanadas','Avocado (Fresh Slices)':'Aguacate fresco en rebanadas','Frijoles (Refried Beans)':'Frijoles refritos','Queso de Puerco (Head Cheese)':'Queso de puerco','Onions (Spicy, Marinated)':'Cebolla picante marinada','Queso Panela Slice (Cheese)':'Rebanada de queso panela','Queso Panela Slice':'Rebanada de queso panela','No Cheese on Beans':'Sin queso en los frijoles','No Cheese on Frijoles refritos':'Sin queso en los frijoles refritos','4 Corn Tortillas':'4 tortillas de maíz','Flour Tortilla':'Tortilla de harina','Telera (Homemade)':'Telera hecha en casa','Avocado Dressing':'Aderezo de aguacate','Panela Cheese':'Queso panela','Cheese Panela':'Queso panela','Sour Cream':'Crema agria','No Drink':'Sin bebida','No Side':'Sin guarnición','Sub Bottle Water':'Sustituir por agua embotellada','Sub Chips':'Sustituir por totopos','Over Easy':'Estrellados, yema líquida','Over Medium':'Estrellados, yema semilíquida','Over Hard':'Estrellados, yema cocida','Scrambled':'Revueltos','Small ':'Chico ','Medium ':'Mediano ','Large ':'Grande ','Gallon ':'Galón ','Add ':'Agregar ','Extra ':'Extra ','Avocado':'Aguacate','Lettuce':'Lechuga','Onions':'Cebolla','Limes':'Limones','Mayo':'Mayonesa','Tomato':'Tomate','Rice':'Arroz','Egg':'Huevo','Ham':'Jamón','Cheese':'Queso','Chips':'Totopos','Chip':'Totopo',' and ':' y '}
for p in products:
 for g in p['groups']:
  g['nameEs']=('Tamaño' if 'Size' in g['name'] else 'Proteína a elegir' if any(s in g['name'] for s in ['Protein','Meat']) else 'Guarniciones' if 'Sides' in g['name'] else 'Ingredientes y opciones')
  for o in g['options']:
   label=o['name']
   for a,b in terms.items():label=label.replace(a,b)
   o['nameEs']=label
(D/'products.json').write_text(json.dumps(products,ensure_ascii=False,indent=2)+'\n')
# Localized display names; retain name as the exact official product identifier.
name_terms={'Double ':'Doble ','Jamon & Queso Panela':'Jamón y queso panela','Bean & Cheese':'Frijoles y queso','Ham & Egg':'Jamón y huevo','Super Gallo Breakfast Torta':'Torta de desayuno Super Gallo','Green Salad':'Ensalada verde','Bottled Water':'Agua embotellada','4 Torta Box':'Caja de 4 tortas','4 Burrito Box':'Caja de 4 burritos','4 Tacos Combo':'Combo de 4 tacos','Family Pack':'Paquete familiar','Pan De Muerto Pequeno':'Pan de muerto pequeño','Huevo Con Jamon Platillo':'Platillo de huevo con jamón','Agua Horchata':'Agua de horchata','Agua Mamey':'Agua de mamey','Agua Jamaica Con Splenda':'Agua de jamaica con Splenda','Agua Chia Con Limon':'Agua de chía con limón','Agua Pepino Con Pina':'Agua de pepino con piña','Agua Mango Dragon Fruit':'Agua de mango y pitahaya','Concha Chocolate':'Concha de chocolate','Concha Blanca':'Concha blanca','Cafe de Olla':'Café de olla','Mosaico Vaso':'Vaso de mosaico','Arroz Con Leche Vaso':'Vaso de arroz con leche','Flan Vaso':'Vaso de flan','Feite Guayaba':'Feite de guayaba','Bigote Danes':'Bigote danés','Cuerno Danes':'Cuerno danés','Elote Fino':'Elote fino'}
for menu in m.values():
 for p in menu['items']:
  n=p['name']
  for a,b in name_terms.items():n=n.replace(a,b)
  if n.endswith(' Torta'):n='Torta de '+n[:-6].lower()
  if ' Taco ' in n:
   protein,size=n.split(' Taco ');n='Taco '+size.lower()+' de '+protein.lower()
  if n.endswith(' Burrito'):n='Burrito de '+n[:-8].lower()
  p['nameEs']=n
(D/'menus.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
