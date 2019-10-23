"""
-> dummed down to be easier to understand

Overview:

-function to get a letter
-check for repeated letters
-check if we completed the word
-get display word
"""

# Gets a single letter from an input
def guess_letter():
    letter_guess = ""
    
    while letter_guess == "":
        entered = input("Guess a letter: ")
        
        if len(entered) == 1:
            if entered.isalpha():
                letter_guess = entered
            else:
                print("Only the English alphabet will be accepted")
        else:
            print("Only a single letter is allowed")
                
    return letter_guess.lower()

# test this function by adding dummy letters
guessed_letters = []
def is_letter_guessed(letter):
    for already_guessed in guessed_letters:
        if already_guessed.lower() == letter.lower():
            return True
    return False
    
word_to_guess = "Hello"
    
def is_word_completed():
    for letter in word_to_guess:
        if letter.isalpha():
            if not is_letter_guessed(letter):
                return False
    return True
    
def get_display_word():
    display_word = ''
    
    for letter in word_to_guess:
        if is_letter_guessed(letter) or not letter.isalpha():
            display_word = display_word + letter
        else:
            display_word = display_word + "_"
        
    return display_word

guesses_left = 10
    
word_completed = False
while not word_completed:
    print("Your word: ", get_display_word())
    print("Remaining guesses: ", guesses_left)
    guess = guess_letter()
    already_guessed = is_letter_guessed(guess)
    if not already_guessed:
        guessed_letters.append(guess)
    else:
        print("You already guessed that letter!")
        continue
        
    
    #check if we finished the word
    word_completed = is_word_completed()
    if word_completed:
        print("You win! The word was: ", word_to_guess)
        break;
    
    guesses_left = guesses_left - 1
    if (guesses_left == 0):
        print("You rand out of guesses!")
        break;
    print("")

    

