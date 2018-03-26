# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""
# 3 steps a while loop needs:

# i = 0      variable initialization
# while(i < 5)  loop condition on that variable
#    print(i)
#    i = i+1 or i +=1    Variable change value



def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from just using range()
    """
    counter = start #while loops are foer when you dont know how long somthing is going to go for, for loop you know the range
    a_list = []
    while counter < stop:
        a_list.append(counter)
        counter += step #this saves the value of step, updates counter
    return a_list
        


def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """
    x = range(start,stop,step)
    f = list(x)
    return f 
    


def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """
    a_list = []
    counter_a = start
    counter_b = stop
    step_2 = 2 # giving step_2 a value
    while counter_a < counter_b: # sets the loop conditions
        a_list.append(counter_a)
        counter_a += step_2 #this saves the value of step and updates counter
    return a_list


def gene_krupa_range(start, stop, even_step, odd_step):
    """Make a range that has two step sizes.

    make a list that instead of having evenly spaced steps
    has odd steps be one size and even steps be another.
    """
    step = 0
    counter = start
    a_list = []
    while counter < stop:
        a_list.append(counter)
        if step % 2 == 1: 
            counter += even_step
        else:
            counter += odd_step
        step += 1
    return a_list
    

def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK
    """
    message = "Give me a number between {low} and {high}:".format(low=low,high=high)
    while True:
        guessed_number = int(input(message)) 
        
        if low < guessed_number < high: #sets the condition 
            print("{} is a correct number".format(guessed_number))
            return guessed_number
        else: 
            print ("{} not in range, try again".format(guessed_number))




def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number (e.g. "cow",
    "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    
    while True: 
        try:
            guessed_Number = int(input("Enter a number:"))
            a_number = int(guessed_Number) # makes it an integer
            return a_number
        except ValueError: #if the guesser uses a non integer it will be an error and process to print next line
            print("Sorry, that is not an integer, please try again")
    return None




import random
def super_asker(low, high):
    """Robust asking function.

    Combine stubborn_asker and not_number_rejector to make a function
    that does it all!
    """

    message = "Give me a number between {low} and {high}:".format(low=low,high=high)
    guessed_number = int(input(message))
    while True:
        if low < guessed_number < high: #sets the condition 
            print("{} is a number within the range".format(guessed_number))
            return guessed_number
        elif low > guessed_number > high:
            print ("{} not in range, try again".format(guessed_number))
        else:
            try:
                guessed_number = int(input(message))
                print("you guessed {},".format(guessed_number),)
            except ValueError: 
                print("Sorry, that is not an integer, please try again")

    return "You got it"



                

if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from
    

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\ngene_krupa_range", gene_krupa_range(1, 20, 2, 5))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)
