from tkinter import *
ventana = Tk()
ventana.title('Prueba de TEXT')
pantalla=Frame(ventana, width=600, height=500)
pantalla.pack()

cuadroComentario=Text(pantalla)
comentario=Label(pantalla, text='Añadir comentarios: ')
comentario.grid(row=1, column=1)
cuadroComentario=Text(pantalla)
cuadroComentario.grid(row=1, column=2)

scrollVertical=Scrollbar(pantalla, command=cuadroComentario.yview)
scrollVertical=Scrollbar(pantalla, command=cuadroComentario.yview)
scrollVertical.grid(row=1, column=3)
scrollVertical.grid(row=1, column=3, sticky='nsew')
cuadroComentario.config(yscrollcommand=scrollVertical.set)

def codigoFuncion():
    textoescrito.set('Hola, ¿cómo estás?')

botonGuardar=Button(ventana, text='Saludos',command=codigoFuncion) 
botonGuardar.pack()

textoescrito=StringVar()

def codigoFuncion2():
 buttonVerde.pack()
 buttonAzul.pack()
 buttonRojo.pack()
 buttonBlanco.pack()
 buttonMorado.pack()
 buttonAmarillo.pack()
 buttonAtras.pack()

def codigoFuncion1():
    cuadroComentario.config(bg='green')

def codigoFuncion3():
    cuadroComentario.config(bg='blue')

def codigoFuncion4():
    cuadroComentario.config(bg='red')

def codigoFuncion5():
    cuadroComentario.config(bg='white')

def codigoFuncion6():
    cuadroComentario.config(bg='purple')

def codigoFuncion7():
    cuadroComentario.config(bg='yellow')

def codigoFuncion8():
    buttonVerde.pack_forget()
    buttonAzul.pack_forget()
    buttonRojo.pack_forget()
    buttonBlanco.pack_forget()
    buttonMorado.pack_forget()
    buttonAmarillo.pack_forget()
    buttonAtras.pack_forget()

buttonColores=Button(ventana, text='Colores',command=codigoFuncion2)
buttonColores.pack()

buttonVerde=Button(ventana, text='Verde',command=codigoFuncion1)
buttonAzul=Button(ventana, text='Azul',command=codigoFuncion3)
buttonRojo=Button(ventana, text='Rojo',command=codigoFuncion4)
buttonBlanco=Button(ventana, text='Blanco',command=codigoFuncion5)
buttonMorado=Button(ventana, text='Morado',command=codigoFuncion6)
buttonAmarillo=Button(ventana, text='Amarillo',command=codigoFuncion7)
buttonAtras=Button(ventana, text='Atrás',command=codigoFuncion8)

def codigoFuncion9():
    buttonTexto1.pack()
    buttonTexto2.pack()
    buttonTexto3.pack()
    buttonTexto4.pack()
    buttonTexto5.pack()
    buttonTexto6.pack()
    buttonTexto7.pack()
    buttonText8.pack()

def codigoFuncion10():
    nombreCampo.config(fg='green')
    cuadroComentario.config(fg='green')

def codigoFuncion11():
    nombreCampo.config(fg='blue')
    cuadroComentario.config(fg='blue')

def codigoFuncion12():
    nombreCampo.config(fg='red')
    cuadroComentario.config(fg='red')

def codigoFuncion13():
    nombreCampo.config(fg='white')
    cuadroComentario.config(fg='white')

def codigoFuncion14():
    nombreCampo.config(fg='purple')
    cuadroComentario.config(fg='purple')

def codigoFuncion15():
    nombreCampo.config(fg='yellow') 
    cuadroComentario.config(fg='yellow')

def codigoFuncion16():
    nombreCampo.config(fg='black')
    cuadroComentario.config(fg='black')

def codigoFuncion17():
    buttonTexto1.pack_forget()
    buttonTexto2.pack_forget()
    buttonTexto3.pack_forget()
    buttonTexto4.pack_forget()
    buttonTexto5.pack_forget()
    buttonTexto6.pack_forget()
    buttonTexto7.pack_forget()
    buttonText8.pack_forget()

buttonTexto=Button(ventana, text='Texto',command=codigoFuncion9)
buttonTexto.pack()

buttonTexto1=Button(ventana, text='Verde',command=codigoFuncion10)
buttonTexto2=Button(ventana, text='Azul',command=codigoFuncion11)
buttonTexto3=Button(ventana, text='Rojo',command=codigoFuncion12)
buttonTexto4=Button(ventana, text='Blanco',command=codigoFuncion13)
buttonTexto5=Button(ventana, text='Morado',command=codigoFuncion14)
buttonTexto6=Button(ventana, text='Amarillo',command=codigoFuncion15)
buttonTexto7=Button(ventana, text='Negro',command=codigoFuncion16)
buttonText8=Button(ventana, text='Atras',command=codigoFuncion17)

def codigoFuncion18():
    buttonCentrar1.pack()
    buttonCentrar2.pack()
    buttonCentrar3.pack()
    buttonCentrar4.pack()

def codigoFuncion19():
    nombreCampo.config(justify='center')
    

def codigoFuncion20():
    nombreCampo.config(justify='right')
   

def codigoFuncion21():
    nombreCampo.config(justify='left')
  

def codigoFuncion22():
    buttonCentrar1.pack_forget()
    buttonCentrar2.pack_forget()
    buttonCentrar3.pack_forget()
    buttonCentrar4.pack_forget()

buttonCentrar=Button(ventana, text='Centrar',command=codigoFuncion18)
buttonCentrar.pack()

buttonCentrar1=Button(ventana, text='Centro',command=codigoFuncion19)
buttonCentrar2=Button(ventana, text='Derecha',command=codigoFuncion20)
buttonCentrar3=Button(ventana, text='Izquierda',command=codigoFuncion21)
buttonCentrar4=Button(ventana, text='Atras',command=codigoFuncion22)

nombreEtiqueta=Label(pantalla, text='Nombre: ')
nombreEtiqueta.grid(row=0, column=1)
nombreCampo=Entry(pantalla, textvariable=textoescrito)
nombreCampo.grid(row=0, column=2) 


ventana.mainloop()