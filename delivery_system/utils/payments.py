def calculate_earnings(order_count):
    if order_count > 50:
        return 500 + order_count * 42
    elif order_count > 25:
        return 500 + order_count * 35
    else:
        return 500

def check_compliance(total_distance_km, total_time_minutes):
    return total_distance_km <= 100 and total_time_minutes <= 600


