def funcionpartida ():
    global funcionar
    print ( "1. Empezar")
    print ( "2. Apagar el juego")
    juego = input ( "Instrucciones: usted tendrá que cumplir con las instrucciones que le diga en una hoja de papel. El juego terminará cuando yo consiga adivinar su edad.")
    if juego == "1":
        print("Escriba el número de su mes de nacimiento: ")
        print("1. Listo")
        print("2. Atrás")
        pregunta1 = input("Respuesta: ")
        if pregunta1 == "1":
            print("A continuación, multiplicalo por 5")
            print("1. Listo")
            print("2. Atrás")
            pregunta2 = input("Respuesta: ")
            if pregunta2 == "1":
                print("Ahora súmale 6 al número que obtuviste")
                print("1. Listo")
                print("2. Atrás")
                pregunta3 = input("Respuesta: ")    
                if pregunta3 == "1":
                    print("Ahora multiplica el número resultante por 4")
                    print("1. Listo")
                    print("2. Atrás")
                    pregunta4 = input("Respuesta: ")
                    if pregunta4 == "1":
                        print("Ahora súmale 9 al número que obtuviste")
                        print("1. Listo")
                        print("2. Atrás")
                        pregunta5 = input("Respuesta: ")
                        if pregunta5 == "1":
                            print("Ahora multiplica el número que obtuviste por 5")
                            print("1. Listo")
                            print("2. Atrás")
                            pregunta6 = input("Respuesta: ")
                            if pregunta6 == "1":
                               print("Ahora súmale el número de su día de nacimiento al resultado")
                               print("1. Listo")
                               print("2. Atrás")
                               pregunta7 = input("Respuesta: ")
                               if pregunta7 == "1":
                                   numero = int(input("Ingrese el resultado final que obtuvo: "))
                                   resultado = numero - 165
                                   print("Su día de nacimiento es: ", resultado)
                                   print("Los primeros dígitos son el mes de nacimiento y los dos últimos dígitos son el día de nacimiento.")
                                   print("1. Atrás")
                                   print("2. Terminar")
                                   pregunta8 = input("Respuesta: ")
                                   if pregunta8 == "1":
                                    pass
                                   elif pregunta8 == "2":
                                    print("Adiós")
                                    funcionar = 0
                               elif pregunta7 == "2":
                                   pass
                            elif pregunta6 == "2":
                                pass
                        elif pregunta5 == "2":
                            pass
                    elif pregunta4 == "2":
                        pass
                elif pregunta3 == "2":
                    pass
            elif pregunta2 == "2":
                pass   
        elif pregunta1 == "2":
            pass
    elif juego == "2":
        print("Adiós")
        funcionar = 0   

funcionar = 1
while funcionar == 1:
    funcionpartida()
        








