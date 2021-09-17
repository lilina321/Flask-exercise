
from flask import Flask, request
app = Flask('__name__')

form = '''
<form action="/" method="POST">
    <h2>Formularz</h2>
    <label>Podaj imię: <input name = 'name' type = 'text' required></label><br>
    <label>Podaj nazwisko: <input name = 'surname' type = 'text' required></label><br>
    <button>Wyślij</button>
</form>
'''
@app.route('/',  methods=('GET', 'POST'))
def hello():
    if request.method == 'POST':
        return 'Witaj ' + request.form['name'] + ' ' + request.form['surname'] + '!'
    else:
        return form

if __name__ == '__main__':
    app.run(debug=True)
