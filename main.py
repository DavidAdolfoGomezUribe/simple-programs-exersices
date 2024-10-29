#Escriba un programa que convierta de centímetros a pulgadas. 
#Una pulgada es igual a 2.54 centímetros.
#
#Ingrese longitud: 45
#45 cm = 17.7165 in
#Ingrese longitud: 13
#13 cm = 5.1181 in


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
        Welcome back Mr/Ms {name}, this is a program for convert centemiters to inch \n 
        Please enter your centemiters: \n """) 
    try :    

        centemiters =   float(input("        "))

        totalInch = (centemiters / 2.54)

        print("    Your inch is: ", totalInch, " in")

        continueAsk = input( "\n    Do you want to calculate again? (yes/no): " ).strip().lower()
        
        if continueAsk != "yes" :
                print("    Thaks for using the program. Goodbye!")
                break
    except :            
        continueAsk = input( "\n    Do you want to calculate again? (yes/no): " ).strip().lower()
        
        if continueAsk != "yes" :
                print("    Thaks for using the program. Goodbye!")
                break

