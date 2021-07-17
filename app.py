import numpy as np
from flask import Flask,request,render_template,url_for
import pickle
import pandas as pd

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features=[x for x in request.form.values()]
    int_features.remove(int_features[2])
    int_array=np.array([[int(i) for i in int_features]])

    ohe_opener = open('column_transformer2.pkl',"rb")
    ohe = pickle.load(ohe_opener)
    int_encoded=ohe.transform(int_array)
    int_dataframe=pd.DataFrame.sparse.from_spmatrix(int_encoded)

    fs_opener = open('feature_selector2.pkl',"rb")
    feature_selector = pickle.load(fs_opener)
    mask=feature_selector.get_support(indices=True)
    input_data_fs = int_dataframe.iloc[:,mask]
    input_data_fs_np=input_data_fs.values

    model_opener = open('model2.pkl',"rb")
    model = pickle.load(model_opener)
    output=model.predict(input_data_fs_np)

    prediction=float(output)

    #final_features=[np.array(int_features)]
    final_features=round(prediction,2)
    return render_template('index.html',prediction_text=final_features)

if __name__=="__main__":
    app.run(debug=True)