class Util:
    start = 0
    end = 0
    invalidSum = 0
    rangeArray = []

    def breakDownRanges(self, ranges):
        rangeList = ranges.split(",")
        for range in rangeList:
            self.rangeArray.append([int(range.split("-")[0]), int(range.split("-")[1])])

    def checkListForInvalidNumbers(self, ranges):
        self.breakDownRanges(ranges)

        for rangeNumbers in self.rangeArray:
            print("checking range: " + str(rangeNumbers[0]) + " to " + str(rangeNumbers[1]))
            for number in range(rangeNumbers[0], rangeNumbers[1] + 1):
                if self.isInvalid(number):
                    self.invalidSum += number

    def isInvalid(self, number):
        compareChecks = []
        comparing = True
        
        index = 1

        if str(number)[0] == '0':
            return False

        # check if any numbers repeat more than once
        # Pattern must repeat at least twice (need 2+ chunks)
        while comparing:
            if len(str(number)) % index == 0 and len(str(number)) // index >= 2:
                numString = str(number)
                numCompare = numString[:index]
                compareChecks = []
                for counter in range(int(len(numString) / index)):
                    if str(numString[(counter * index):((counter + 1) * index)]) == str(numCompare):
                        compareChecks.append(True)
                    else:
                        compareChecks.append(False)
                # Return invalid as soon as we find a repeating pattern
                if False not in compareChecks:
                    print("invalid number: " + str(number))
                    return True

            index += 1

            if index >= len(str(number)):
                comparing = False

        return False
    # def isOdd(self, length):
    #     return length % 2 != 0