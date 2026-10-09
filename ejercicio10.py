#Calcular el consumo de gasolina por km
print("Calcular el consumo de gasolina por km")
print("-" * 40)
km_recorridos = float(input("Kilómetros recorridos: "))
galones_usados = float(input("Galones usados: "))
consumo = km_recorridos / galones_usados
print("Consumo (km por galón):", round(consumo, 2))
