Bu kod ile coğrafi koordinatı verilen iki nokta arasındaki mesafeyi, dünyanın yuvarlaklığını da dikkate alarak hesaplamaya imkan veren "heversine" formülünün kullanımını sağlamaktadır. 
Bu formül özellikle görmeyerek atış imkanı sağlayan silah sistemlerinde mesafe verisinin elde edilmesi için kullanılan bir yaklaşımdır.
Formülde geçen parmetre ve dğeişkenlerin açıklamaları şu şekildedir;
delta_lat = iki nokta arasındaki enlem farkı ifade eder.
delta_lon = iki nokta arasındaki boylam farkı ifade eder.
R = dünaynın yarı çapı (6371 km olarak alınır)
lat1 ve lat2 = sırasıyla 1 nci noktanın enlemi ve 2nci noktanın enlem değerini "Radyan" cinsinden ifade eder.
c = bu değer "a" ara değedinden elde edilen trigonometrik bir değerdir.
Radyan = derece * pi/180 şeklinde formülize edilir. Python kütüphanesinde "radyans" fornkisyonu derece olarak verilen değeri radyan cinsine çevirir.


![haversine1](https://github.com/tlgbskn/GeographicalDistanceCalculator/assets/47304774/65933564-1aed-4958-906a-cc820efbfb12)
![haversine2](https://github.com/tlgbskn/GeographicalDistanceCalculator/assets/47304774/9eab58e7-1463-4fa9-9b29-69ca1ddacfe2)
