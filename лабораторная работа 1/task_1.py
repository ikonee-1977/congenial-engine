numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
none_left = numbers[0:4]
none_right = numbers[5:]
middle = (sum(none_right) + sum(none_left)) / len(numbers)
numbers[4] = middle
print("Измененный список:", numbers)
