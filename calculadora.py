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

def funcionecuacion ():
    numero1 = input ("Primer número: ")
    numero2 = input("Segundo número: ")
    numero3 = input("Tercer número: ")

    numero1 = int ( numero1)
    numero2 = int ( numero2)
    numero3 = int ( numero3)
    ecuacion = (numero1 + numero2) * numero3
    print ( ecuacion)

while funcionar == True:
 print ( "Nuestras opciones:")
 print ( "1. Realizar una suma")
 print ( "2. Realizar una resta")
 print ( "3. Realizar una multiplicación")
 print ( "4. Realizar una división")
 print ( "5. Realizar una ecuación")
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
     funcionecuacion ()
 elif pregunta == "6":
     print ( "Adiós")
     funcionar=False