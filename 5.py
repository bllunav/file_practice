from pathlib import Path

while True:
    num1 = int(input("enter the first number or 'exit' to exit: "))
    if num1 == "exit":
        print("exited!")
        break
    num2 = int(input("enter the first number or 'exit' to exit: "))
    if num2 == "exit":
        print("exited!")
        break

    try:
        result = num1 / num2
    except ZeroDivisionError:
        pass

    else:
        print(result)