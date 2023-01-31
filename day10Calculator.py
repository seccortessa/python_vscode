# Calculator


def add(a,b):
    return a + b

def substract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for key in operations:
    print(key)
    
    
operations_symbol = input("Pick an operation from the line above: ")

continueAsk = True

if operations_symbol in operations:
    last_answer = operations[operations_symbol](num1, num2)
    
print(f"{num1} {operations_symbol} {num2} = {last_answer}")
while continueAsk:
    
    letter_continue = input("Do you want to continue calculating? type 'y' or 'n': ")

    if letter_continue == 'n':
        break

    operations_symbol = input("Pick another operation: ")
    num_next = int(input("What's the next number?: "))

    if operations_symbol in operations:
        next_answer = operations[operations_symbol](last_answer, num_next)
        
    print(f"{last_answer} {operations_symbol} {num_next} = {next_answer}")
    last_answer = next_answer