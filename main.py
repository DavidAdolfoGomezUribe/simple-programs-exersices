#Huevos a la copa
#Ejercicio sacado de [Lang09].
#Cuando un huevo es hervido en agua, las proteínas comienzan a coagularse cuando la temperatura sobrepasa un punto crítico. A medida que la temperatura aumenta, las reacciones se aceleran.
#En la clara, las proteínas comienzan a coagularse para temperaturas sobre 63°C, mientras que en la yema lo hacen para temperaturas sobre 70°C. Para hacer un huevo a la copa, la clara debe haber sido calentada lo suficiente para coagularse a más de 63°C, pero la yema no debe sobrepasar los 70°C para evitar obtener un huevo duro.
#El tiempo en segundos que toma al centro de la yema alcanzar Ty
#°C está dado por la fórmula:
#t=M2/3cρ1/3Kπ2(4π/3)2/3ln[0.76To−TwTy−Tw],
#donde M
#es la masa del huevo, ρ
#su densidad, c
#su capacidad calorífica específica y K
#su conductividad térmica. Algunos valores típicos son:
#
#
#M=47[g]
#para un huevo pequeño y M=67[g]
#para uno grande,
#ρ=1.038[gcm−3]
#c=3.7[Jg−1K−1]
#, y
#K=5.4⋅10−3[Wcm−1K−1
#].
#Tw
#es la temperatura de ebullición del agua y To
#la temperatura original del huevo antes de meterlo al agua, ambos en grados Celsius.

#Escriba un programa que reciba como entrada la temperatura original del huevo y
#  muestre como salida el tiempo en segundos que le toma alcanzar la temperatura máxima para prepararlo a la copa.



#i need to sleep man 

import math


print(f""" 
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝                                                        
                                """) 
name = input("    Hello, please enter your full name:  ")

while True:
   
    print(f""" \n
        Welcome back Mr/Ms {name}, this is a program for calculate the perfect temperature for an eggs in the cup: \n 
          """) 
    
        #DISCLAIMER : I put this inputs because non all eggs have the same mass and the wanted temperature oscilates between 63 and 70 and this oscilation its a lot more or less seconts to wait

    try :    
        tO = float(input("        Initial temperature: ")) 
        mass = float(input("        egg mass(between 47g and 67g): "))
        p = 1.038    #density of the egg
        c = 3.7      #especific heat of the egg
        k = 5.4e-3   #termic condictivity of the egg
        tW = 100     #boiling water temperature
        tY = float(input("        wanted egg temperature (between 63 and 70 greades for eggs in the cup): ")) 

        t=(  ((mass**(2/3))*c*(p**(1/3)))/( (k*(math.pi**2)) *  ((4*math.pi)/3)**(2/3)  )  )  *  (math.log(0.76 * ((tW -tO ) / (tY - tO)) ))
        
        tR = round(t, 2)

        print("    The time that you need to wait is : ", tR , "seconds")

    
        

        continueAsk = input( "\n    Do you want to calculate again? (yes/no): " ).strip().lower()
        
        if continueAsk != "yes" :
                print("    Thaks for using the program. Goodbye! \n ")
                break
    except :            
        continueAsk = input( "\n    Do you want to calculate again? (yes/no): " ).strip().lower()
        
        if continueAsk != "yes" :
                print("    Thaks for using the program. Goodbye! \n ")
                break

