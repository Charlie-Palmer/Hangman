import random

word_list = ['mango', 'kiwi', 'cherry', 'plum', 'lychee']

word = random.choice(word_list)
print(word)

def check_guess(guess):
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
    return check_guess


def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please enter a single alphabetical character")
    check_guess(guess)
    return ask_for_input



ask_for_input()    