from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Data i godzina: ' + str(datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"))

@app.route('/calc', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        num1 = float(request.form['liczba1'])
        num2 = float(request.form['liczba2'])
        operation = request.form['operation']
        if operation == "dodawanie":
            return 'Wynik to '+ str(num1 + num2)
        if operation == "odejmowanie":
            return 'Wynik to '+ str(num1 - num2)
        if operation == "mnozenie":
            return 'Wynik to '+ str(num1 * num2)
        if operation == "dzielenie":
            return 'Wynik to '+ str(num1 / num2)
    else:
        return '<form method="post" action="/calc"><label>Liczba 1: <input type = "number" name = "liczba1"></label><br><label>Liczba 2: <input type = "number" name = "liczba2"></label><br><label>Działanie: <select name = "operation" required><option value = "dodawanie">+</option><option value = "odejmowanie">-</option><option value = "mnozenie">*</option><option value = "dzielenie">/</option></select></label><br><button>Wynik</button><form>'
    

if __name__ == '__main__':
    app.run()