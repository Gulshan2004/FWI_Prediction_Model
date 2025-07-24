import pickle
import numpy as np
import pandas as pd
from flask import Flask,request,jsonify,render_template
#here jsonify is used so that i can return my result in the form of json
#render_template will be useful in finding out the url of the html file
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app=application

#import ridge regressorand standard scaler pickle
ridge_model=pickle.load(open('models/ridge.pkl','rb'))
standard_scaler=pickle.load(open('models/scaler.pkl','rb'))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
#using GET i get the default information of the particular app
#using POST i post information i.e im sending some query and based on that i get result
def predict_datapoint():
    if request.method=="POST":
        Tempreature=float(request.form.get('Tempreature'))
        RH=float(request.form.get('RH'))
        Ws=float(request.form.get('Ws'))
        Rain=float(request.form.get('Rain'))
        FFMC=float(request.form.get('FFMC'))
        DMC=float(request.form.get('DMC'))
        ISI=float(request.form.get('ISI'))
        Classes=float(request.form.get('Classes'))
        Region=float(request.form.get('Region'))

        new_data_scaled=standard_scaler.transform([[Tempreature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result=ridge_model.predict(new_data_scaled)

        return render_template('home.html',results=result[0])


    else:
        return render_template('home.html')
    
if __name__ == '__main__':
    app.run(host="0.0.0.0")
