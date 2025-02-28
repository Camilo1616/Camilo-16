# vari1 = 100    
# vari2 = 200 
# 
# vari1 = vari2 + vari2
# 
# ancho = 1203
# alto = 1000
# area = ancho * alto
# 
# a =21
# b =30
# c =a + b
# 
#print ("c:", c)
#print ("area:", area)
# 
# d = 30 
# f = 30 
# g = "30"
# 
# x = a == b
# y = x and a == c
# 
#print ("x:", x)
#print ("d+f:", d+f) 
# 
# y = a == b and d < a or f == g 
#  
#print ("y:", y)
# 
# z = a*b == b*d and a*d < b*a
# 
#print ("z:", z) 
# 
# altura = 30
# peso = "80"
# 
# pesoNum = int(peso)
# pesoNumfloat = float(peso)
# 
# peso2= str (pesoNumfloat) 
#
#print (peso == peso2)
# 
# 

#Ejercicio 1
 


def is_float (value):
    try:
        float(value)
        return True
    except ValueError: 
        return False

inputusuario = input("Ingrese el primer numero: ")

isfloat = is_float (inputusuario)

if  not isfloat:
    inputusuario = input ("El valor ingresado no es numerico")

numero1=float(inputusuario)
numero2=float(input("ingresa el segundo numero: "))


suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print ("El resultado de la suma es: ", suma)
print ("El resultado de la resta es: ", resta)
print ("El resultado de la multiplicacion es: ", multiplicacion)
print ("El resultado de la division es: ", division)
