# app.py
from flask import Flask, redirect, render_template, request, url_for
from col import myzip
from numberss.simp import add,sub
from numberss.comp import ispal,sum_of_digits


app = Flask(__name__)

# Your routes and Flask setup here...

@app.route('/add/<int:num1>/<int:num2>')
def add_route(num1, num2):
    result = add(num1, num2)
    return render_template('add.html', num1=num1, num2=num2, result=result)

@app.route('/subtract/<int:num1>/<int:num2>')
def subtract_route(num1, num2):
    result = sub(num1, num2)
    return render_template('subtract.html', num1=num1, num2=num2, result=result)

@app.route('/sum_of_digits/<int:number>')
def sum_of_digits_route(number):
    result = sum_of_digits(number)
    return render_template('sum_of_digits.html', number=number, result=result)

@app.route('/ispal/<int:number>')
def ispal_route(number):
    is_palindrome = ispal(number)
    return render_template('ispal.html', number=number, is_palindrome=is_palindrome)

@app.route('/myzip')
def myzip_route():
    # Assuming you have two lists as query parameters, e.g., /myzip?list1=1,2,3&list2=a,b,c
    list1 = request.args.get('list1').split(',')
    list2 = request.args.get('list2').split(',')

    zipped_result = myzip(list1, list2)
    return render_template('myzip.html', zipped_result=zipped_result)



@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)

