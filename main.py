#Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:
#
#Primera nota: 55
#Segunda nota: 71
#Tercera nota: 46
#Cuarta nota: 87
#El promedio es: 64.7

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
        Welcome back Mr/Ms {name}, this is a program to calculate your notes average \n 
        Please enter your 4 notes: \n """) 
    try :    

        noteOne =   float(input("    Please enter your firs note   : "))

        noteTwo =   float(input("    Please enter your second  note: "))

        noteThree = float(input("    Please enter your third  note : "))

        noteFour =  float(input("    Please enter your fourth  note: "))

        totalNotes = (noteOne + noteTwo + noteThree + noteFour)/4

        print("    Your final average note is: ", totalNotes)

        continueAsk = input( "\n    Do you want to calculate again? (yes/no): " ).strip().lower()
        
        if continueAsk != "yes" :
                print("    Thaks for using the program. Goodbye!")
                break
    except :            
        continueAsk = input( "\n    Do you want to calculate again? (yes/no): " ).strip().lower()
        
        if continueAsk != "yes" :
                print("    Thaks for using the program. Goodbye!")
                break

