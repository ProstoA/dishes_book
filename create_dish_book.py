import pprint
cook_book = {}
with open('dishes_book.txt', encoding='utf-8', newline='\r\n') as f:
    dish_name = ''
    dish_ingredients = []
    for line in f:
        line = line.strip('\r\n')
        if line == '':
            cook_book[dish_name] = dish_ingredients
            dish_name = ''
            dish_ingredients = []
        elif dish_name == '':
            dish_name = line.lower()
        elif '|' in line:
            m = line.split("|")
            dish_ingredients.append({'ingridient_name': m[0], 'quantity': int(m[1]), 'measure': m[2]})
    cook_book[dish_name] = dish_ingredients
    #pprint.pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] +=\
          new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                            shop_list_item['measure']))

def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .lower().split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count)
  print_shop_list(shop_list)

create_shop_list()