import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

my_choice = [False, False , False]
pc_choice = [False, False , False]
printo = [rock, paper, scissors]

print("Welcome to the game")
my_choice[int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))] = True


# print(my_choice)

pc_choice[random.randint(0, 2)] = True
result = "You lose"

for i in range(3):
    if my_choice[i]:
        print(printo[i])
    if my_choice[i] and pc_choice[i]:
        result = "It's a tie"
        break

for i in range(3):
    if pc_choice[i]:
        print(f"Computer chose: \n{printo[i]}")


        
(pc_choice[0], pc_choice[1], pc_choice[2]) = (pc_choice[2], pc_choice[0], pc_choice[1])


for i in range(3):
    if my_choice[i] and pc_choice[i]:
        result = "You win"
        break

print(result)
