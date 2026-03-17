numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
numbers[4]=0
# TODO заменить значение пропущенного элемента средним арифметическим
summ=sum(numbers)
count=len(numbers)
cr_arifm=summ/count
numbers[4]=cr_arifm
print("Измененный список:", numbers)
