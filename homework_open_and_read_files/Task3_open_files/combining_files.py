def comb_files(names_files: list):
    '''Функция преобразования трех файлов в один'''
    dict_names_files = {}
    for name_file in names_files:
        # with open(f'homework_open_and_read_files/Task3_open_files/{name_file}', 'r', encoding='utf-8') as file:
        with open(name_file, 'r', encoding='utf-8') as file:
            # Читаем файл, записываем в словарь
            # по ключу name_file как отдельный список
            dict_names_files[name_file] = [file.readlines()]
            # Длина dict_names_files[name_file] равная количеству строк
            legth = len(dict_names_files[name_file][0])
            # Добавление длины в тот же словарь к ключу name_file
            dict_names_files[name_file] += [{'leght': legth}]

    sort_dict_name_file = dict(sorted(dict_names_files.items(),
                               # Отсортировать dict_names_files по leght
                                      key=lambda x: x[1][1]['leght']))

    for k, v in sort_dict_name_file.items():
        line = ''.join(v[0])
        with open('homework_open_and_read_files/Task3_open_files/result.txt',
                  'a', encoding='utf-8') as file:
            # Запись файла в файл result
            file.write(f'{k[-5:]}\n{v[1]['leght']}\n{line}\n')


comb_files(['homework_open_and_read_files/Task3_open_files/1.txt',
            'homework_open_and_read_files/Task3_open_files/2.txt',
            'homework_open_and_read_files/Task3_open_files/3.txt'])
