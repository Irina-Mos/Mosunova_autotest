try:
    a = 10 / 0
except ZeroDivisionError as e:
    print(f"На ноль делить нельзя. Ошибка: {e} ")
else:
    print("Деление прошло успешно.")
finally:
    print("Тут мы пытались поделить")