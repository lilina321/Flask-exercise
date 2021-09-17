
from flask import Flask, request
import random
app = Flask('__name__')

num = random.randint(1, 100)


@app.route('/', methods=('GET', 'POST'))
def losowanie():

    if request.method == "POST":
        guessNum = request.form['guessNum']
        if num == int(guessNum):
            return '<strong><h2>Gratulacje! Zgadłeś!</strong></h2>'
        if num > int(guessNum):
            return '<strong><h2>Za mało! Spróbuj ponownie...</strong></h2><form method="post" action="/"><label>Podaj liczbę: <input type = "number" name = "guessNum"></label><br><button>Sprawdź</button><form>'
        if num < int(guessNum):
            return '<strong><h2>Za dużo! Spróbuj ponownie...</strong></h2><form method="post" action="/"><label>Podaj liczbę: <input type = "number" name = "guessNum"></label><br><button>Sprawdź</button><form>'
    else:
        return '<strong><h2>Zgadnij liczbę od 0 do 100!</h2></strong><form method="post" action="/"><label>Podaj liczbę: <input type = "number" name = "guessNum"></label><br><button>Sprawdź</button><form>'


if __name__ == '__main__':
    app.run(debug=True)
