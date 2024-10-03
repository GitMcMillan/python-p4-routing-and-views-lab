#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Route for the base URL '/'
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Route to print the string
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter) # Print the string in the terminal
    return parameter  # Display the string in the browser


# Route to display numbers in range
@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = '\n'.join(str(i) for i in range(0, parameter)) + '\n'  # Append newline at the end
    return numbers  # Return plain text with newlines

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == "+":
        return str(num1 + num2)
    elif operation == "-":
        return str(num1 - num2)
    elif operation == "*":
        return str(num1 * num2)
    elif operation == "div":
        return str(num1 / num2)
    elif operation == "%":
        return str(num1 % num2)
    else:
        return f'<p>Invalid operation: {operation}'
    
    
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
