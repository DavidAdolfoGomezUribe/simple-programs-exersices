#Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo.
#El promedio del ramo se calcula con la siguiente formula.
#
#NC=(C1+C2+C3)/3
#NF=NC⋅0.7+NL⋅0.3
#Donde NC
# es el promedio de certámenes, NL
# el promedio de laboratorio y NF
# la nota final.
#Escriba un programa que pregunte al usuario las notas de los dos primeros certamen
#  y la nota de laboratorio, y muestre la nota que necesita el alumno para aprobar el
#  ramo con nota final 60.

#Ingrese nota certamen 1: 45
#Ingrese nota certamen 2: 55
#Ingrese nota laboratorio: 65
#Necesita nota 72 en el certamen 3


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
        Welcome back Mr/Ms {name}, this is a program for calculate the aprove note for the alumn: \n 
          """) 
    try :    
        
        c1 = float(input("        Please enter note of the first contest : "))
        c2 = float(input("        Please enter note of the second contest : "))
        laboratoryNote = float(input("        Please enter note of laboratory : "))

        finalNote = 60 

        c3 = (((finalNote-(laboratoryNote* 0.3))/0.7 )*3) + (- c1 - c2)

        c3r = round(c3,4)
       
        print(f"        The note por third contest in order to aprove with a final note of 60 is : ",c3r )

        continueAsk = input( "\n    Do you want to calculate again? (yes/no): " ).strip().lower()
        
        if continueAsk != "yes" :
                print("    Thaks for using the program. Goodbye! \n ")
                break
    except :            
        continueAsk = input( "\n    Do you want to calculate again? (yes/no): " ).strip().lower()
        
        if continueAsk != "yes" :
                print("    Thaks for using the program. Goodbye! \n ")
                break

