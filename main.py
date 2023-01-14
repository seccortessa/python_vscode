# tip calculator 


print("Welcome to the tip calculator")
bill = float(input('What was the total bill? $'))
percentaje = 1.0 + float(input("What percentage tip would you like to give? 10, 12, or 15? "))/100
people = int(input("How many people to split the bill? "))

result = round((bill / people) * percentaje,2)
resultf = "0:4f".format(result)
print(f"Each person should pay ${result}")

