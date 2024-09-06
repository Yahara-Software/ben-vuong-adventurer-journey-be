import math

# This function uses the pythagorean theorem to calculate straight line distance between the start and end of an "adventure path" 
# based on a string that represents steps taken by an adventurer.
# Assumptions:
# - The adventurer takes even steps
# - The input string is well formed (only non-numeric characters are F,B,R,L)
# - If the adventurer moves left or right, their "forward" direction stays the same (they are moving in a strafing motion, side-to-side, while still facing the same direction)

def calculate_journey_distance_from_path_string(pathStr):
    currentVal = ""
    verticalTotal = 0
    horizontalTotal = 0

    for char in pathStr:
        if char.isnumeric():
            currentVal += char
        else:
            if char == 'F':
                verticalTotal += int(currentVal)
                currentVal = ""
            elif char == 'B':
                verticalTotal -= int(currentVal)
                currentVal = ""
            elif char == 'R':
                horizontalTotal += int(currentVal)
                currentVal = ""
            elif char == 'L':
                horizontalTotal -= int(currentVal)
                currentVal = ""

    return math.sqrt(horizontalTotal * horizontalTotal + verticalTotal * verticalTotal)

print("Straight line distance from start to end of path:", calculate_journey_distance_from_path_string("15F6B6B5L16R8B16F20L6F13F11R"), "steps")