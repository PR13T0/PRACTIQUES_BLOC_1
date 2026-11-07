from tkinter import *
ventana = Tk()
ventana.config(bg="black")
ventana.iconbitmap("logo.ico")
ventana.geometry("500x500")
ventana.resizable(1,1)
ventana.title("Prieto's")



pantalla1 = Frame(ventana)
pantalla1.config(bd=30)
pantalla1.config(relief='sunken')
pantalla1.config(cursor='heart')
label = Label(pantalla1, text="Que tengas un buen día")
label.place(x=50, y=30)
label.config(bg='brown')
label.config(font=('Serif', 20, 'bold',))
label.config(fg='white')
pantalla1.config(width=1250, height=300)
pantalla1.config(bg='blue')
pantalla1.pack()

pantalla2 = Frame(ventana)
pantalla2.config(width=650, height=300)
pantalla2.config(cursor='star')
pantalla2.config(bg='magenta')
pantalla2.pack(side=LEFT)

pantalla3 = Frame(ventana)
pantalla3.config(width=650, height=300)
pantalla3.config(cursor='gumby')
pantalla3.config(bg='yellow')
pantalla3.pack(side=RIGHT)


ventana.mainloop()