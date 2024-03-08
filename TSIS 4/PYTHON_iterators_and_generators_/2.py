def evens():
    n = int(input())
    ev = (int(i) for i in range(0, n + 1, 2))
    for i in range(int(n / 2)):
        print(next(ev), end = ", ")
    print(next(ev))

evens()

"""
Эта функция `evens()` запрашивает у пользователя целое число `n` с помощью `input()`. 
Затем она создает генераторное выражение `ev`, которое генерирует четные числа от 0 до `n-1` включительно, увеличивая шаг на 2.
Далее функция использует цикл `for`, который итерируется `n/2` раз (поскольку мы генерируем только четные числа), 
чтобы печатать четные числа. На каждой итерации из генератора `ev` извлекается следующее значение с помощью функции `next()`, 
и это значение печатается с помощью `print()`. Чтобы все числа выводились в одной строке, мы используем параметр `end=", "`, 
чтобы добавить запятую после каждого числа.
В конце функция вызывает `next(ev)` еще один раз, чтобы вывести последнее четное число и завершить строку печати.
Таким образом, эта функция выводит на экран все четные числа от 0 до `n-1`, разделенные запятыми, и затем выводит последнее четное число.
"""