import csv # Импортируем файлы
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    with open(INPUT_FILENAME) as f: # Открываем файл "input.csv" и связываем его с f
        a = [line for line in csv.DictReader(f)] # Читаем содержимое файла f и сохраняем его в переменную a
    with open(OUTPUT_FILENAME, "w") as f: # Открываем файл "output.json" и связываем его с f
        json.dump(a, f, indent=4) # Записываем список словарей а в файл f и в формате JSON с отступами равными 4

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")