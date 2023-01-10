first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))
operator = input("Enter operator(+,-,*,/): ")

if operator == '+':
    res = first_num + second_num
elif operator == '-':
    res = first_num - second_num
elif operator == '*':
    res = first_num * second_num
elif operator == '/':
    res = first_num / second_num
else:
    res = "Invalid operator"

print("The result is : ", res)
