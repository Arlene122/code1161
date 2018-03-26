"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""


from exercise1 import not_number_rejector
from exercise1 import super_asker
import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    marge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    
    print("\nWelcome to the guessing Game!")
    print("A number between _ and 100 ?")
    lowerBound = input("Enter a lower bound: ") 
    print ("Ok then, a number between {0} and 100 ?".format(lowerBound))
    lowerBound = int(lowerBound)
    highbound = 100
    actualNumber = random.randint(lowerBound, 100)

    guessed = False

    while not guessed:
      try:
        guessedNumber = int(input("guess a number:")) #this is now considered an integer due to int
        print("you guessed {0},".format(guessedNumber))
      except ValueError: #error will occur if guesser input a non integer within range
        print("sorry, i will on process an integer, try again")
        continue 
      if (guessedNumber < lowerBound or guessedNumber > highbound):
        print("That is not in range")
      elif guessedNumber == actualNumber:
        print("You got it! It was {}".format(actualNumber))
        guessed = True
      elif guessedNumber < actualNumber:
        print("Too small, try again   ")
      else:
        print("Too big, Try again")
    
    return ("You Got It!")
      
      

if __name__ == "__main__":
    advancedGuessingGame()
