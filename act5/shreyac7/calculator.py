from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def calculate(num1, num2, operation):
    if operation == 'addition':
        return num1 + num2
    elif operation == 'subtraction':
        return num1 - num2
    elif operation == 'multiplication':
        return num1 * num2
    elif operation == 'division':
        if num2 == 0:
            return "Error: Division by zero"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_result():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        result = calculate(num1, num2, operation)
        return render_template('result.html', num1=num1, num2=num2, operation=operation, result=result)
    except ValueError:
        return "Error: Please enter valid numeric values."
    except KeyError:
        return "Error: Please fill out all fields."

if __name__ == '__main__':
    app.run(debug=True)

