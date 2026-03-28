def a(items_list, target_item): # Задаем переменную а
    if target_item in items_list: # Условие взвращения индекса
        return items_list.index(target_item) # Возвращаем индекс первого вхождения
    else: # Если товар не найден в списке
        return None # Возвращаем None
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = a(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
