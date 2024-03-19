from flask import Flask, jsonify, request

app = Flask(__name__)

transport = [
    {
      "id": 1,
      "name": "Expresso Oriente",
      "price_confort": "R$ 52.10",
      "price_econ": "R$ 21.50",
      "city": "São Paulo",
      "duration": "12h",
      "seat": "12C",
      "bed": "5A"
    },
    {
      "id": 2,
      "name": "Expresso Oriente",
      "price_confort": "R$ 194.20",
      "price_econ": "R$ 43.10",
      "city": "Belo Horizonte",
      "duration": "18h",
      "seat": "1A",
      "bed": "4B"
    },
    {
      "id": 3,
      "name": "Expresso Oriente",
      "price_confort": "R$ 74.50",
      "price_econ": "R$ 92.20",
      "city": "Curitiba",
      "duration": "18h",
      "seat": "22A",
      "bed": "7C"
    },
    {
      "id": 4,
      "name": "Expresso Oriente",
      "price_confort": "R$ 776.30",
      "price_econ": "R$ 383.60",
      "city": "Fortaleza",
      "duration": "48h",
      "seat": "9D",
      "bed": "4B"
    },
    {
      "id": 5,
      "name": "Expresso Oriente",
      "price_confort": "R$ 311.30",
      "price_econ": "R$ 270.95",
      "city": "Campinas",
      "duration": "12h",
      "seat": "16A",
      "bed": "7C"
    },
    {
      "id": 6,
      "name": "ZazTraz",
      "price_confort": "R$ 82.09",
      "price_econ": "R$ 71.19",
      "city": "São Paulo",
      "duration": "8h",
      "seat": "20B",
      "bed": "6A"
    },
    {
      "id": 7,
      "name": "ZazTraz",
      "price_confort": "R$ 213.20",
      "price_econ": "R$ 521.21",
      "city": "Belo Horizonte",
      "duration": "18h",
      "seat": "19C",
      "bed": "1B"
    },
    {
      "id": 8,
      "name": "ZazTraz",
      "price_confort": "R$ 226.50",
      "price_econ": "R$ 164.32",
      "city": "Curitiba",
      "duration": "18h",
      "seat": "14C",
      "bed": "3D"
    },
    {
      "id": 9,
      "name": "ZazTraz",
      "price_confort": "R$ 235.80",
      "price_econ": "R$ 75.80",
      "city": "Natal",
      "duration": "36h",
      "seat": "7D",
      "bed": "8A"
    },
    {
      "id": 10,
      "name": "ZazTraz",
      "price_confort": "R$ 190.50",
      "price_econ": "R$ 145.50",
      "city": "Manaus",
      "duration": "16h",
      "seat": "25D",
      "bed": "4C"
    },
    {
      "id": 11,
      "name": "ZazTraz",
      "price_confort": "R$ 42.35",
      "price_econ": "R$ 18.95",
      "city": "Campinas",
      "duration": "12h",
      "seat": "25A",
      "bed": "2B"
    },
    {
      "id": 12,
      "name": "Rapido Jacutinga",
      "price_confort": "R$ 318.25",
      "price_econ": "R$ 116.75",
      "city": "Salvador",
      "duration": "4h",
      "seat": "17D",
      "bed": "7C"
    },
    {
      "id": 13,
      "name": "Rapido Jacutinga",
      "price_confort": "R$ 214.87",
      "price_econ": "R$ 128.20",
      "city": "Campinas",
      "duration": "2h",
      "seat": "9A",
      "bed": "1A"
    },
    {
      "id": 14,
      "name": "Rapido Jacutinga",
      "price_confort": "R$ 315.72",
      "price_econ": "R$ 218.14",
      "city": "São Paulo",
      "duration": "2h",
      "seat": "20B",
      "bed": "4C"
    },
    {
      "id": 15,
      "name": "Rapido Jacutinga",
      "price_confort": "R$ 913.67",
      "price_econ": "R$ 412.14",
      "city": "Rio de Janiero",
      "duration": "3h",
      "seat": "20A",
      "bed": "2C"
    },
    {
      "id": 16,
      "name": "Rapido Jacutinga",
      "price_confort": "R$ 141.50",
      "price_econ": "R$ 102.20",
      "city": "Recife",
      "duration": "5h",
      "seat": "13D",
      "bed": "6B"
    }
]

@app.route('/trips', methods=['GET'])
def get_trips():
    # endpoint to return a list of transports with the necessary information for each one
    return jsonify(transport)

@app.route('/trips/<int:trip_id>', methods=['GET'])
def get_trips_by_id(trip_id):
    # endpoint to return a specific transport according to the id
    trip = next((trip for trip in transport if trip['id'] == trip_id), None)
    if trip:
        return jsonify(trip)
    else:
        return jsonify({'message': 'Trip not found'}), 404
    
@app.route('/best-prices', methods=['POST'])
def get_best_prices():
    # endpoint that returns the cheapest and fastest trip according to the chosen city
    destiny = request.json.get('destiny')
    if not destiny:
        return jsonify({'message':'Please, specify destination'}), 400
    
    fast_travel = min(transport, key=lambda x: x['duration'])
    economical_travel = min(transport, key=lambda x: x['price_econ'])

    return jsonify({
        'fast_travel': {
            'company_name': fast_travel['name'],
            'bed': fast_travel['bed'],
            'duration': fast_travel['duration'],
            'total_price': fast_travel['price_confort']
        },
        'economical_travel': {
            'company_name': economical_travel['name'],
            'bed': economical_travel['bed'],
            'duration': economical_travel['duration'],
            'total_price': economical_travel['price_econ']
        }
    })

if __name__ == '__main__':
    app.run(port = 5000, host = 'localhost',debug=True)