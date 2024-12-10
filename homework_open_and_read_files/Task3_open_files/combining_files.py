def comb_files(names_files: list):
    '''Функция преобразования трех файлов в один'''
    dict_names_files ={}
    for name_file in names_files:
        with open(name_file, 'r', encoding='utf-8') as file:
            dict_names_files[name_file] = [file.readlines()]   # Читаем файл,записываем в словарь по ключу name_file как отдельный список
            legth = len(dict_names_files[name_file][0])        # Длина dict_names_files[name_file] равная количеству строк
            dict_names_files[name_file] += [{'leght': legth}]  # Добавление длины в тот же словарь к ключу name_file

    sort_dict_name_file = dict(sorted(dict_names_files.items(),
                                      key=lambda x: x[1][1]['leght']))  # Отсортировать dict_names_files по leght

    for k, v in sort_dict_name_file.items():
        line = ''.join(v[0])
        with open('result.txt', 'a', encoding='utf-8') as file:
            file.write(f'{k}\n{v[1]['leght']}\n{line}\n')               # Запись файла в файл result

comb_files(['1.txt', '2.txt', '3.txt'])
