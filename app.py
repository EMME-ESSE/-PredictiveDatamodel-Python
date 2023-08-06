from flask import Flask, render_template, request
import random

app = Flask(__name__)

player_choices = []

@app.route('/')
def RPS():
    return render_template('RPS.html')

@app.route('/PPT', methods=['POST'])
def PPT():
    user_choice = request.form['choice']
    player_choices.append(user_choice)
    computer_choice = predict_next_choice()  # Utilizar la función para predecir la elección del computador
    result = determine_winner(user_choice, computer_choice)
    return render_template('RPS.html', user_choice=user_choice, computer_choice=computer_choice, result=result)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'It\'s a tie!'
    elif user_choice == 'rock':
        return 'You win!' if computer_choice == 'scissors' else 'You lose!'
    elif user_choice == 'paper':
        return 'You win!' if computer_choice == 'rock' else 'You lose!'
    elif user_choice == 'scissors':
        return 'You win!' if computer_choice == 'paper' else 'You lose!'

def predict_next_choice():
    if not player_choices:
        return random.choice(['rock', 'paper', 'scissors']) 
    rock_count = player_choices.count('rock')
    paper_count = player_choices.count('paper')
    scissors_count = player_choices.count('scissors')
    total_choices = len(player_choices)

    rock_prob = rock_count / total_choices
    paper_prob = paper_count / total_choices
    scissors_prob = scissors_count / total_choices

    print("User Chose Rock: {} times, Paper: {} times, and Scissors: {} times".format(rock_count, paper_count, scissors_count))
    print("The probabilities are: for Rock {}, Paper {}, and Scissors {}".format(rock_prob, paper_prob, scissors_prob))

    # Elegir la opción con la mayor probabilidad como próxima elección del computador
    if rock_prob > paper_prob and rock_prob > scissors_prob:
        return 'paper' if rock_prob > 0.5 else 'scissors'
    elif paper_prob > rock_prob and paper_prob > scissors_prob:
        return 'scissors' if paper_prob > 0.5 else 'rock'
    else:
        return 'rock' if scissors_prob > 0.5 else 'paper'
    
def printuser(rock_count, paper_count, scissors_count, rock_prob, paper_prob, scissors_prob):
    print("User Chose Rock: {} times, Paper: {} times, and Scissors: {} times".format(rock_count, paper_count, scissors_count))
    print("The probabilities are: for Rock {}, Paper {}, and Scissors {}".format(rock_prob, paper_prob, scissors_prob))

if __name__ == '__main__':
    app.run(debug=True)
