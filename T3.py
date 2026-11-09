import random
import math

a = float(input("ingrese el valor de a (elipse): "))
b = float(input("ingrese el valor de b (elipse): "))
c = float(input("ingrese el valor de c (hiperboal): "))
d = float(input("ingrese el valor de d (hiperbola): "))
cant = int(input("ingrese la cant de puntos aleatorios: "))

if a <= 0 or b <= 0 or c <= 0 or d <= 0 or cant <= 0:
    print("todos los valores deben ser mayores que cero.")
else:
    pnt_elipse = 0
    pnt_inter = 0

    for i in range(cant):
        x = random.uniform(-a, a)
        y = random.uniform(-b, b)

        dnt_elipse = (x**2 / a**2) + (y**2 / b**2) <= 1

        dnt_hiperbola = (x**2 / c**2) - (y**2 / d**2) >= 1

        if dnt_elipse:
            pnt_elipse += 1

            if dnt_hiperbola:
                pnt_inter += 1

    a_elipse = math.pi * a * b

    if pnt_elipse > 0:
        a_inter = a_elipse * (
            pnt_inter / pnt_elipse
        )
    else:
        a_inter = 0

    print("\n--- RESULTADOS ---")
    print("Puntos generados:", cant)
    print("Puntos dentro de la elipse:", pnt_elipse)
    print("Puntos en la interseccion:", pnt_inter)
    print("Area de la elipse:", round(a_elipse, 6))
    print("Area aproximada de al interseccion:",
    round(a_inter, 6))
