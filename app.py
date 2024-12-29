from flask import Flask, request, render_template
import numpy as np
import pickle
import mysql.connector


app = Flask(__name__)

# Load the pre-trained model
model = pickle.load(open('model.pkl', 'rb'))


@app.route("/")
def home():
    return render_template("index.html")

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",       # Change to your MySQL host
        user="root",   # Your MySQL username
        password="Samarth@9538",  # Your MySQL password
        database="heart_disease"  # Database name
    )


@app.route("/predict", methods=["POST"])
@app.route("/predict", methods=["POST"])
def predict():
    # Extracting data from form
    float_features = [
        request.form['age'],
        request.form['sex'],
        request.form['chestPain'],
        request.form['bp'],
        request.form['cholesterol'],
        request.form['fbs'],
        request.form['ekg'],
        request.form['maxHr'],
        request.form['exerciseAngina'],
        request.form['stDepression'],
        request.form['slope'],
        request.form['vessels'],
        request.form['thallium']
    ]

    # Convert inputs to numpy array
    features = np.array([float_features], dtype=float)

    # Make prediction
    prediction = model.predict(features)
    prediction_text = "The person has Heart Disease" if prediction[0] == 1 else "The person does not have Heart Disease"


    # Save the result to the database
    try:
        db = get_db_connection()
        cursor = db.cursor()
        query = """
            INSERT INTO predictions (
                age, sex, chestPain, bp, cholesterol, fbs, ekg, maxHr, exerciseAngina, stDepression, slope, vessels, thallium, result
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (*float_features, prediction_text))
        db.commit()
        cursor.close()
        db.close()
    except Exception as e:
        print(f"Error: {e}")

    # Render the result on the result.html page
    return render_template("predict.html", prediction_text=prediction_text)





if __name__ == "__main__":
    app.run(debug=True)
