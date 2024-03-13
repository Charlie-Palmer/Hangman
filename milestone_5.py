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
            for x in range(0, len(self.word)):
                if self.word[x] == guess: #adds guess to word if correct
                    self.word_guessed[x] = guess
            self.num_letters -= 1
        else: #reduce number of lives if wrong
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.num_lives -= 1
            print(f'You have {self.num_lives} lives left.')
                
    
    
    def ask_for_input(self):
        '''
        Asks user for an input and if the letter is valid will pass check_guess function.
        '''
        while True:
            guess = input("Guess a letter: " ) #asks for a letter and checks if valid
            if len(guess) != 1 or not guess.isalpha():
             print(f'Invalid letter. Please enter a single alphabetical letter')  
             
            elif guess in self.list_of_guesses: #blocks repeat guesses
             print(f'You already tried that letter!')
            
            else: #checks guess and adds to list of guesses
             self.check_guess(guess)
             self.list_of_guesses.append(guess)
             break
           
        return self.ask_for_input
    

def play_game(word_list):
    '''
    Function to play the hangman game
    '''
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print(f'You lost!')
            break
        
        elif game.num_lives != 0 and game.num_letters < 0:
            print('Congratulations. You won the game!')
            break    
        elif game.num_letters > 0:
            game.ask_for_input()
        

play_game(word_list)
    