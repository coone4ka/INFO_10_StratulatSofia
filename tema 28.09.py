import math
#1
a = 7
b = 7.7
c = True
d = "Salut"
print("Tipul variabilei a este", type(a))
print("Tipul variabilei b este", type(b))
print("Tipul variabilei c este", type(c))
print("Tipul variabilei d este", type(d))

#2
masa = input("Masa: ")
viteza = input("Viteza: ")
Ec = float(masa) * (pow(float(viteza), 2)) / 2
print("Energia cinetica este", Ec)

#3
nr = input("Numarul: ")
print("Valoarea absoluta al acestui numar este", abs(float(nr)))
print("Numarul rotunjit la cea mai mica valoare este", math.floor(float(nr)))
print("Numarul rotunjit la cea mai mare valoare este", math.ceil(float(nr)))
print("Numarul rotunjit este", round(float(nr)))

#4
a = float(input("Cateta a: "))
b = float(input("Cateta b: "))
ipotenuza = math.hypot(a,b)
unghi1 = math.degrees(math.atan2(a,b))
unghi2 = math.degrees(math.atan2(b,a))
print("Ipotenuza este", ipotenuza)
print("Primul unghi este", unghi1)
print("Al doilea unghi este", unghi2)