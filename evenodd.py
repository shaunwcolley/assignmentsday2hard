num = input("What number do you want to test for even or odd? > ")
num = int(num)

def check_even_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"

result = check_even_odd(num)

print(f"Your number is {result}!")
