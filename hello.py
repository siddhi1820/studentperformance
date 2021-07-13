from flask import Flask
from flask import render_template,request,jsonify
from flask import  redirect,url_for
import joblib


import numpy as np
hello=Flask(__name__)
model=joblib.load('hour')
@hello.route('/')
def home():
    return  render_template('content.html')
@hello.route('/predict',methods=['POST'])
def predict():
       features=[int(x) for x in request.form.values()]
       final=[np.array(features)]
       prediction=model.predict(final)
       output=round(prediction[0],2)
       return render_template('content.html',prediction_text='marks of student should be {}'.format(output)+'%')



if __name__=='__main__':
    hello.run(port=1000)
