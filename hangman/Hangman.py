"""

-create an array
-print array
-append to array
-access index of array
-get length of array
-loop thru array

-create string "is an array"
-access index of string
-get length of string
-loop thru letters in string
-"append" to string (+=)


-on each iteration of string, print if letter.isalpha()
-print letter.lower()/.upper()

-compare each letter to 'h' or 'e'
-make a class that prints input
-only accepts 1 letter
-only accepts alphabetical

-class stores all the letters that you pressed
-removes duplicates

g

"""

hi = 'hi'



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
            print("\nplease only enter letters!\n")
            return
        if not len(guess):
            print("\nyou gotta enter something\n")
            return
        if len(guess) > 1:
            print("\nPlease only enter one letter\n")
            return
        
        if self.already_guessed(guess):
            print("\nYou already guessed that!\n")
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
            
            
round = Word("Example 'word' with spaces and punctuation.")
finished = False
while not finished:
    finished = round.play()
    
    
    
    
    