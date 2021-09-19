from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])

def przelicznik():
    if request.method == 'POST':
        if request.form['waluta'] == 'EUR' and request.form['waluta2'] == 'EUR':
            return 'Wynik: ' + request.form['kwota'] + ' ' + request.form['waluta2']
        if request.form['waluta'] == 'EUR' and request.form['waluta2'] == 'PLN':
            return 'Wynik: ' + str(int(request.form['kwota']) * 4.6) + ' ' + request.form['waluta2']
        if request.form['waluta'] == 'EUR' and request.form['waluta2'] == 'USD':
            return 'Wynik: ' + str(int(request.form['kwota']) * 1.17) + ' ' + request.form['waluta2']

        if request.form['waluta'] == 'PLN' and request.form['waluta2'] == 'PLN':
            return 'Wynik: ' + request.form['kwota'] + ' ' + request.form['waluta2']
        if request.form['waluta'] == 'PLN' and request.form['waluta2'] == 'EUR':
            return 'Wynik: ' + str(int(request.form['kwota']) * 0.22) + ' ' + request.form['waluta2']
        if request.form['waluta'] == 'PLN' and request.form['waluta2'] == 'USD':
            return 'Wynik: ' + str(int(request.form['kwota']) * 0.26) + ' ' + request.form['waluta2']

        if request.form['waluta'] == 'USD' and request.form['waluta2'] == 'USD':
            return 'Wynik: ' + request.form['kwota'] + ' ' + request.form['waluta2']
        if request.form['waluta'] == 'USD' and request.form['waluta2'] == 'EUR':
            return 'Wynik: ' + str(int(request.form['kwota']) * 0.85) + ' ' + request.form['waluta2']
        if request.form['waluta'] == 'USD' and request.form['waluta2'] == 'PLN':
            return 'Wynik: ' + str(int(request.form['kwota']) * 3.92) + ' ' + request.form['waluta2']
    else:
        return render_template('waluty.html')

if __name__ == '__main__':
    app.run(debug = True)
