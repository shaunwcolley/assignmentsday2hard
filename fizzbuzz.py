num = input("Give me an integer! > ")
num = int(num)

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "Fizz Buzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return "Neither Fizz nor Buzz for you my friend!"

print(fizzbuzz(num))
