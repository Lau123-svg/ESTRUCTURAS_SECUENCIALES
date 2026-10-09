print("Convertir Celsius a Fahrenheit")
print("-" * 40)
ciudad=input("nombre de la ciudad: ")
celsius = float(input("Grados Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print("Ciudad:", ciudad)
print("Fahrenheit:", round(fahrenheit, 2))