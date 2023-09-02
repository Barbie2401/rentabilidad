#Desafio 1 pregunta 2

#Programa que calcula utilidades 2

#Ingreso de variables
precio=int(input("\nInserte Precio de Suscripción: "))
usarios_normal=int(input("Ingrese Número de usuarios normales: "))
usuarios_premium=int(input("Ingrese Número de usuarios Premium: "))
gasto_total=int(input("Ingrese Gastos Totales: "))

## Calculo de utilidad
utilidades= (precio* usarios_normal) + ((precio*1.5)*usuarios_premium)-gasto_total


#Imprimir las utilidades
print(f"\nLas utilidades son {utilidades}")

