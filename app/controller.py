
from flask import render_template, request, redirect
from app import app
from app.models.game import Game
from app.models.player import Player
from app.models.selection import Selection

@app.route('/')
def index():
    return render_template('base.html', title="Home")

@app.route('/game_start')
def game():
    return render_template('game_start.html', title="Game")

@app.route('/game_start/rock')
def rock():
    return render_template('rock.html')

@app.route('/game_start/paper')
def paper():
    return render_template('paper.html')

@app.route('/game_start/scissors')
def scissors():
    return render_template('scissors.html')

@app.route('/game_start/<choice1>/<choice2>')
def result(choice1, choice2):
    if choice1 == 'rock':
        choice_1 = Selection.ROCK
    elif choice1 == 'paper':
        choice_1 = Selection.PAPER
    elif choice1 == 'scissors':
        choice_1 = Selection.SCISSORS

    if choice2 == 'rock':
        choice_2 = Selection.ROCK
    elif choice2 == 'paper':
        choice_2 = Selection.PAPER
    elif choice2 == 'scissors':
        choice_2 = Selection.SCISSORS
    player_1 = Player("Jeffy", choice_1)
    player_2 = Player("Grant", choice_2)

    play_game = Game.play_game(player_1, player_2)
    return render_template('result.html', winner=play_game)



    

    