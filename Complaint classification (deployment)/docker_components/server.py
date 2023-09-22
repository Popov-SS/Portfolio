from flask import Flask, request, jsonify
import pandas as pd
import dill
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def general():
    return "Welcome to prediction page."

@app.route('/predict', methods=['POST'])
def send_prediction():
    response = {'success':False}
    request_json = request.get_json()
    if request_json['text']:
        data = pd.DataFrame(request_json['text']).squeeze()
        if isinstance(data, str): #если отправили один документ
            data = [data]
        response['predict'] = lr_pipeline.predict(data).tolist()
        response['predict_proba'] = lr_pipeline.predict_proba(data).tolist()
        response['success'] = True
    return jsonify(response)

if __name__ == '__main__':
    with open('lr_pipeline.dill', 'rb') as myfile:
        lr_pipeline = dill.load(myfile)
    port = int(os.environ.get('PORT', 8180))
    app.run(host='0.0.0.0', debug=True, port=port)