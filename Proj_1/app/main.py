from flask import Flask,render_template,request,jsonify
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('hypothyroid_model.pkl','rb'))

"""
#Tell the terminal what application to run
export FLASK_APP=main.py
#Tell the terminal what application to run for windows
set FLASK_APP=main.py
#Run the application
flask run
"""

@app.route('/')
def hello():
    return "Hello World! Test run ok "

@app.route('/home')
def home():
    """
    required inputs
    ['age','TSH','T3','TT4','T4U','FTI']
    """
    return render_template('home.html')



@app.route('/predict', methods=['POST'])
def predict():

    # convert featuers entered into int

    int_featuers = [float(x) for x in request.form.values()]

    # convert the values to an array
    final_features = [np.array(int_featuers)]

    prediction = model.predict(final_features)

   

    if prediction == 0:
        answer = "Patient has Hypothyroid please analyse further"
    elif prediction == 1:
        answer = "Patient does not have hypothyroid thank you!"
    else:
        answer = "No predictions were made try again"

    print(answer)

    return render_template('predict.html', prediction_answer = answer)

if __name__ == '__main__':
    app.run(debug=True)
