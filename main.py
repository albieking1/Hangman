import time
user = input("What is your name: ")
print("Hello, " + user, "Time to play hangman!")
time.sleep(1)
time.sleep(0.5)
answer = ("secret")
guesses = ''
turns = 10
while turns > 0:
  failed = 0
  for char in answer:
    if char in guesses:
      print(char,end=""),
    else:
      print("_",end=""),
      failed += 1
  if failed == 0:
    print("You won!")
    break
  guess = input("Guess a character: ")
  guesses += guess
  if guess not in answer:
    turns -= 1
    print("Wrong!")
    print("You have", + turns, "more guesses!")
    if turns == 0:
      print("Game over, you lose!")
