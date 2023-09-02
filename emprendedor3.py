#Desafio 1 pregunta 3

#Programa que calcula utilidades 3

#Ingreso de variables
precio=float(input("\nInserte Precio de Suscripción: "))
num_ususarios=float(input("Ingrese Número de usuarios: "))
gasto_total=float(input("Ingrese Gastos Totales: "))
utilidades_lastyear=float(input("Ingrese Utilidades del año anterior: "))

#Formula para calcular utilidades actuales
utilidades= (precio*num_ususarios-gasto_total)

#imprimir las utilidades del presente año
print(f"\nLas utilidades del presente año son: {utilidades}")

#Formula para mostrar la razón entre las utilidades actuales y las del año anterior con dos decimales.
razon_utilidades= round((utilidades/utilidades_lastyear),2)

#Imprimir razón entre las utilidades actuales y las del año anterior con dos decimales.
print(f"La razón entre utilidades del presente año y las del año anterior es: {razon_utilidades}\n")
