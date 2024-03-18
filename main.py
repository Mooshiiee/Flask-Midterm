from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/listrandom/<int:n>')
def listrandom(n):
    random_list = []
    for i in range(n):
        random_list.append(random.randint(1,99))
    return render_template('listrandom.html', random_list=random_list)

@app.route('/mult/<int:n1>/<int:n2>')
def multiply(n1,n2):
    result = n1 * n2 
    return render_template('calculator.html', result=result)


@app.route('/div/<int:n1>/<int:n2>')
def divide(n1,n2):
    result = n1/ n2 
    return render_template('calculator.html', result=result)


@app.route('/add/<int:n1>/<int:n2>')
def add(n1,n2):
    result = n1 + n2 
    return render_template('calculator.html', result=result)


@app.route('/sub/<int:n1>/<int:n2>')
def subtract(n1,n2):
    result = n1 -  n2 
    return render_template('calculator.html', result=result)

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')
