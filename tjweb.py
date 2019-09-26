from flask import Flask, Response, request, jsonify
from TJSpliteWord import TJSpliteWord
from TJPredict import TJPredict

app = Flask(__name__)
tjspliteword = TJSpliteWord()
tjpredict = TJPredict()


@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_data()
    result0 = tjspliteword.Spliteword(data.decode("utf-8")) 
    result1 = tjpredict.Predict(result0) 

    response = jsonify(result1)

    return response

@app.route('/wordcloud', methods=['POST'])
def wordcloud():

    data = request.get_data()
    cdict = tjspliteword.WordCount(data.decode("utf-8")) 
    result = tjspliteword.WordCloud(cdict) 

    return result

    
@app.route('/spliteword', methods=['POST'])
def spliteword():

    data = request.get_data()
    result = tjspliteword.Spliteword(data.decode("utf-8")) 

    response = jsonify(result)

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 
