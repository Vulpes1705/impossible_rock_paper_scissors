# 
import time
version = "0.9.0"

greeting = "***Hello! Welcome to the Impossible Rock-Paper-Scissors game***"

time.sleep(1)
print(greeting)
time.sleep(1)
print("The current version is " + version)
time.sleep(1)
print("Let's play. Make your choice. Rock, Paper or Scissors?")
players_choice = input("Please type \"Rock\" , \"Paper\" or \"Scissors\" ")
if players_choice == "Rock":
    print("You've chosen " + players_choice + ". My choice is Paper. Game over.")
elif players_choice == "Paper":
    print("You've chosen " + players_choice + ". My choice is Scissors. Game over.")
elif players_choice == "Scissors":
    print("You've chosen " + players_choice + ". My choice is Rock. Game over.")
else:
    print("Please choose \"Rock\" , \"Paper\" , or \"Scissors\"")



