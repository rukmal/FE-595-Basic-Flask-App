from flask import Flask, render_template, request
from typing import Tuple

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculator', methods=['GET'])
def calculateLandingPage():
    return render_template('calculate.html')

@app.route('/add', methods=['POST'])
def add():
    n1, n2 = __getNumbers(request)
    return str(n1 + n2)

@app.route('/subtract', methods=['POST'])
def subtract():
    n1, n2 = __getNumbers(request)
    return str(n1 - n2)

@app.route('/divide', methods=['POST'])
def divide():
    n1, n2 = __getNumbers(request)
    return str(n1 / n2)

@app.route('/multiply', methods=['POST'])
def multiply():
    n1, n2 = __getNumbers(request)
    return str(n1 * n2)

def __getNumbers(request) -> Tuple[float, float]:
    numberOne = float(request.form.get('numberOne', 0.0))
    numberTwo = float(request.form.get('numberTwo', 0.0))
    return numberOne, numberTwo

if __name__ == '__main__':
    app.run(debug=True)
