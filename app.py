from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route("/", methods=["POST"])
def recommend():
    data = request.get_json()
    destination = data.get("destination")
    margin = float(data.get("margin", 0))

    # Simuler recommandations
    hotels = [
        {"hotel": f"Hôtel Premium {destination}", "price": 250, "margin": margin + 0.1},
        {"hotel": f"Hôtel Zen {destination}", "price": 210, "margin": margin + 0.05}
    ]

    return jsonify(hotels)
