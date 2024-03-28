from math import radians, cos, sin, sqrt, atan2
import folium

def haversine(lat1, lon1, lat2, lon2):
    # Dünya'nın yarıçapı (km cinsinden)
    R = 6371.0

    # Koordinatların radyan cinsine dönüştürülmesi
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Enlem ve boylam farkı
    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1

    # Haversine formülü
    a = sin(delta_lat/2)**2 + cos(lat1) * cos(lat2) * sin(delta_lon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))

    distance = R * c
    return distance

# İstanbul ve Ankara'nın koordinatları
istanbul = [41.0082, 28.9784]
ankara = [39.9334, 32.8597]

# İki şehir arasındaki mesafe (km cinsinden)
distance_km = haversine(istanbul[0], istanbul[1], ankara[0], ankara[1])

# Haritanın oluşturulması
m = folium.Map(location=[(istanbul[0] + ankara[0]) / 2, (istanbul[1] + ankara[1]) / 2], zoom_start=6)

# İstanbul ve Ankara'ya işaretçilerin eklenmesi
folium.Marker(istanbul, popup='İstanbul').add_to(m)
folium.Marker(ankara, popup='Ankara').add_to(m)

# İki nokta arasında çizgi çekilmesi
folium.PolyLine(locations=[istanbul, ankara], color='blue', tooltip=f"Mesafe: {distance_km:.2f} km").add_to(m)

# Haritanın kaydedilmesi
m.save('istanbul_ankara_mesafe.html')

# HTML dosyasını tarayıcıda açabilirsiniz
