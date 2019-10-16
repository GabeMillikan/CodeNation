
class Word():
    guessed_letters = []

    def __init__(self, word):
        self.word = word
        
    def play(self):
        guess = input("guess a letter: ")
        if guess.isalpha() and len(guess) == 1:
            self.guessed_letters.append(guess)
        else:
            print("Only a single letter please")

round = Word("epic")

while True:
    round.play()
    print(round.guessed_letters)