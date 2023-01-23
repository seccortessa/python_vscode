

for i in range(1,101):
    letra = ""
    if i % 3 == 0:
        letra += "Fizz"
        if i % 5 == 0:
            letra += "Buzz"
    elif i % 5 == 0:
        letra += "Buzz"
    else:
        letra += str(i)
    print(letra)
        