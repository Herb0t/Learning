from util import Util
import getpass

# ask the user for a word to guess
word = getpass.getpass("Enter a word to guess: ")

util = Util(word)

# # check if letter is in hiddenwordarray
while True:
    selectedLetter = input("Enter a letter: ")
    
    if util.check_letter(selectedLetter):
        if util.check_if_won():
            print("You won!")
            break
    else:
        print("Letter not found")

    util.draw_hanged_man()
    
    if util.check_if_lost():
        print("You lost!")
        break
print("The word was: " + word)