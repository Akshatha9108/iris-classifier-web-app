from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the model and label encoder
model = pickle.load(open('saved_model.sav', 'rb'))

@app.route('/')
def home():
    result = " "
    return render_template('index.html', result=result)

@app.route('/predict', methods=['POST'])
def predict():
    result = " "
    if request.method == 'POST':
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])

        # Make a prediction using your model
        features = [[sepal_length, sepal_width, petal_length, petal_width]]
        prediction = model.predict(features)

        # Assuming your model predicts a class label, you can use it in the result
        result = f"The predicted class is: {prediction[0]}"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
