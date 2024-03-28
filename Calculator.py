from math import radians, cos, sin, sqrt, atan2

# Dünya'nın yarıçapı (km cinsinden)
R = 6371.0

# İlk noktanın koordinatları (Örneğin, İstanbul)
lat1 = radians(41.0082)
lon1 = radians(28.9784)

# İkinci noktanın koordinatları (Örneğin, Ankara)
lat2 = radians(39.9334)
lon2 = radians(32.8597)

# Enlem ve boylam farklarının hesaplanması
delta_lat = lat2 - lat1
delta_lon = lon2 - lon1

# Haversine formülü
a = sin(delta_lat / 2)**2 + cos(lat1) * cos(lat2) * sin(delta_lon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

# İki nokta arasındaki mesafe
distance = R * c
    
print(f"İstanbul ile Ankara arasındaki mesafe: {distance} kilometredir.")
