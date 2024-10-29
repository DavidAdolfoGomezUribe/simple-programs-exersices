#Escriba un programa que pida al usuario un entero de tres dígitos,
#y entregue el número con los dígitos en orden inverso:
#Ingrese numero: 345
#543
#Ingrese numero: 241
#142



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
        Welcome back Mr/Ms {name}, this is a program for invert the order of your digits \n 
        Please enter your digits: \n """) 
    try :    
        
        digits =   input("        ")
        
        if digits.isdigit() : #super util el isdigit(), tambien puede usarse isdecimal()
        

            invertDigits = digits[::-1] #el slicinng permite crear una subcadena de la cadena y el -1 para invertirla
        
            print("        Your invert digits is: ", invertDigits)

        else :  

            print("        Enter valid digits (nubers only)")

        continueAsk = input( "\n    Do you want to invert again? (yes/no): " ).strip().lower()
        
        if continueAsk != "yes" :
                print("    Thaks for using the program. Goodbye! \n ")
                break
    except :            
        continueAsk = input( "\n    Do you want to invert again? (yes/no): " ).strip().lower()
        
        if continueAsk != "yes" :
                print("    Thaks for using the program. Goodbye! \n ")
                break

