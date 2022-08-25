from logger import logger


def file_open_dict():
    cook = list()
    cook_book = dict()
    file = "recipes.txt"

    with open(file, 'rt', encoding='utf-8') as fg:
        for line in fg:
            line = line.strip()
            cook.append(line)

    for x in range(len(cook)):
        if cook[x].isdigit():
            items = list()
            key = cook[x - 1]
            for y in range(1, int(cook[x]) + 1):
                ingredients_n = dict()
                ingredient = cook[x + y].split('|')
                ingredients_n['ingredient_name'] = ingredient[0]
                ingredients_n['quantity'] = int(ingredient[1])
                ingredients_n['measure'] = ingredient[2]
                items.append(ingredients_n)
            cook_book[key] = items
    return cook_book


logger_path = logger(path=f'Task1/')


@logger_path
@logger(path=None)
def get_shop_list_by_dishes(dishes, person_count):
    cook_book = file_open_dict()
    title_list = dict()
    for dish in dishes:
        for ingredients_n in cook_book[dish]:
            if ingredients_n['ingredient_name'] not in title_list:
                title_list[ingredients_n['ingredient_name']] = {
                    'measure': ingredients_n['measure'],
                    'quantity': ingredients_n['quantity'] * person_count
                }
            else:
                title_list[ingredients_n['ingredient_name']]['quantity'] = (
                        title_list[ingredients_n['ingredient_name']]['quantity']
                        + (ingredients_n['quantity'] * person_count))
    return title_list
