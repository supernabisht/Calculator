import art
print(art.logo)
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multi(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
operation={ "+": add,
            "-": sub,
            "*" : multi,
            "/": div}
def calculator():
    a = int(input("What's the first number? "))
    should_accumulate = True
    while should_accumulate:


        for key in operation:
            print(key)
        op_to_perform = input("Type the operation you want to perform: ")
        b = int(input("What's the second number? "))

        ans = (operation[op_to_perform](a, b))
        print(f"{a}{op_to_perform}{b}= {ans}")


        choice = input("Type 'y' to continue the operation or 'n' to restart a operation: ").lower()

        if choice == "y":
            a = ans
            should_accumulate=True
        else:
            should_accumulate = False
            print("\n" * 100)
            calculator()


calculator()





