funcionar=True
def funcionSuma ():
     numero1 = input ("Primer número: ")
     numero2 = input("Segundo número: ")

     numero1 = int ( numero1)
     numero2 = int ( numero2)
     suma = numero1 + numero2
     print ( suma)

def funcionResta ():
     numero1 = input ("Primer número: ")
     numero2 = input("Segundo número: ")

     numero1 = int ( numero1)
     numero2 = int ( numero2)
     resta = numero1 - numero2
     print ( resta)

def funcionMultiplicacion ():
    numero1 = input ("Primer número: ")
    numero2 = input("Segundo número: ")
    numero1 = int ( numero1)
    numero2 = int ( numero2)
    multiplicacion = numero1 * numero2
    print ( multiplicacion)
    
def funcionDivision ():
    numero1 = input ("Primer número: ")
    numero2 = input("Segundo número: ")

    numero1 = int ( numero1)
    numero2 = int ( numero2)
    division = numero1 / numero2
    print ( division)

def funcionHipotenusa ():
    cat1 = input ("Primer cateto")
    cat2 = input ("Segundo cateto")
     
while funcionar == True:
 print ( "Nuestras opciones:")
 print ( "1. Realizar una suma")
 print ( "2. Realizar una resta")
 print ( "3. Realizar una multiplicación")
 print ( "4. Realizar una división")
 print ( "5. Calcular el costado de un triángulo rectángulo")
 print ( "6. Terminar")

 pregunta = input ( "¿Qué quieres hacer?:")
 if pregunta == "1":
     funcionSuma ()
 elif pregunta == "2":
     funcionResta ()
 elif pregunta == "3":
     funcionMultiplicacion ()
 elif pregunta == "4":
     funcionDivision ()
 elif pregunta == "5":
     print ( "1. Calcular la hipotenusa")
     funcionHipotenusa ()
     print ( "2. Calcular un cateto")
 elif pregunta == "6":
     print ( "Adiós")
     funcionar=False
