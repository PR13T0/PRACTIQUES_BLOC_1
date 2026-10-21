funcionar=True
def funcionSuma ():
     numero1 = input ("Introduzca el primer número: ")
     numero2 = input("Introduzca el segundo número: ")

     numero1 = int ( numero1)
     numero2 = int ( numero2)
     suma = numero1 + numero2
     print ( "El resultado de la suma es: ", suma)

def funcionResta ():
     numero1 = input ("Introduzca el primer número: ")
     numero2 = input("Introduzca el segundo número: ")

     numero1 = int ( numero1)
     numero2 = int ( numero2)
     resta = numero1 - numero2
     print ( "El resultado de la resta es: ", resta)

def funcionMultiplicacion ():
    numero1 = input ("Introduzca el primer número: ")
    numero2 = input("Introduzca el segundo número: ")
    numero1 = int ( numero1)
    numero2 = int ( numero2)
    multiplicacion = numero1 * numero2
    print ( "El resultado de la multiplicación es: ", multiplicacion)
    
def funcionDivision ():
    numero1 = input ("Introduzca el primer número: ")
    numero2 = input("Introduzca el segundo número: ")

    numero1 = int ( numero1)
    numero2 = int ( numero2)
    division = numero1 / numero2
    print ( "El resultado de la división es: ", division)

def funcionHipotenusa ():
    cat1 = input ("Introduzca el primer cateto: ")
    cat2 = input ("Introduzca el segundo cateto: ")

    cat1 = int ( cat1)
    cat2 = int ( cat2)
    hipotenusa = (cat1**2 + cat2**2)**0.5
    print ( "La hipotenusa es: ", hipotenusa)

def funcioncateto ():
        hipo = input ("Introduzca la hipotenusa: ")
        cat = input ("Introduzca el cateto conocido: ")

        hipo = int ( hipo)
        cat = int ( cat)
        cat2 = (hipo**2 - cat**2)**0.5
        print ( "El segundo cateto es: ", cat2)

def funcionAreaCirculo ():
    r = input ("Introduzca el radio del círculo: ")
    r = int (r)
    area = 3.1416 * r**2
    print ( "El área del círculo es: ", area)

def funcionAreaTriangulo ():
    base = input ("Introduzca la base del triángulo: ")
    altura = input ("Introduzca la altura del triángulo: ")

    base = int (base)
    altura = int (altura)
    area = (base * altura) / 2
    print ( "El área del triángulo es: ", area)

def funcionAreaRectangulo ():
    base = input ("Introduzca la base del rectángulo: ")
    altura = input ("Introduzca la altura del rectángulo: ")

    base = int (base)
    altura = int (altura)
    area = base * altura
    print ( "El área del rectángulo es: ", area)

def funcionAreaCuadrado ():
    lado1 = input ("Introduzca el primer lado del cuadrado: ")
    lado2 = input ("Introduzca el segundo lado del cuadrado: ")
    lado1 = int (lado1)
    lado2 = int (lado2)
    area = lado1 * lado2
    print ( "El área del cuadrado es: ", area)

while funcionar == True:
 print ( "Nuestras opciones:")
 print ( "1. Realizar una suma")
 print ( "2. Realizar una resta")
 print ( "3. Realizar una multiplicación")
 print ( "4. Realizar una división")
 print ( "5. Calcular el costado de un triángulo rectángulo")
 print ( "6. Calcular el área de figuras geométricas")
 print ( "7. Terminar")

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
     print ( "2. Calcular un cateto")
     print ( "3. Atrás")
     pregunta2 = input ( "¿Qué quieres hacer?:")
     if pregunta2 == "1":
         funcionHipotenusa ()
     elif pregunta2 == "2":
         funcioncateto ()
     elif pregunta2 == "3":
            pass
 elif pregunta == "6":
     print ( "1. Calcular el área de un círculo")
     print ( "2. Calcular el área de un triángulo")
     print ( "3. Calcular el área de un rectángulo")
     print ( "4. Calcular el área de un cuadrado")
     print ( "5. Atrás")
     pregunta2 = input ( "¿Qué quieres hacer?:")
     if pregunta2 == "1":
         funcionAreaCirculo ()
     elif pregunta2 == "2":
         funcionAreaTriangulo ()
     elif pregunta2 == "3":
         funcionAreaRectangulo ()
     elif pregunta2 == "4":
         funcionAreaCuadrado ()
     elif pregunta2 == "5":
         pass
 elif pregunta == "7":
     print ( "Adiós")
     funcionar=False
