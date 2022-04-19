"""Programa 7
verificar si dos numeros son diferentes"""

print("---------------------------------")
print("--------NUMEROS DIFERENTES-------")
print("---------------------------------")

#input
x = int(input("Digite el valor de x: "))
y = int(input("Digite el valor de y: "))

# procesing
if x != y:
    msj = "SOn diferentes"
else:
    msj = "SOn iguales"

# output
print("Los numeros " + msj)