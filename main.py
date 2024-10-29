#Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:

#Ingrese el radio: 5
#Perimetro: 31.4
#Área: 78.5

import math

print("\n")
print("Welcome to the program to calculate the area and the perimeter of a circle, please enter the following data: \n ")
print("(remember only put numbers) \n ")

try:
    radius = int(input("Radius: "))


    area = math.pi * (radius**2)

    perimeter = 2 * math.pi * radius


    print(f"""
        The area of the circule will be {area} and his perimeter will be {perimeter}
    """)

except:
    print("(remember only put numbers \n )") 