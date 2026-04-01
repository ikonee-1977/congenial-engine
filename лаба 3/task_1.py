def function(items_list, item): #Функция первого вхождения
    first_index = None # изначально не найдено
    for i in range(len(items_list)): #цикл по всем товарам
        if items_list[i] == item:
            first_index = i
            return first_index
    return first_index #возврат
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
for find_item in ['банан', 'груша', 'персик']:
    index_item = function(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")