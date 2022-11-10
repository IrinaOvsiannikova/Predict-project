import flask
import numpy as np
from flask import render_template

import tensorflow as tf
from tensorflow import keras


app = flask.Flask(__name__, template_folder= 'templates')

@app.route('/', methods = ['POST', 'GET'])

@app.route('/index', methods = ['POST', 'GET'])
def main():
    loaded_model = keras.models.load_model('linear_model')
    if flask.request.method =='GET':
        
        return render_template('main.html',resultb = False)

    if flask.request.method =='POST':
        
        		
        IW = float(flask.request.form['IW'])
        
        IF= float(flask.request.form['IF'])
        
        VW = float(flask.request.form['VW'])
        
        FP = float(flask.request.form['FP'])
        
        y_pred = loaded_model.predict([[IW, IF, VW, FP]])
        
        return render_template('main.html', result = y_pred, resultb = True)
		

if __name__ == '__main__':
    app.run()
    

