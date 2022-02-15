import random

dic = ["South", "world", "about", "again", "heart", "pizza", "water", "happy", "sixty", "board", "month", "Angel", "death", "green", "music", "fifty", "three", "party", "piano", "Kelly", "mouth", "woman", "sugar", "amber", "dream", "apple", "laugh", "tiger", "faith", "earth", "river", "money", "peace", "forty", "words", "smile", "abate", "house", "alone", "watch", "lemon", "South", "erica", "anime", "after", "santa", "women", "admin", "jesus"]


result_word = ["_","_","_","_","_"]
counter = 0
player_letters = []
game_on = None

def play ():
  ask = input ("Do you want to play wordledurdle? \n")
  if ask == "yes":
    game_on = True
    
  else:
    game_on = False
  
  return game_on

''''
def play_again():
  ask = input ("Do you want to play wordledurdle again? \n")
  if ask == "yes":
    game_on = True
    counter = 0
  else:
    game_on = False
  
  return game_on
'''

def player_guess():
  player_word = input("enter a 5 leter word \n")
  player_letters = list(player_word)
  return player_letters

def compare_words(player_letters):
  for x in range(0,5):
    if player_letters[x].upper() == letters[x]:
      result_word[x] = player_letters[x].upper()
      
    elif player_letters[x].upper() in letters:
      result_word[x] = player_letters[x]
      
    else:
      result_word[x] = "_"

  return result_word

def check_win():   
  if result_word == letters:
    print ("congrats you win!")
    
    return True
  

game_on = play()

while game_on == True:
  word = (random.choice(dic)).upper()
  letters = list(word)
  while counter < 6:
    player_letters = player_guess()
    compare_words(player_letters)
    print (result_word)
    if check_win() == True:
      break
      play()
    counter +=1
  if result_word != letters:
    print (f"sorry you looooseee! the word was {word}")
  counter = 0
  game_on =play()