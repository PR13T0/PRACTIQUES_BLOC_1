funcionar = True
def funcionpartida ():
    print ( "1. Empezar")
    print ( "2. Atrás")
    juego = input ( "Instrucciones: usted tendrá que pensar un número del 1 al 10 y tendrá que decir si su número es mayor o menor al número que yo le pregunte. El juego terminará cuando yo consiga adivinarlo.")
    if juego == "1":
        pregunta1 = input ( "¿El número que pensaste es mayor que 5?")
        print ( "1. Sí")
        print ( "2. No")
        if pregunta1 == "1":
            pregunta2 = input ( "¿El número que pensaste es mayor que 7?")
            print ( "1. Sí")
            print ( "2. No")
            if pregunta2 == "1":
                pregunta3 = input ( "¿El número que pensaste es mayor que 9?")
                print ( "1. Sí")
                print ( "2. No")
                if pregunta3 == "1":
                    print ( "El número que pensaste es 10")
                elif pregunta3 == "2":
                    pregunta4 = input ( "¿El número que pensaste es mayor que 8?")
                    print ( "1. Sí")
                    print ( "2. No")   
                    if pregunta4 == "1":
                        print ( "El número que pensaste es 9")
                    elif pregunta4 == "2":
                        print ( "El número que pensaste es 8")
            elif pregunta2 == "2":
                pregunta5 = input ( "¿El número que pensaste es mayor que 6?")
                print ( "1. Sí")
                print ( "2. No")
                if pregunta5 == "1":
                    print ( "El número que pensaste es 7")
                elif pregunta5 == "2":
                    print ( "El número que pensaste es 6")
        elif pregunta1 == "2":
            pregunta6 = input ( "¿El número que pensaste es mayor que 3?")
            print ( "1. Sí")
            print ( "2. No")
            if pregunta6 == "1":
                pregunta7 = input ( "¿El número que pensaste es mayor que 4?")
                print ( "1. Sí")
                print ( "2. No")
                if pregunta7 == "1":
                    print ( "El número que pensaste es 5")
                elif pregunta7 == "2":
                    print ( "El número que pensaste es 4")
            elif pregunta6 == "2":
                pregunta8 = input ( "¿El número que pensaste es mayor que 1?")
                print ( "1. Sí")
                print ( "2. No")
                if pregunta8 == "1":
                    pregunta9 = input ( "¿El número que pensaste es mayor que 2?")
                    print ( "1. Sí")
                    print ( "2. No")
                    if pregunta9 == "1":
                        print ( "El número que pensaste es 3")
                    elif pregunta9 == "2":
                        print ( "El número que pensaste es 2")
                elif pregunta8 == "2":
                    print ( "El número que pensaste es 1")
    if juego == "2":
        empezar = False
        pass


funcionar = True
while funcionar == True:
    print ( "¿Qué quieres hacer?:")
    print ( "1. Realizar una nueva partida")
    print ( "2. Apagar el juego")

    pregunta = input ( "¿Qué quieres hacer?:")
    if pregunta == "1":
        funcionpartida ()
    elif pregunta == "2":
        print ( "Adiós")
        funcionar = False

