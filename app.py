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

    # Suppression des valeurs par défaut : on suppose que tout est envoyé depuis UiPath ✅
    destination = data["Destination"]
    checkin_base = data["CheckInDate"]
    checkout_base = data["CheckOutDate"]
    price = float(data["Price"])
    margin = float(data["MarginScore"])
    stars = int(data["HotelStars"])
    room_type = data["RoomType"]
    refundable = data["Refundable"]
    breakfast = data["BreakfastIncluded"]
    parking = data["ParkingAvailable"]
    activities = data["ActivitiesIcluded"]
    guests = data["NumberOfGuest"]
    booking_channel = data["BookingChannel"]

    hotel_type = "Business" if "agency" in booking_channel.lower() else random.choice(hotel_types)

    checkin = random_date(checkin_base)
    checkout = random_date(checkout_base)
    if checkin > checkout:
        checkin, checkout = checkout, checkin

    result = {
        "Hotel Type": hotel_type,
        "Hotel Name": f"Hôtel {random.choice(['Premium', 'Zen', 'Relax', 'Élite'])} {destination}",
        "Room Type": room_type,
        "Check-In Date": checkin,
        "Check-Out Date": checkout,
        "Check-In Time": random.choice(checkin_times),
        "Check-Out Time": random.choice(checkout_times),
        "Price": round(price + random.uniform(-30, 30), 2),
        "City": destination,
        "Stars": min(max(stars + random.choice([-1, 0, 1]), 2), 5),
        "Airport Transfer": random.randint(0, 1),
        "Refundable": refundable,
        "BreakfastIncluded": breakfast,
        "ParkingAvailable": parking,
        "ActivitiesIncluded": activities,
        "NumberOfGuest": guests,
        "Reservation URL": f"https://www.book-now.com/reservation/{random.randint(100000,999999)}"
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
