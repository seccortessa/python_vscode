


# we're gonna building a blackjack game

"""game rules:
1. Dealer hand himself and player a card, showing the value, and then one more card, but this one is hidden.
2. the goals is achieve 21 as scoring, so the player can take a card from maze, or stay 
3. if you have less than 17, you must take a card.
3. if one reaches more than 21, loses
4. if none reaches the 21, the player with largest number under 21 wins.

* A counts as 11 or as 1
* J,  Q and K count as 10
* the remaining cards count as it's own number.
"""
    
import random


cards = [11, 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9, 10, 10, 10, 10]

class player:
    def __init__(self,name):
        self.name = name
        self.cards = []
        self.score = 0

    def giveaCard(self):
        n = choseCard()
        self.cards.append(n)
        self.updateScore(n)
        
    def updateScore(self,newNumber):
        self.setScore(self.getScore()+newNumber)
        
    def setScore(self,score):
        self.score = score
        
    def getScore(self):
        return self.score

    def getCards(self):
        return self.cards

    def seeHand(self):
        print("You cards are:") 
        print(self.getCards()) 
        print("and the sum is:") 
        print(self.getScore()) 

def choseCard():
    return random.choice(cards)

def initGame():
    computer = player("PC")
    human_name = input("Welcome to blackjack, please type your name: ")
    human = player(human_name)
    
    computer.giveaCard()
    human.giveaCard()
    computer.giveaCard()
    human.giveaCard()
    
    onPlay = True
    
    while onPlay:
        human.seeHand()
        cont = input("Take (t) or Plant (p): ")
        human.seeHand()
        if cont == 'p' or cont == 'P'  or human.getScore() > 21 :
            onPlay = False
        if cont == 't':
            human.giveaCard()
            
        computer.seeHand()
        if computer.getScore() < 17:
            computer.giveaCard()
        if computer.getScore() < 21 and computer.getScore() > 17:
            if random.random() > 0.5:
                computer.giveaCard()
            else:
                 onPlay = False
                
        if computer.getScore() > 21:
            onPlay = False

    print('Your score is') 
    print(human.getScore())
    print("and computer score is ") 
    print(computer.getScore())

    if human.getScore() > computer.getScore() or computer.getScore() > 21:
        print("You Win!")
    elif computer.getScore() > human.getScore() or human.getScore() > 21:
        print("Computer Wins!")
        
        

initGame()

playagain = input("Do you want to play again? 'y' or 'n'")

if playagain == 'y':
    initGame()