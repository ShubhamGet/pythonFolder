# choices: it returns a list with a random selection from the given sequence.
import random

myname = ["Shubh", "Maan", "Golu"]

print(random.choices(myname, weights = [5, 1, 1], k = 5))