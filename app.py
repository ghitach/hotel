from flask import Flask, request, jsonify
import random
from datetime import datetime, timedelta

app = Flask(__name__)

room_types = ["Standard", "Deluxe", "Suite", "Family", "Economy"]
hotel_types = ["Resort", "Boutique", "Business", "Luxury", "Budget", "Wellness"]
checkin_times = ["14:00", "15:00", "16:00"]
checkout_times = ["11:00", "12:00"]

@app.route("/", methods=["POST"])
def recommend():
    data = request.get_json()

    destination = data.get("Destination", "Paris")
    price = float(data.get("Price", 100))
    stars = int(data.get("HotelStars", 4))
    room_type = data.get("RoomType", "Standard")
    breakfast = data.get("BreakfastIncluded", False)
    parking = data.get("ParkingAvailable", False)
    activities = data.get("ActivitiesIncluded", False)
    guests = int(data.get("NumberOfGuest", 2))

    checkin_date = data.get("CheckInDate", "2025-04-15")
    checkout_date = data.get("CheckOutDate", "2025-04-17")

    hotel = {
        "Hotel Name": f"Hôtel Relax {destination}",
        "City": destination,
        "Room Type": room_type,
        "Stars": stars,
        "Check-In Date": checkin_date,
        "Check-Out Date": checkout_date,
        "Check-In Time": random.choice(checkin_times),
        "Check-Out Time": random.choice(checkout_times),
        "Price": round(price + random.uniform(-30, 30), 2),
        "Refundable": data.get("Refundable", True),
        "BreakfastIncluded": breakfast,
        "ParkingAvailable": parking,
        "ActivitiesIncluded": activities,
        "NumberOfGuest": guests,
        "Reservation URL": f"https://www.book-now.com/reservation/{random.randint(100000,999999)}"
    }

    return jsonify(hotel)

if __name__ == "__main__":
    app.run(debug=True)
