#список известных имен файлов
file_names = ['file1.txt', 'file2.txt', 'file3.txt']

# список для хранения информации о файлах
files_info = []

# проходим по каждому известному имени файла
for file_name in file_names:
    # открываем файл для чтения
    with open(file_name, 'r') as file:
        # считываем содержимое файла и определяем количество строк
        content = file.read()
        num_lines = len(content.split('\n'))

        # создаем элемент списка с информацией о файле и добавляем его в список
        file_info = (file_name, num_lines, content)
        files_info.append(file_info)

# сортируем список по количеству строк в каждом файле
files_info.sort(key=lambda x: x[1])

# создаем новый файл для записи результата
with open('result.txt', 'w') as result_file:
    # проходим по каждому элементу списка
    for file_info in files_info:
        # записываем служебную информацию о файле (имя файла и количество строк)
        result_file.write(f'File Name: {file_info[0]}\n')
        result_file.write(f'Number of Lines: {file_info[1]}\n')

        # записываем содержимое файла
        result_file.write(file_info[2])
        result_file.write('\n')