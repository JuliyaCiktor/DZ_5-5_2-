while True:
    num1 = float(input("Введіть перше число: "))
    operator = input("Введіть оператор (+, -, *, /): ")
    num2 = float(input("Введіть друге число: "))
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Помилка! Ділення на нуль."
    else:
        result = "Невірний оператор!"
    print("Результат:", result)
    continue_calc = input("Хочете продовжити? (yes/y щоб продовжити): ").lower()
    if continue_calc != "yes" and continue_calc != "y":
        print("Робота калькулятора завершена.")
        break
