def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def Simplecalculator():
    print("Welcome to the Simple Calculator!")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("\nChoose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        print(f"{num1} + {num2} = {addition(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtraction(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiplication(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {division(num1, num2)}")
    else:
        print("PLEASE ENTER VALID INPUT.")

if __name__ == "__main__":
    Simplecalculator()
