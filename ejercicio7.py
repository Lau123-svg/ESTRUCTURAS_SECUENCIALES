#Convertir minutos a horas
minutos = int(input("Minutos: "))
horas = minutos // 60
minutos_restantes = minutos % 60
print(f"{horas} horas y {minutos_restantes} minutos")
