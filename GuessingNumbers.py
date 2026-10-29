import random
import sys

def welcome_message():
  print("=" * 20)
  print("welcome ; you're here to guess a number between 1 to 100")
  print("=" * 20)
  print("Your guess is now generated !")
  print("be aware that you have only 5 chances to find the number")

def hint_generator(diff, guess, correct_guess):
  if guess > correct_guess:
    direction = "Your guess is bigger than the chosen number !"
  else:
    direction = "Your guess is smaller than the chosen number !"

  if diff <= 5:
    closeness = "You're too close !"
  elif diff <= 15:
    closeness = "You're close but you gotta guess closer !"
  else:
    closeness = "You're too far !"

  return f"{closeness} (&) {direction}"

def ranking_system(attempts):
  rank_chart = {
      1: "You're the best , WELL DONE !!!",
      2: "Very good level of guessing !!",
      3: "That's kinda good !",
      4: "let's say it's acceptable",
      5: "You gotta try more next time",
  }
  return rank_chart.get(attempts, "")

def input_verify():
  while True:
    user_input = input("Enter a number between 1 to 100 as your guess: ")
    if user_input.isdigit():
      number = int(user_input)
      if 1 <= number <= 100:
        return number
      else:
        print("ERROR: Please enter a valid number from 1 to 100")
    else:
      print("ERROR: Please only enter valid integer number")

def start_game():
  correct_guess = random.randint(1, 100)
  left_attempts = 5
  used_attemps = 0

  while used_attemps < left_attempts:
    print("=" * 20)
    print(f"you have guessed {used_attemps} attempts from {left_attempts} !")
    guess = input_verify()
    used_attemps += 1

    diff = abs(guess - correct_guess)
    
    if guess == correct_guess:
      print("=" * 20)
      print(
          f"YAY , you won & you found the correct number {correct_guess} !!!"
      )
      print(f"RANKING DEPENDING ON YOUR TRIES : {ranking_system(used_attemps)}")
      print("=" * 20)
      return True

    hint = hint_generator(diff, guess, correct_guess)
    print(f"Guidance System Says : {hint}")

    if used_attemps == left_attempts:
      print("=" * 20)
      print("SORRY , you lost (you reached your max attempts)")
      print(f"the correct number was {correct_guess}")
      print("=" * 20)
      return False

def main():
  welcome_message()
  while True:
    start_game()

    while True:
      choice = input("do you wanna play again? (yes/no): ").strip().lower()

      if choice in ["بله", "y", "yes"]:
        print("New game begins ...\n")
        break
      elif choice in ["خیر", "n", "no"]:
        print("Bye ! thanks for playing :)")
        sys.exit()
      else:
        print("Pls enter a valid choice !!")

"""the text below is actually making sure that the user is running the program directly"""

if __name__ == "__main__":
  main()
