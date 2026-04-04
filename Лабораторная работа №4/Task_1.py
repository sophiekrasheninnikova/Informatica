import json
def task() -> float:
    a = "input.json"
    with open(a) as f: # Прочитали файл JSON
        json_data = json.load(f) # Считываеv данные из файла f в формате JSON и сохраняем их в переменную json_data
    summa = sum([item["score"] * item["weight"] for item in json_data]) # Вычислили сумму произведений "score" * "weight" в каждом словаре
    return round(summa, 3) # вернули значение с плавающей запятой, округленное до 3 знаков после запятой


print(task())