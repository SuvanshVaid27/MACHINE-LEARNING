from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_suburb_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_type_names', methods=['GET'])
def get_type_names():
    response = jsonify({
        'types': util.get_type_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    type = request.form['type']
    suburb = request.form['suburb']
    rooms = int(request.form['rooms'])
    distance = int(request.form['distance'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(suburb, type, rooms, distance)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Melbourne House Price Prediction...")
    util.load_saved_artifacts()
    app.run()