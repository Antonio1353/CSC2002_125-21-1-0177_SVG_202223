#DAY 10.py
# CALCULATOR
def add( n1, n2) :
    return n1+n2

def subtract(n1, n2):
    return n1 +(n2*-1)

def multiply (n1, n2) :
    return n1*n2

def divide(n1, n2):
    return n1/n2

operations ={"+":add,
 "-":subtract,
 "*":multiply,
 "/":divide}


def calc ():
        going = True

        while going:
            num1 =float(input("What is the first number"))

            for ke in operations :
                print(f"{ke}")

            operation_symbol = input("Pick an operation:")
            num2 =float(input("What is the next number"))
            drey = operations[operation_symbol]

            first_answer = drey(num1, num2)

            print(f"{num1}  {operation_symbol} {num2}  = {first_answer}")

            Decision= input(f"Type 'y' to continue calulating with {first_answer}, or type 'n' to exit").lower
            # operation_symbol = input("Pick another operation")
            # num3 = int(input("What's the next number"))
            # drey = operations[operation_symbol]
            # second_answer = drey(first_answer, num3)
            # print(f"{first_answer}  {operation_symbol} {num3}  = {second_answer}")

            if Decision != "y" :
                going = False

