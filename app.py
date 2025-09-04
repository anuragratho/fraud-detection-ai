from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load saved model, scaler, and PCA
model = joblib.load('models/best_xgboost_model.pkl')
scaler = joblib.load('models/scaler.pkl')
pca = joblib.load('models/pca.pkl')

# Feature columns expected by the model
FEATURES = [
    'step', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest',
    'isFlaggedFraud', 'type_CASH_IN', 'type_CASH_OUT', 'type_DEBIT', 'type_PAYMENT', 'type_TRANSFER',
    'balance_change_org', 'balance_change_dest', 'amount_to_oldbalanceOrg_ratio', 'amount_to_oldbalanceDest_ratio'
]

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    proba = None
    if request.method == 'POST':
        # Get form data
        data = []
        for f in FEATURES:
            val = request.form.get(f, 0)
            try:
                val = float(val)
            except:
                val = 0
            data.append(val)
        arr = np.array(data).reshape(1, -1)
        arr_scaled = scaler.transform(arr)
        arr_pca = pca.transform(arr_scaled)
        pred = model.predict(arr_pca)[0]
        proba = model.predict_proba(arr_pca)[0][1]
        prediction = 'Fraudulent' if pred == 1 else 'Not Fraudulent'
    return render_template('index.html', features=FEATURES, prediction=prediction, proba=proba)

if __name__ == '__main__':
    app.run(debug=True)
