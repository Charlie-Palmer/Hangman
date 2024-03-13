import random

word_list = ['mango', 'kiwi', 'cherry', 'plum', 'lychee']

class Hangman:
    '''
    The hangman game
    '''
    
    def __init__(self, word_list, num_lives = 5):
        '''
        Initialise the game with a list of words and a number of lives
        '''
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word)) - len(set(self.word_guessed))
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        '''
        Checks the guesses made by the user and returns wether correct or not
        '''
        guess = guess.lower() #makes sure all guesses are lower case
        
        if guess in self.word: #checks if guess is in the word or not
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
                
    
    
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: " )
            if len(guess) != 1 or not guess.isalpha():
             print(f'Invalid letter. Please enter a single alphabetical letter')  
             
            elif guess in self.word_guessed:
             print(f'You already tried that letter!')
            
            else:
             self.check_guess(guess)
             self.list_of_guesses.append(guess)
             break
           
        return self.ask_for_input
    
hangman_game = Hangman(word_list)
hangman_game.ask_for_input()
