import os
import time

win = 0

players = {
  "wrongcount" : [0, 0],
  "usword" : ['', ''],
  "word" : ['', ''],
  "wrongguess" : [[],[]],
  "guesses" : [[],[]],
}

def usgen(word, guesses):
  usword = ''
  for letter in word:
    if letter in guesses:
      usword+= f" {letter} " #replaces underscore with letter when player guesses correctly
    else:
      usword+=" _ " #replaces letter with underscore
  return usword

gameboard = ["","O","O\n|"," O\n/|"," O\n/|\\"," O\n/|\\\n/"," O\n/|\\\n/ \\"] #array of different limbs for the stickman


def turn(player):
  global win
  global otherplayer
  otherplayer = (player+1)%2 #changes player turn
  print(gameboard[players["wrongcount"][player]]) #prints the stick figure
  print(players["usword"][otherplayer]) #prints the word that is underscored
  print(players["wrongguess"][player]) #prints the board of wrong guesses
  playerguess = input(f"Player {player + 1} Choose A Letter: ") #f-string changes what player is displayed

  if playerguess not in players["word"][otherplayer]: #checks if the letter is not in the other player's word
    os.system("clear")
    players["wrongcount"][player] += 1 #adds a limb if guess is wrong
    print(gameboard[players["wrongcount"][player]]) #prints stick figure
    players["wrongguess"][player].append(playerguess) #adds players guess to the list of wrong letters
    print(players["usword"][otherplayer]) #prints the underscored word
    print(players["wrongguess"][player]) #prints the list of wrong letters

  else:
    os.system("clear")
    players["guesses"][player].append(playerguess) #adds the letter to the list of correct guesses
    print(gameboard[players["wrongcount"][player]]) #prints the hangman
    players["usword"][otherplayer] = usgen(players["word"][otherplayer], players["guesses"][player]) #replaces underscore with correct letter
    print(players["usword"][otherplayer]) #prints the underscored word
    print(players["wrongguess"][player]) #prints board of wrong guesses
    playerwordguess = input(f"Player {player + 1} Guess The Word: ")

    if playerwordguess == players["word"][otherplayer]: #checks if guess is correct
      print(f"Player {player+1} Wins!")
      time.sleep(1)
      print("The Correct Word Was " + players["word"][otherplayer]) #displays the word that was guessed correctly
      time.sleep(2)
      win = 1 #sets win to 1 so game can restart
  os.system("clear")

def intro(): #plays on start and after win
  print("Welcome to Hangman!")
  time.sleep(1.5)
  print("Player 1's Turn")
  players["word"][0] = input("Player 1 Choose a Word: ").lower()
  players["usword"][0] = usgen(players["word"][0], []) #replaces the word with underscores

  os.system("clear")

  print("Player 2's Turn")
  players["word"][1] = input("Player 2 Choose a Word: ").lower()
  players["usword"][1] = usgen(players["word"][1], []) #replaces the word with underscores
  os.system("clear")

def reset():
  players["wrongcount"] = [0, 0]
  players["wrongguess"] = [[],[]]
  players["guess"] = [[],[]]

intro()

pturn = 0
while True:
  #checks win and resets if player wins
  if win == 1 or players["wrongcount"][0] == 6 or players["wrongcount"][1] == 6: #checks if win condition; if not, checks if a player has 6 limbs.
    print(f"Player {otherplayer} has Won!")
    time.sleep(1.5)
    os.system("clear")
    reset()
    intro()
    pturn = 0
    win = 0
  else:
    #changes to a different player's turn
    turn(pturn)
    if pturn == 0:
      pturn = 1
    else:
      pturn = 0