import random

word_list = ['Mango', 'Kiwi', 'Cherry', 'Plum', 'Lychee']

word = random.choice(word_list)

print(word)
Guess = input("Please enter a letter: ")
if len(Guess) == 1 and Guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
        
