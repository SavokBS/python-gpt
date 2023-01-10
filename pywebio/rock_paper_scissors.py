from pywebio.input import button_group
from pywebio.output import put_html
import random

def play_game():
    put_html("""
    <h1>Rock-Paper-Scissors</h1>
    <p>Make your choice:</p>
    <div id="buttons"></div>
    <br>
    <br>
    <div id="result"></div>
    """)
    choices = ["rock", "paper", "scissors"]
    player_choice = button_group("buttons", choices, labels=choices)
    computer_choice = random.choice(choices)
    
    result = ""
    if player_choice == computer_choice:
        result = "Tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        result = "You Win!"
    else:
        result = "You Lost!"
    
    put_html(f"<p>You chose {player_choice}, computer chose {computer_choice}.</p>")
    put_html(f"<p>{result}</p>")
    
play_game()
