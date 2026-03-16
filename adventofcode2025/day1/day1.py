from day1util import Util

lockInstructions = []
with open("./adventofcode/day1input.txt", "r") as file:
    lockInstructions = file.readlines()

util = Util()

for instruction in lockInstructions:
    util.lockInstruction(instruction)

print(util.zeroCount)