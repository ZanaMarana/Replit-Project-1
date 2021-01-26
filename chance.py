print("Die roll function: ")
from random import randrange #imports randrange
def dieRoller (): #defines function
  return (randrange(1, 6)) #returns random integer
print(dieRoller()) #uses function 

print()

print("Random odd number function: ")
from random import randint
def oddRandom(): #defines oddRandom function
  return randint(1, 102) #searches between 1 to 102
while True: #loops infinitely until broken
  randy=oddRandom() #sets a variable to the odd roll
  if randy%2==1: #checks if evenly divisible by 2 (odd)
    print(randy) #prints odd random number
    break #breaks loop
  else: #otherwise
    pass #passes through

print()

print("Double die roll function:")
def dieRoller (): #defines function
  return (randrange(1, 6),randint(1,6)) #returns random integer twice
print(dieRoller()) #uses function to get two dice rolls

print()

print("Deck of cards function:")
from random import shuffle
def pick_card():
  card_type = ['Clubs', 'Diamonds', 'Hearts', 'Spades'];
  card_number = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']    
  # shuffle the cards
  shuffle(card_type) 
  shuffle(card_number) 
  return [card_number[0], card_type[0]] #returns the first card on the shuffled deck
# Show the randomly picked card
print(pick_card())

print()

print("Random city function:")
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"] #creates list
from random import choice #imports choice function
city=choice(cities) #chooses random city
print(city) #returns one city