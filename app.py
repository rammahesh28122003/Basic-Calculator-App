from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def calculator():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']
    result = 0
    if operation == 'addition':
        result = num1 + num2
    elif operation == 'subtraction':
        result = num1 - num2
    elif operation == 'multiplication':
        result = num1 * num2
    elif operation == 'division':
        result = num1 / num2
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
