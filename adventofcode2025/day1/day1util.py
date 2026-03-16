class Util:
    startingPosition = 0
    zeroCount = 0
    lock = []

    def __init__(self):
        self.startingPosition = 50
        self.lock = [i for i in range(100)]
        self.zeroCount = 0

    def lockInstruction(self, instruction):
        # print(instruction)
        letter = self.getLetterFromInstruction(instruction)
        number = self.getNumberFromInstruction(instruction)
        self.move(letter, number)

    def getLetterFromInstruction(self, instruction):
        return instruction[0]

    def getNumberFromInstruction(self, instruction):
        #remove the first letter from the instructions 
        numberInstruction = instruction[1:]
        return int(numberInstruction)

    def move(self, letter, number):
        # print(letter, number)
        direction = 1 if letter == 'R' else -1  

        for i in range(number):
            newPosition = self.startingPosition + direction
            if self.hitOutOfBounds(newPosition):
                newPosition = self.moveInBounds(newPosition)
            self.startingPosition = newPosition
        
            if self.startingPosition == 0:
                self.zeroCount += 1
        # print(self.startingPosition)

    def hitOutOfBounds(self, number):
        if number < 0 or number > 99:
            return True
        return False

    def moveInBounds(self, number):
        if number < 0:
            return 99
        if number > 99:
            return 0
        return number