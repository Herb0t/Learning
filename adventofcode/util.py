class Util:
    startingPosition = 0
    lock = []

    def __init__(self):
        self.startingPosition = 0
        self.lock = [i for i in range(100)]

    def lockInstruction(self, instruction):
        print(instruction)
        letter = self.getLetterFromInstruction(instruction)
        number = self.getNumberFromInstruction(instruction)
        

    def getLetterFromInstruction(self, instruction):
        return instruction[0]

    def getNumberFromInstruction(self, instruction):
        #remove the first letter from the instructions 
        numberInstruction = instruction[1:]
        return int(numberInstruction)

    def move(self, letter, number):
        if letter == 'L':
            # move position to the left

        elif letter == 'R':
            # move position to the right


