#Desafio 1 pregunta 1

#Programa que calcula utilidades

#Ingreso de variables
precio=int(input("\nInserte Precio de Suscripción: "))
num_ususarios=int(input("Ingrese Número de usuarios: "))
gasto_total=int(input("Ingrese Gastos Totales: "))

#Formula para calcular utilidades
utilidades= (precio*num_ususarios-gasto_total)

#imprimir las utilidades
print(f"\nLas utilidades son {utilidades}")

