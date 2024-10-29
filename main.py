#Pitágoras
#Escriba un programa que reciba como entrada las longitudes de los dos catetos a
# y b
# de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c
# del triangulo, dado por el teorema de Pitágoras: c2=a2+b2
#Ingrese cateto a: 7
#Ingrese cateto b: 5
#La hipotenusa es 8.6023252670426267
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
        Welcome back Mr/Ms {name}, this is a program for calculate the hipotenuse in a right triangle \n 
        Please enter your legs : \n """) 
    try :    
        
        legA =   float(input("        leg a : "))
        legB =   float(input("        leg a : "))

        hipotenuse = math.sqrt((legA**2) + (legB**2))

        print("The hipotenuse for the triangle is : ", hipotenuse)

        

        continueAsk = input( "\n    Do you want to calculate again? (yes/no): " ).strip().lower()
        
        if continueAsk != "yes" :
                print("    Thaks for using the program. Goodbye! \n ")
                break
    except :            
        continueAsk = input( "\n    Do you want to calculate again? (yes/no): " ).strip().lower()
        
        if continueAsk != "yes" :
                print("    Thaks for using the program. Goodbye! \n ")
                break

