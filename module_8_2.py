"""
Функция personal_sum(numbers):
Должна принимать коллекцию numbers.
Подсчитывать сумму чисел в numbers путём перебора и увеличивать переменную result.
Если же при переборе встречается данное типа отличного от числового, то обработать исключение TypeError,
увеличив счётчик incorrect_data на 1.
В конечном итоге функция возвращает кортеж из двух значений: result - сумма чисел,
incorrect_data - кол-во некорректных данных.

Функция calculate_average(numbers)
Среднее арифметическое - сумма всех данных делённая на их количество.
Должна принимать коллекцию numbers и возвращать: среднее арифметическое всех чисел.
Внутри для подсчёта суммы используйте функцию personal_sum написанную ранее.
Т.к. коллекция numbers может оказаться пустой, то обработайте исключение ZeroDivisionError при делении на 0 и верните 0.
Также в numbers может быть записана не коллекция, а другие типы данных, например числа.
Обработайте исключение TypeError выводя строку 'В numbers записан некорректный тип данных'.
В таком случае функция просто вернёт None.
"""

# Создадим функцию "personal_sum", которая принимает не ограниченное количество параметров "*numbers"
def personal_sum(*numbers):
    # Создадим переменную "result", куда будем записывать результат подсчета суммы чисел в параметре "numbers".
    # Изначально равно 0.
    result = 0
    # Создадим переменную "incorrect_data", куда будем записывать результат перебора циклом "for" если в параметре
    # "numbers" тип данных отличается от числового. Изначально равно 0.
    incorrect_data = 0
    # запустим цикл "for", перебирающий переменную "i" в параметре "numbers" и пройдемся во вложенном цикле "for"
    # переменной "j" в переменной "i".
    for i in numbers:
        for j in i:
            # После цикла "for" запустим блок "try", который будет добавлять в переменную "result" результат перебора
            # переменной "j", если же цикл "for" не выполняется (в переменной "i" тип данных отличается от числового)
            # добавляем в переменную "incorrect_data" значение и выводим соответсвующую запись (print).
            try:
                result+=j
            except TypeError:
                incorrect_data+=1
                print(f'Некорректный тип данных для подсчета суммы - {j}')
    # в конце функции возвращаем(return) кортеж из двух значений: "result" - сумма чисел,
    # "incorrect_data" - кол-во некорректных данных.
    return [result, incorrect_data]

# Создадим функцию "calculate_average", которая принимает не ограниченное количество параметров "*numbers"
def calculate_average(*numbers):
    # с помощью метода "isinstance" проверяем передаваемые значения в параметр "numbers" принадлежность
    # числовому типу(int), и выводим сообщение(print), функция возвращает "None"
    if isinstance(*numbers, int):
        print('В numbers записан некорректный тип данных')
        return None
    # запустим блок "try", в котором передадим в переменную "num" результат работы функции "personal_sum",
    # и будем возвращать среднее арифметическое значение всех чисел.
    try:
        num = personal_sum(*numbers)
        return num[0]/(len(*numbers) - num[1])
    # обработаем блоком "except" исключение, если коллекция "numbers" окажется пустой, и вернем 0.
    except ZeroDivisionError:
        return 0


# Пример выполнения программы:
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать