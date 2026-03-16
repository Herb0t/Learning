from util import Util

batteryBanks = []
with open("./adventofcode2025/day3/input.txt", "r") as file:
    batteryBanks = file.read().splitlines()




util = Util()
# batteryBanks = [
# "987654321111111",
# "811111111111119",
# "234234234234278",
# "818181911112111",
# ]

for batteryBank in batteryBanks:
    string = util.findLargestJoltage(batteryBank)

print(util.outputJoltage)


# 17387
