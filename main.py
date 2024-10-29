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
print(f""" \n
    Welcome back Mr/Ms {name}, this is a program to calculate your notes average \n 
    Please enter your 4 notes: \n """) 

noteOne =   int(input("    Please enter your firs note   : "))

noteTwo =   int(input("    Please enter your second  note: "))

noteThree = int(input("    Please enter your third  note : "))

noteFour =  int(input("    Please enter your fourth  note: "))

totalNotes = (noteOne + noteTwo + noteThree + noteFour)/4

print("    Your final average note is: ", totalnotes)


