from drawhang import draw_hanged_man

class Util:
    word = ""
    hiddenwordarray = []
    wrongGuessesCount = 0
    wrongGuesses = []
    correctGuesses = []

    def __init__(self, word):
        self.word = word
        for letter in word:
            self.hiddenwordarray.append([letter, "0"])

    def check_letter(self, letter):
        if letter.lower() in self.word.lower():
            self.update_hiddenwordarray(letter)
            return True
        else:
            self.wrongGuessesCount += 1
            self.wrongGuesses.append(letter)
            return False

    def check_if_won(self):
        for item in self.hiddenwordarray:
            if item[1] == "0":
                return False
        
        self.print_hiddenwordarray()
        return True

    def check_if_lost(self):
        if self.wrongGuessesCount >= 6:
            return True
        return False

    def update_hiddenwordarray(self, letter):
        for index, item in enumerate(self.hiddenwordarray):
            if letter.lower() in item[0].lower() and item[1] == "0":
                self.hiddenwordarray[index][1] = "1"

    def draw_hanged_man(self):
        draw_hanged_man(self.wrongGuessesCount)
        self.print_hiddenwordarray()
        self.print_wrong_guesses()

    def print_wrong_guesses(self):
        print("Wrong guesses: ")
        for item in self.wrongGuesses:
            print(item, end=" ")
        print()

    def print_hiddenwordarray(self):
        for item in self.hiddenwordarray:
            if item[1] == "1":
                print(item[0], end=" ")
            else:
                print("_", end=" ")
        print()