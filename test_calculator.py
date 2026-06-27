# Импортируем нашу функцию из файла calculator.py
from calculator import add

def test_add():
    print("Запуск теста функции add...")
    # Ожидаем, что 2 + 3 = 5
    assert add(2, 3) == 5, f"Ошибка! Ожидали 5, но получили {add(2, 3)}"
    print("Тест успешно пройден!")

# Запускаем тест при вызове этого файла
if __name__ == "__main__":
    test_add()
