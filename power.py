from flask import Flask, request, render_template
app = Flask('__name__')

def res():
    n = int(request.form['number'])
    n_power = str(n ** 2)
    n_power_n = str(n**n)
    return render_template("res.html", content = n_power, content2 = n_power_n)


@app.route('/', methods=('GET', 'POST'))
def power():
    if request.method == 'POST':
        return res()
    else:
        return render_template("index.html")
    

if __name__ == '__main__':
    app.run(debug=True)