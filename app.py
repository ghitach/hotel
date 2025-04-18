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

    base_checkin = data.get("CheckInDate", "2025-08-10")
    base_checkout = data.get("CheckOutDate", "2025-08-15")
    base_city = data.get("Destination", "Paris")
    base_price = float(data.get("Price", 100))
    base_stars = int(data.get("HotelStars", 4))
    base_room_type = data.get("RoomType", "Standard")
    base_refundable = int(data.get("Refundable", 1))
    base_breakfast = int(data.get("BreakfastIncluded", 1))
    base_parking = int(data.get("ParkingAvailable", 0))
    base_activities = int(data.get("ActivitiesIcluded", 0))
    base_guests = int(data.get("NumberOfGuest", 2))

    # booking channel influence hotel type ?
    booking_channel = data.get("BookingChannel", "Online")
    if "agency" in booking_channel.lower():
        hotel_type = "Business"
    elif "direct" in booking_channel.lower():
        hotel_type = "Boutique"
    else:
        hotel_type = random.choice(hotel_types)

    results = []
    for _ in range(random.randint(5, 20)):
        checkin = random_date(base_checkin)
        checkout = random_date(base_checkout)
        if checkin > checkout:
            checkin, checkout = checkout, checkin

        result = {
            "Hotel Type": hotel_type,
            "Room Type": random.choice(room_types),
            "Check-In Date": checkin,
            "Check-Out Date": checkout,
            "Check-In Time": random.choice(checkin_times),
            "Check-Out Time": random.choice(checkout_times),
            "Price": round(base_price + random.uniform(-30, 30), 2),
            "City": base_city,
            "Stars": min(max(base_stars + random.choice([-1, 0, 1]), 2), 5),
            "Airport Transfer": random.randint(0, 1),
            "Refundable": base_refundable,
            "BreakfastIncluded": base_breakfast,
            "ParkingAvailable": base_parking,
            "ActivitiesIncluded": base_activities,
            "NumberOfGuest": base_guests,
            "Reservation URL": f"https://www.book-now.com/reservation/{random.randint(100000,999999)}"
        }
        results.append(result)

    return jsonify(results)
