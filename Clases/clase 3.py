ege = 18    
country = "USA"
userHasDNI = True

if ege >= 21 and country == "USA":  
    print("You can buy alcohol")
elif ege >= 18 and  country == "COL":
    print("You can buy alcohol")
else:
    userHasDNI = False
    print("You can't buy alcohol")


#ejercicio 2

#for student in range(1, 10):
 #   print(f"Estudiante {student}")

#ejercicio 3

#students = 0 

#while userHasDNI: 
#    students += 1
#    print(students)
#    if students == 10:
#        userHasDNI = False
#
#    if ege >= 21 and country == "USA":
#        print("You can buy alcohol")
#    elif ege >= 18 and  country == "COL":
#        print("You can buy alcohol")
#    else:
#        userHasDNI = False
#        print("You can't buy alcohol")

while userHasDNI:
 
    print ("HOLA 1") 
    if ege >= 21 and country == "USA":       
       print("You can buy alcohol")
       break
    elif ege >= 18 and  country == "COL":
       print("You can buy alcohol")
       break
    else:
       userHasDNI = False
       print("You can't buy alcohol")

       print ("HOLA 2")
