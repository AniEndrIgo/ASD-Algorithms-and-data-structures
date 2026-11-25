x = int(input("Введите число x: "))

if x < 1:
    print("Ошибка: число должно быть больше нуля.")
else:
    result = []
    
    for i in range(1, x + 1):
        num = i
        while num % 3 == 0:
            num //= 3
        while num % 5 == 0:
            num //= 5
        while num % 7 == 0:
            num //= 7

        if num == 1:
            result.append(i)
            
    print(f"Числа от 1 до {x}, делящиеся на 3,5,7:")
    print(result)