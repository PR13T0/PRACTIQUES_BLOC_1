from tkinter import *
ventana = Tk()
ventana.title('Preguntas')
ventana.config(bg="yellow")
pantalla=Frame(ventana, width=500, height=300, bg='orange')
pantalla.pack()

cuadroTexto=Entry(pantalla)
cuadroTexto.grid(row=1, column=2)
pregunta1=Label(pantalla, text='¿Cuál es su nombre? ')
pregunta1.grid(row=1, column=1)
pregunta1.config(bg='pink')

cuadroTexto2=Entry(pantalla)
cuadroTexto2.grid(row=3, column=2)
pregunta2=Label(pantalla, text='¿Cuál es su edad? ')
pregunta2.grid(row=3, column=1)
pregunta2.config(bd='10')

cuadroTexto3=Entry(pantalla)
cuadroTexto3.grid(row=5, column=2)
pregunta3=Label(pantalla, text='¿Qué prefiere usted, perros o gatos? ')
pregunta3.grid(row=5, column=1)
pregunta3.config(font='Serif 10 bold')

cuadroTexto4=Entry(pantalla)
cuadroTexto4.grid(row=7, column=2)
cuadroTexto4.config(show='*')
pregunta4=Label(pantalla, text='¿Qué prefiere usted, playa o piscina? ')
pregunta4.grid(row=7, column=1)

ventana.mainloop()
