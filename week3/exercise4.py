# -*- coding: UTF-8 -*-
"""Week 3, Exercise 4."""


import math
# import time


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    Each guess, print what the guess is Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}
    This will be quite hard, especially hard if you don't have a good diagram!

    Debugging helpers:
      * GUARD is there to make it only run a few times so that you can see
        what's happening.
      * time.sleep(0.5) makes it pause for half a second.
      You don't need to use both together, and should remove them both before
      you submit. The tests will be checking that they aren't in there.
      (You should remove them from the file, not comment them out, the
      tests aren't that smart yet.)
    """

  #my answer
  #count = 1
  #s = int((low + high) / 2)
  #while actual_number != s:
  # if s < actual_number:
  #    low = s
  #  else:
  #    high = s
  #  s = int((low + high) / 2)
  #  count = count
  #return {"guess": s, "tries": count}

  
  
  d = {"guess": [], "tries": 0}:
  current = int(high/2)
  current_high = high
  current_low = low
  while current != actual_number:
    if actual_number < current:
      current_high = current
      current = int((current_high + current_low)/2)
    elif actual_number > current:
      current_low = current
      current = int((current_high + current_low)/2)
    d["guess"].append(current)
    d["tries"] += 1
  return d

if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
