from flask import Flask, request, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

# Dummy model prediction function
def dummy_model_predict(features_scaled):
    # Random confidence for testing
    fake_confidence = np.random.uniform(0.4, 0.99)
    is_fake = np.random.choice([True, False])
    return is_fake, fake_confidence

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    username = request.form.get('username', '').strip()

    if not username:
        return render_template('index.html', error="Please enter a username!")

    try:
        # Dummy features matching original model
        features_df = pd.DataFrame([{
            'profile_pic': 0,
            'nums_length_username': 0,
            'fullname_words': 0,
            'nums_length_fullname': 0,
            'name_equals_username': 0,
            'description_length': 0,
            'external_url': 0,
            'private': 0,
            'num_posts': 0,
            'num_followers': 0,
            'num_following': 0
        }])

        # Use dummy model for testing
        is_fake, confidence = dummy_model_predict(features_df)

        return render_template(
            'result.html',
            username=username,
            is_fake=is_fake,
            confidence=round(confidence * 100, 2)
        )

    except Exception as e:
        return render_template('index.html', error=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)