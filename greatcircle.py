import math

def deg2rad(deg):
    return deg * math.pi / 180;

def rad2deg(rad):
    return rad * 180 / math.pi

def distance(lat1, lon1, lat2, lon2):
    R = 6371.0 # km
    dLat = deg2rad(lat2 - lat1)
    dLon = deg2rad(lon2 - lon1)
    lat1 = deg2rad(lat1)
    lat2 = deg2rad(lat2)
    a = math.sin(dLat / 2.0) * math.sin(dLat / 2.0) + math.sin(dLon / 2.0) * math.sin(dLon / 2.0) * math.cos(lat1) * math.cos(lat2)
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
    d = R *c
    return d

