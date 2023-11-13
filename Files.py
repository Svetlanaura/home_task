import os

path = os.path.join(os.getcwd(), 'Text.txt')
with open(path) as Text_file:
    cook_book = {}
    for string in Text_file:
        dish = string.strip()
        ingredients_count = int(Text_file.readline().strip())
        dish_dict = []
        for item in range(ingredients_count):
            ingredients_name, quantity, measure = Text_file.readline().strip().split('|')
            dish_dict.append({'ingredient_name': ingredients_name,
                              'quantity': quantity,
                              'measure': measure})
        cook_book[dish] = dish_dict
        Text_file.readline()


#  Задача №2
def shop_list(dishes, person_count):
    shop_dict = {}
    for _dish in dishes:
        for ingredient in cook_book[_dish]:
            ingredients_list = dict([(ingredient['ingredient_name'],
                                      {'quantity': int(ingredient['quantity']) * person_count,
                                       'measure': ingredient['measure']})])
            if shop_dict.get(ingredient['ingredient_name']) == 'None':
                union = (int(shop_dict[ingredient['ingredient_name']]['quantity']) +
                         int(ingredients_list[ingredient['ingredient_name']]['quantity']))
                shop_dict[ingredient['ingredient_name']]['quantity'] = union
            else:
                shop_dict.update(ingredients_list)
    return shop_dict


print(shop_list(['Запеченный картофель', 'Омлет', 'Фахитос', 'Омлет', 'Запеченный картофель'], 5))
