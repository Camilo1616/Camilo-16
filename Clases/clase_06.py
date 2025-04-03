#    print (llaves, valores)




# tik tok 
while True:
    print ("ingrese un numero del 1 al 200", "ingrese el numero 2 para salir")
    numero = int(input())
    if  numero == 2:
        break    
    if numero < 200:
        for contador in range (numero):
            if contador % 15 == 0:
                print (contador, "fizzbuzz")
            elif contador % 7 == 0:
                print (contador, "good")
            elif contador % 5 == 0:
                print (contador ,"buzz")
            elif contador  % 3 == 0 :
                print (contador ,"fizz")
                break
    else :
        print ("numero superior a 200")    