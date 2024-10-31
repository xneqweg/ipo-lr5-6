with open('text.txt', 'r') as f_in, open('output.txt', 'w') as f_out: # Открываем файлы "text.txt" для чтения и "output.txt" для записи
    line_number = 1 # Инициализируем переменную для нумерации строк, начиная с 1
    for line in f_in: # Проходим по каждой строке в файле "text.txt"
        f_out.write(f"{line_number}: {line}") # Записываем в файл "output.txt" строку с номером и содержимым
        line_number += 1 # Увеличиваем счетчик номера строки