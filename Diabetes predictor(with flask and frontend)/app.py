# from flask import Flask, render_template, request
# import joblib
# import numpy as np

# app = Flask(__name__)
# model = joblib.load('model.sav')


# @app.route('/')
# def home():
#     return render_template('index.html')


# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         features = [float(x) for x in request.form.values() if x.strip()]

#         if not features:
#             raise ValueError(
#                 "Invalid input. Please provide values for all features.")

#         prediction = model.predict([features])
#         result = "DIABETES" if prediction[0] == 1 else "Negative"
#         message = f"Oops! You have DIABETES." if prediction[
#             0] == 1 else "Great news! You do not have DIABETES."
#         return render_template('index.html', prediction_text=message)

#     except Exception as e:
#         return render_template('index.html', prediction_text=f'Error: {str(e)}')


# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__, static_url_path='/static')
model = joblib.load('model.sav')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values() if x.strip()]

        if not features:
            raise ValueError(
                "Invalid input. Please provide values for all features.")

        prediction = model.predict([features])
        result = "DIABETES" if prediction[0] == 1 else "Negative"
        message = f"Oops! You have DIABETES." if prediction[
            0] == 1 else "Great news! You do not have DIABETES."

        gif_filename = 'diabetes.webp' if prediction[0] == 1 else 'no-diabetes.webp'

        return render_template('result.html', prediction_text=message, gif_filename=gif_filename)

    except Exception as e:
        return render_template('result.html', prediction_text=f'Error: {str(e)}')


if __name__ == '__main__':
    app.run(debug=True)
