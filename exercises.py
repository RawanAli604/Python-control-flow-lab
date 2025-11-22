# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()

# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    
    vowels = "aeiou"
    letter = input('enter a letter (a-z or A-Z)').lower()
    if letter in vowels:
      print(f"The letter {letter} is a vowel.")
    elif letter.isalpha():
      print(f"The letter {letter} is a consonant.")
    else:
      print("It is anInvalid entry")

# Call the function
check_letter()

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
 try:
   age = int(input("Please enter your age: "))
   if age <= 0:
     print("Age cannot be negative or a letter. Please enter a valid age.")
     return
   vote_age = 18
   if age >= vote_age:
     print("You are eligible to vote")
   else:
     print("You aren't eligible to vote") 

 except ValueError:
     print("Invalid input. Please enter a valid number for your age.")

  
# Call the function
check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
  try:
    dog = int(input("Input a dog's age: "))
    if dog <= 2:
      if dog == 1:
        dog_age = 10
      elif dog == 2:
        dog_age = 20
    else:
      dog_age = dog*7

    print(f"The dog's age in dog years is {dog_age}")

  except ValueError:
    print("Invalid input")
# Call the function
calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    ans = ["yes", "no"]

    cold_input = input("Is it cold? (yes/no): ").lower()
    if cold_input not in ans:
        print("Invalid input. Please type 'yes' or 'no'.")
        return
    
    raining_input = input("Is it raining? (yes/no): ").lower()
    if raining_input not in ans:
        print("Invalid input. Please type 'yes' or 'no'.")
        return
    
    is_cold = cold_input == "yes"
    is_raining = raining_input == "yes"

    if is_cold and is_raining:
        print("Wear a waterproof coat.")
    elif is_cold and not is_raining:
        print("Wear a warm coat.")
    elif not is_cold and is_raining:
        print("Carry an umbrella.")
    else:
        print("Wear light clothing.")

# Call the function
weather_advice()

# Exercise 6: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

def guess_number():
  target = 42
  max = 5
  print("Guess a number between 1 and 100, you have 5 guesses")

  for attempt in range(1, max+1):
    try:
     if attempt == max-1:
        print("Last chance!")

     guess = int(input(f"Attempt {attempt}: Enter your guess: "))
     if guess < 1 or guess > 100:
        print("Your guess must be between 1 and 100.")
        continue

     if guess == target:
        print("Congratulations, you guessed correctly!")
        return
     elif guess < target and guess != target:
        print("Your guess is too low.")
     elif guess > target and guess != target:
        print("Your guess is too high.")
    
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

  print("Sorry, you failed to guess the number in five attempts.")
# Call the function
guess_number()

