#Agenda I

from tkinter import *
from tkinter import messagebox

lista =[]

def guardar():
    n = nombre.get()
    ap = app.get()
    am = apm.get()
    c = correo.get()
    t = telefono.get()
    lista.append(n+"$"+ap+"$"+am+"$"+t+"$"+c)
    escribirContacto()
    messagebox.showinfo("Guardado","El contacto ha sido guardado en la agenda")
    nombre.set("")
    app.set("")
    apm.set("")
    correo.set("")
    telefono.set("")
    consultar()


def eliminar():
    eliminado = conteliminar.get()
    removido = False
    for elemento in lista:
        arreglo = elemento.split("$")
        if conteliminar.get() == arreglo[3]:
            lista.remove(elemento)
            removido = True
    escribirContacto()
    consultar()
    if removido:
        messagebox.showinfo("Eliminar","Elemento eliminado "+eliminado)

def consultar():
    r = Text(root, width=80, height=15)
    lista.sort()
    valores = []
    r.insert(INSERT, "Nombre\tApellidos P\t\tApellido M\t\tTeléfono\t\tCorreo\n")
    for elemento in lista:
        arreglo = elemento.split("$")
        valores.append(arreglo[3])
        r.insert(INSERT, arreglo[0]+"\t"+arreglo[1]+"\t\t"+
        arreglo[2]+"\t\t"+arreglo[3]+"\t\t"+arreglo[4]+"\t\n")
    r.place(x=20,y=230)
    spinTelefono = Spinbox(root, value=(valores),textvariable=conteliminar).place(x=450,
    y=50)
    if lista ==[]:
        spinTelefono = Spinbox(root, value=(valores)).place(x=450,y=50)
    r.config(state=DISABLED)

def iniciarArchivo():
    archivo = open("ag.txt","a")
    archivo.close()

def cargar():
    archivo = open("ag.txt","r")
    linea = archivo.readline()
    if linea:
        while linea:
            if linea[-1]=='\n':
                linea = linea[:-1]
            lista.append(linea)
            linea = archivo.readline()
    archivo.close()

def escribirContacto():
    archivo = open("ag.txt","w")
    lista.sort()
    for elemento in lista:
        archivo.write(elemento+"\n")
    archivo.close()


root = Tk()
nombre = StringVar()
app = StringVar()
apm = StringVar()
correo = StringVar()
telefono = StringVar()
conteliminar = StringVar()
colorFondo = "#006"
coloLetra = "#FFF"
root.title("Agenda con archivos")
root.geometry("700x500")
root.config(bg= colorFondo)
etiquetaTitulo = Label(root, text="Agenda con archivos",bg=colorFondo, fg=coloLetra).place(x=270,y=10)
etiquetaN = Label(root,text="Nombre",bg=colorFondo,fg=coloLetra).place(x=50,y=50)
cajaN= Entry(root,textvariable=nombre).place(x=150, y=50)
etiquetaApp = Label(root, text="Apellido Paterno",bg=colorFondo,fg=coloLetra).place(x=50,y=80)
cajaApp =Entry(root,textvariable=app).place(x=150,y=80)
etiquetaApm = Label(root,text="Apellido Materno", bg=colorFondo,fg=coloLetra).place(x=50,y=110)
cajaApm =Entry(root,textvariable=apm).place(x=150,y=110)
etiquetaT = Label(root,text="Telefono", bg=colorFondo,fg=coloLetra).place(x=50,y=140)
cajaT =Entry(root,textvariable=telefono).place(x=150,y=140)
etiquetaC = Label(root,text="Correo", bg=colorFondo,fg=coloLetra).place(x=50,y=170)
cajaC =Entry(root,textvariable=correo).place(x=150,y=170)
etiquetaEliminar = Label(root,text="Teléfono: ",bg=colorFondo,fg=coloLetra).place(x=370,y=50)
spinTelefono = Spinbox(root,textvariable=conteliminar).place(x=450,y=50)
botonGuardar = Button(root,text="Guardar",command=guardar,bg="#009",fg="white").place(x=180,y=200)
botonEliminar = Button(root,text="Eliminar",command=eliminar,bg="#009",fg="white").place(x=490,y=80)


mainloop()