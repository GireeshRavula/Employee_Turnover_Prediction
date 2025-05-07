from flask import Flask,render_template,request
import numpy as np
import pickle
# import os
# os.chdir('/home/pranay532/mysite')
with open("Employee/Emp_ret1.pkl",'rb') as f:
    model = pickle.load(f)
#create an object instance
app = Flask(__name__)
@app.route('/pranay')
def check():
    return "Kudhah Fizz"
@app.route('/') #by default methods = ['GET']
def new():
    return render_template("endix.html")
@app.route('/predict',methods=['GET','POST'])
def predict():

    promoted = int(request.form['Promoted'])
    print(promoted)
    review = float(request.form['Enter_Reviews'])
    projects = int(request.form['Enter_no_of_Projects'])
    salary = int(request.form['Salary'])
    tenure = float(request.form['Tenure'])
    satisfaction = float(request.form['Satisfaction'])
    bonus = int(request.form['Bonus'])
    avg_hrs_month = float(request.form['Enter_Avg_hrs_month'])
    left = int(request.form['Left'])
    input_data = np.array([[promoted,review,projects,salary,tenure,satisfaction,bonus,avg_hrs_month,left]])
    print(input_data)
    predicted_price = model.predict(input_data)[0]

    if predicted_price == 1:
        prediction = 'Retention'
    else:
        prediction = 'Attrition'

    return render_template('endix.html', prediction = prediction)
app.run()