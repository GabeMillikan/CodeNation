alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet = "abcdefghijklmnopqrstuvwxyz"

class Word():
    guessed_letters = []

    def __init__(self, word):
        self.word = word
        self.finished = False
        self.remaining_guesses = 10
        
    def already_guessed(self, check):
        for letter in self.guessed_letters:
            if letter.lower() == check.lower():
                return True
        return False
        
    def letters_left(self):
        left = []
        
        for letter in alphabet:
            if not self.already_guessed(letter):
                left.append(letter)
                
        return left
        
    def get_print_word(self):
        out = ""
        for letter in self.word:
            if self.already_guessed(letter):
                out += letter
            else:
                if not letter.isalpha():
                    out+=letter
                else:
                    out += "*"
            
        return out
        
    def guess_correct(self, check):
        for letter in self.word:
            if letter.lower() == check.lower():
                return True
                
        return False
        
        
    def play(self):
        print("\nThe word is: ", end = '')
        print(self.get_print_word())
        
        print("Remaining guesses: ", self.remaining_guesses)
        
        print("Letter Bank: ", end = '')
        for l in self.letters_left():
            print(l, end=' ')
        print()
    
        guess = input("guess a letter: ")
        if not guess.isalpha():
            print("please only enter letters!")
            return
        if not len(guess):
            print("you gotta enter something")
            return
        if len(guess) > 1:
            print("Please only enter one letter")
            return
        
        if self.already_guessed(guess):
            print("You already guessed that!")
            return            
            
        self.guessed_letters.append(guess)
        self.guessed_letters.sort()
        if not self.guess_correct(guess):
            self.remaining_guesses -= 1
        
        if (self.get_print_word().lower() == self.word.lower()):
            print()
            print("You win!")
            print("The word was : '" + self.word + "'")
            return True
            
        if self.remaining_guesses <= 0:
            print()
            print("You lose!")
            print("The word was : '" + self.word + "'")
            return True
            
            
        return False
            
            
round = Word("1: One, 2: Two, 3: Three")
finished = False
while not finished:
    finished = round.play()
    
    
    
    
    