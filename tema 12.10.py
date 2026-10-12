n = int(input("Introdu numarul de zile: "))
ore = n * 24
minute = ore * 60
print(ore, "ore")
print(minute, "minute")


m1 = float(input("Introdu prima masa in kg: "))
m2 = float(input("Introdu a doua masa in kg: "))
total = m1 + m2
grame = total * 1000
print(f"Masa totala: {total:.2f} kg")
print(f"Masa totala: {grame:.2f} g")


distanta = float(input("Introdu distanta in km: "))
consum = float(input("Introdu consumul in L/100 km: "))
combustibil = distanta * consum / 100
print(f"Combustibil necesar: {combustibil:.2f} L")


n = int(input("Introdu numarul de minute: "))
ore = n // 60
minute = n % 60
print(ore, "ore si", minute, "minute")