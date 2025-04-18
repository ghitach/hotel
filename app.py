from flask import Flask, request, jsonify
import random
from datetime import datetime, timedelta

app = Flask(__name__)

room_types = ["Standard", "Deluxe", "Suite", "Family", "Economy"]
hotel_types = ["Resort", "Boutique", "Business", "Luxury", "Budget", "Wellness"]
checkin_times = ["14:00", "15:00", "16:00"]
checkout_times = ["11:00", "12:00"]


def random_date(base_date_str, variation_days=3):
    base_date = datetime.strptime(base_date_str, "%Y-%m-%d")
    delta = timedelta(days=random.randint(-variation_days, variation_days))
    return (base_date + delta).strftime("%Y-%m-%d")


@app.route("/", methods=["POST"])
def recommend():
    data = request.get_json()

    # Données extraites dynamiquement de la requête
    base_city = data.get("Destination")
    base_checkin = data.get("CheckInDate")
    base_checkout = data.get("CheckOutDate")
    base_price = float(data.get("Price"))
    base_stars = int(data.get("HotelStars"))
    base_room_type = data.get("RoomType")
    base_refundable = bool(data.get("Refundable"))
    base_breakfast = bool(data.get("BreakfastIncluded"))
    base_parking = bool(data.get("ParkingAvailable"))
    base_activities = bool(data.get("ActivitiesIncluded"))
    base_guests = int(data.get("NumberOfGuest"))

    # Générer un seul hôtel correspondant aux critères
    hotel = {
        "Hotel Name": f"Hôtel {random.choice(['Vista', 'Relax', 'Panorama', 'Zen'])} {base_city}",
        "City": base_city,
        "Room Type": base_room_type,
        "Check-In Date": random_date(base_checkin),
        "Check-Out Date": random_date(base_checkout),
        "Check-In Time": random.choice(checkin_times),
        "Check-Out Time": random.choice(checkout_times),
        "Price": round(base_price + random.uniform(-25, 25), 2),
        "Stars": base_stars,
        "Refundable": base_refundable,
        "BreakfastIncluded": base_breakfast,
        "ParkingAvailable": base_parking,
        "ActivitiesIncluded": base_activities,
        "NumberOfGuest": base_guests,
        "Reservation URL": f"https://www.book-now.com/reservation/{random.randint(100000, 999999)}"
    }

    return jsonify(hotel)


if __name__ == "__main__":
    app.run(debug=True)
