import os


from day9art import logo

print(logo)
print("Welcome to the secret auction program.")

bids = {}

continueQ = True

while continueQ:
    
    name = input("What is your name?:")
    bid = int(input("What's your bid?: $"))

    bids[name] = bid
    
    
    answer = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if answer == "no":
        continueQ = False
    os.system("clear")
        
keys_list = []
values_list = []
update_value = 0
max_value  = 0
for key in bids:
    keys_list.append(key)
    values_list.append(bids[key])
    if bids[key] > update_value:
        if bids[key] > max_value:
            max_value = bids[key]
    update_value = bids[key]
    
print(keys_list)
print(values_list)
print(max_value)

max_index = values_list.index(max_value)

print("La persona que más puso fue", keys_list[max_index],"con un valor de",max_value)

