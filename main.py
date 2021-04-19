# -*- coding: utf-8 -*-

"""
Benson Lee
CPSC 223P-01
April 8, 2021
blee71@csu.fullerton.edu
"""

import random

# Hangman class
class Hangman: 
  def __init__(self, word, triesAllowed = 0):
    self.word = word
    self.triesAllowed = len(self.word)
    self.guesses = set()

  def Guess(self, letter):
    """Pass in a letter (length = 1) and check to see if it is in the word.
       If it is, replace blanks in display word with letter and return True
       If not, decrement the number of tries left and return False."""
    if len(letter) != 1:
      return False
    if letter in self.guesses:
      self.GetDisplayWord()
    self.guesses.add(letter)
    if letter in self.word:
      print("Good guess! Letters used: {0}".format(self.GetLettersUsed()))
      return True
    else:
      self.triesAllowed -= 1
      print()
      print("Too bad! Letters used: {0}".format(self.GetLettersUsed()))

      if (self.triesAllowed == 0):
       print("You lost! The word was {0}.".format(self.word))
       return False

  def GetNumTriesLeft(self):
    """Return the number of tries left."""
    return self.triesAllowed
    
  def GetDisplayWord(self):
    """Return the display word (with dashes where letters have not been guessed)
    i.e. the word happy with only the letter 'p' guessed so far would be '--pp-'"""
    return ''.join(c if c in self.guesses else '-' for c in self.word)
    
  def GetLettersUsed(self):
    """Return a string with the list of letters that have been used."""
    return '-'.join(self.guesses)

  def GetGameResult(self):
    """Return True if all letters have been guessed. False otherwise."""
    for i in self.word:
      if i not in self.guesses:
        return False
    return True

if __name__ == "__main__":
  # Read all the words from the hangman_words.txt file
  wordFile = open("hangman_words.txt", "r")
  wordFileText = wordFile.read()
  wordFile.close()

  # Convert the string of words in wordFile to a list
  wordFileList = wordFileText.split()
  minWord = 0
  maxWord = len(wordFileList) - 1
    
  # Seed the random number generator with current system time
  random.seed()
    
  # Get a random word 
  randomIndex = random.randint(minWord, maxWord)

  # Instantiate a game using the Hangman class
  game = Hangman(wordFileList[randomIndex])
       
  while game.GetNumTriesLeft() > 0:
    print()

    game.GetGameResult()
    print("Here's your word so far: {0}".format(game.GetDisplayWord()))
    print("You have {0} guesses left.".format(game.GetNumTriesLeft()))
    print()
    userInput = str(input("Guess a letter: "))

    if userInput.islower() and (len(userInput) == 1):
      game.Guess(userInput)
    else:
      print("Invalid character! Try again...")

    if game.GetGameResult():
      print("Congratulations! You won!! The word was {0}.".format(game.word))
      break