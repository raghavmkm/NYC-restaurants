from flask import Flask, request, jsonify
from flask_cors import CORS
from ml_models import *

app = Flask(__name__)
CORS(app)

@app.route('/compute', methods=['POST'])
def compute():
    data = request.get_json()
    input_value = data.get('input', '')

    model, scaler = model_2()
    pred = get_recommendations(input_value, model, scaler, 4)
    pred = pred["Name"].tolist()
    output_string = ""
    for i in pred:
        output_string += i + ", "
    output_string = output_string[:-2]
    
    # Perform a simple computation. For example, reverse the input string.
    result = input_value[::-1]
    
    return jsonify({'result': output_string})

if __name__ == '__main__':
    app.run(debug=True)