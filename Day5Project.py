import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

banco = letters + symbols + numbers
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_tot = nr_numbers + nr_symbols + nr_letters
passw = []
indice = []


for i in range(nr_tot):
    indice.append(i)
    passw.append('"')

indice = random.sample(indice, len(indice))

for i in range(nr_numbers):
    pos_pull = random.randint(1, len(numbers))
    passw[indice[i]] = numbers[pos_pull-1]
    
    
for i in range(nr_numbers,nr_symbols+nr_numbers):
    pos_pull = random.randint(1, len(symbols))
    passw[indice[i]] = symbols[pos_pull-1]

for i in range(nr_symbols+nr_numbers,nr_tot):
    pos_pull = random.randint(1, len(letters))
    passw[indice[i]] = letters[pos_pull-1]

passs = ""         
for i in passw:
    passs += i
print("The password generated is:\n",passs)