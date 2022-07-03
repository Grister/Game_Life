from flask import Flask, render_template
from game_of_life import GameOfLife

app = Flask(__name__)


@app.route('/')
def index():
    GameOfLife(20, 20)
    return render_template('index.html')


@app.route('/live')
def live():
    game = GameOfLife()
    game.counter += 1
    game.form_new_generation()
    return render_template('live.html', game=game)


if __name__ == '__main__':
    app.run(debug=True)
