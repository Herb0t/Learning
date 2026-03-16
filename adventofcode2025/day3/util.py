class Util:
    outputJoltage = 0
    
    def findLargestJoltage(self, batteryBank):
        firstJoltageNum = 0
        highestFirstJoltageIndex = 0
        for index, battery in enumerate(batteryBank):
            if int(battery) > firstJoltageNum and index != len(batteryBank) - 1:
                firstJoltageNum = int(battery)
                highestFirstJoltageIndex = index

        print("highest first joltage index: " + str(firstJoltageNum))
        print("first joltage num: " + str(batteryBank))
        
        print("battery bank: " + str(batteryBank[highestFirstJoltageIndex:]))
        secondJoltageNum = 0
        for index, battery in enumerate(batteryBank[highestFirstJoltageIndex + 1:]):
            if int(battery) > secondJoltageNum:
                secondJoltageNum = int(battery)

        self.outputJoltage += int(str(firstJoltageNum) + str(secondJoltageNum))
        print(str(firstJoltageNum) + str(secondJoltageNum))



        