from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle

app = Flask(__name__)
model = pickle.load(open("D:\\EDA\\Crop_Recommendation_System\\Crop_Recommendation_System.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("WebApp.html")


@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":            
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])
        n = float(request.form['n'])
        p = float(request.form['p'])
        k = float(request.form['k'])
        
        prediction = model.predict([[temperature, humidity, ph, rainfall, n, p, k]])
        output = prediction[0]
        output = output[output.find('_') + 1 : ].capitalize()

        return render_template('WebApp.html', prediction_text=f'{output} will grow.')

    return render_template("WebApp.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)