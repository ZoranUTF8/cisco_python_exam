# Imagine that your computer program loves these plants. Whenever it receives an input in the form of the word Spathiphyllum, it involuntarily shouts to the console the following string: "Spathiphyllum is the best plant ever!"
#
# Write a program that utilizes the concept of conditional execution, takes a string as input, and:
#
# prints the sentence "Yes - Spathiphyllum is the best
# plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
# prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
# prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.

def get_result():
    userInput = str(input("Enter text?"))

    if userInput == ("Spathiphyllum"):
        print("Yes - Spathiphyllum is the best plant ever!")
    elif userInput == ("spathiphyllum"):
        print("No, I want a big Spathiphyllum!")
    else:
        print(f"Spathiphyllum! Not {userInput}!")

get_result()