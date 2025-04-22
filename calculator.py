def calc(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b

a = float(input("Первое число: "))
op = input("Оператор (+-*/): ")
b = float(input("Второе число: "))
print("Результат:", calc(a, b, op))