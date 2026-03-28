def find_common_participants(group_1, group_2, separator=","): #Задаем функцию, принимающую 2 строки и необязательный аргумент
    list1 = group_1.split(separator) # Разделяем строки на списки участников (1 строка)
    list2 = group_2.split(separator) # Разделяем строки на списки участников (2 строка)
    common = set(list1).intersection(set(list2)) # Находим общих участников
    return sorted(list(common)) # Возвращаем полученый результат в виде списка общих участников


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, "|")
print(result)
