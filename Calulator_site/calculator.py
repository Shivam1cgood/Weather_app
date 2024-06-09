from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/calculator")
def Calulator_page():
    return render_template('index2.html')

@app.route("/math" , methods = ['POST'])
def calculator_test():
    ops = request.form['operation']
    first_num = int(request.form['num1'])
    second_num = int(request.form['num2'])

    if ops == 'add':
        r = first_num + second_num
        return f"Addition of {first_num} and {second_num} is {r}"
    
    elif ops == 'subtract':
        r = first_num - second_num
        return f"Subtraction of {first_num} and {second_num} is {r}"
    
    elif ops == 'multiply':
        r = first_num * second_num
        return f"Multiplication of {first_num} and {second_num} is {r}"
    
    elif ops == 'divide':
        r = first_num / second_num
        return f"Division of {first_num} by {second_num} is {r}"
    

if __name__ == '__main__':
    app.run(host = "0.0.0.0", )
    
