num1 = input("First number: ")
ope = input("Operation: ")
num2 = input("Second number: ")

num1 = float(num1)
num2 = float(num2)

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def calc(n1, n2):
    if ope == "+":
        return add(n1, n2)
    elif ope == "-":
        return sub(n1, n2)
    elif ope == "*":
        return mult(n1, n2)
    elif ope == "/":
        return div(n1, n2)

answer = calc(num1, num2)

print(answer)
