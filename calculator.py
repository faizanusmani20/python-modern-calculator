

def calculate(num1,op,num2):
    match op:
        case '+':
            return num1+num2
        case '-':
            return num1-num2
        case '*':
            return num1*num2
        case '/':
            if num2==0:
                return "Cannot divide by 0"
            else:
                return num1/num2
        case '**':
            return num1**num2
        case _:
            return "Invalid Operator"


print("\n"+"="*30)
print("      Modern Calculator 🖩     ")
print("="*30)

while True:
    try:
        num1=float(input("Enter a number: "))
        op=input("Operator '+' '-' '*' '/' '**' ")
        num2=float(input("Enter a number: "))

        result= calculate(num1,op,num2)

        print(f"Result = {result}")

        again=input("Calculate Again (Yes/No)").strip().lower()
        if again!="yes":
            print("GoodBye ♥")
            break

    except ValueError:
        print("Invalid Number !")
