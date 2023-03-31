from flask import Flask, render_template, request
# import numpy as np
import joblib
import pandas as pd
app = Flask(__name__, static_url_path='/static')
@app.route('/', methods=['GET','POST'])
def home():
    return render_template('index.html')
@app.route('/masterprediksi', methods=['GET','POST']) 
def masterprediksi():
    if request.method == 'GET':
        print(request.form)
        return render_template('masterprediksi.html')
    elif request.method == 'POST':
         # Get values through input bars
        model  = joblib.load("model_development/model_predict_home_price.pkl")
        income = request.form.get("income")
        age = request.form.get("age")
        if float(age) < 2.6:
            age = str(2.6)
        bathroom = request.form.get("bathroom")
        if int(bathroom) < 3:
            bathroom =  str(3)
        bedroom = request.form.get("bedroom")
        if int(bedroom) < 2:
            bedroom = str(2)
        population = request.form.get("population")
        
        # Put inputs to dataframe
        X = pd.DataFrame([[income, age, bathroom, bedroom, population]], columns = ["income", "age", "bathroom", "bedroom", "population"])
     
        # Get prediction
        predict_price = round(model.predict(X)[0],2)      
    else:
        predict_price = ""    
    return render_template("masterprediksi.html", output = predict_price)


@app.route('/masterprediksiusia', methods=['GET','POST']) 
def masterprediksiusia():
    if request.method == 'GET':
        print(request.form)
        return render_template('masterprediksiusia.html')
    elif request.method == 'POST':
         # Get values through input bars
        model2 = joblib.load("model_development/model_predict_home_age.pkl")
        income = request.form.get("income")
        bathroom = request.form.get("bathroom")
        if int(bathroom) < 3:
            bathroom =  str(3)
        bedroom = request.form.get("bedroom")
        if int(bedroom) < 2:
            bedroom = str(2)
        population = request.form.get("population")
        price = request.form.get("price")
        
        # Put inputs to dataframe
        X = pd.DataFrame([[income, bathroom, bedroom, population, price]], columns = ["income", "bathroom", "bedroom", "population", "price"])
        
        # Get prediction
        predict_age = round(model2.predict(X)[0])      
    else:
        predict_age = ""   
    return render_template("masterprediksiusia.html", output_age = predict_age)

@app.route('/about', methods=['GET','POST']) 
def about():
    return render_template('about.html')

@app.route('/pemilik', methods=['GET','POST']) 
def pemilik():
    return render_template('pemilik.html')

@app.route('/pemiliksingle', methods=['GET','POST']) 
def pemiliksingle():
    return render_template('pemiliksingle.html')

if __name__ == "__main__":
    app.run()