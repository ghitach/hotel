from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def recommend():
    data = request.get_json()
    destination = data.get("destination")
    margin_score = float(data.get("margin"))

    # Exemple de recommandations fictives
    recommendations = [
        {
            "hotel": "Hôtel Premium " + destination,
            "price": 250,
            "margin": margin_score + 0.1,
            "bonus": "petit-déjeuner inclus"
        },
        {
            "hotel": "Hôtel Éco " + destination,
            "price": 180,
            "margin": margin_score + 0.05,
            "bonus": "annulation gratuite"
        }
    ]
    return jsonify(recommendations)
