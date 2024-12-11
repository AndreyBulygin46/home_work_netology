def dictionary_coobook(name_file: str) -> dict:
    '''Функция для составления словаря'''
    with open(name_file, 'r', encoding='utf-8') as f:
        data = f.read().splitlines()

    index_data_empty = [0]                                                          # Список с нуля, чтобы добавить туда индесы ''
    index_data_empty += [index+1 for index ,word in enumerate(data) if word == '']  # Список индексов пустых строк

    dict_cook_book = {}         # Словарь кулинарной книги
    for i in index_data_empty:  # Перебираем полученный список индексов пустых строк
        dict_cook_book[data[i]] = [{'ingredient_name': data[i+v+2].split(' | ')[0],
                                    'quantity':  int(data[i+v+2].split(' | ')[1]),
                                    'measure':  data[i+v+2].split(' | ')[2]}
                                    for v in range(int(data[i+1]))]

    return dict_cook_book


def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
    '''Расчет ингридиентов для персон'''
    cook_book = dictionary_coobook('ingreingredients.txt')          # Получаем словарь кулинарной книги
    result = {}
    quantity = 0
    for key in dishes:
        lening_key = len(cook_book[key])                            # Считаем количество словарей в списке cook_book по ключу key
        for i in range(lening_key):
            ingredient_name = cook_book[key][i]['ingredient_name']  # Определяем ключ для словаря
            measure = cook_book[key][i]['measure']                  # Единицы измерения для словаря
            quantity = cook_book[key][i]['quantity']                # Количество для словаря
            if ingredient_name in result:                           # Если ключ уже есть в словаре result, то увеличиваем его на новое знач.
                quantity += cook_book[key][i]['quantity']
            result[ingredient_name] = {'measure': measure, 'quantity': quantity*person_count}

    return result

print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))
