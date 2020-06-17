#Agenda I

#JUAN PABLO MEZA GAZABÓN


from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re



lista =[]

listita=[]

try:
    archivo = open("ag.txt","r")
    listita = archivo.readlines()
except FileNotFoundError:
    print("WEA NO ENCONTRADA")
    listita=[]


correoValidar = False

#-----------------VALIDACIPONES---------------------------

#---------VALIDACIÓN TELÉFONO
def validate_telefono(text):
    return text.isdecimal()


def validarCorreo(text):

    
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',text.lower()):
	    correoValidar = True
    else:
	    correoValidar = False



def guardar():
    n = nombre.get()
    ap = app.get()
    am = apm.get()
    c = correo.get()
    t = telefono.get()


    if ((n != "") and (ap != "") and (am != "") and (c != "") and (t != "")):

        
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',c.lower()):

            lista.append(n+"$"+ap+"$"+am+"$"+t+"$"+c)
            listita.append(n+"$"+ap+"$"+am+"$"+t+"$"+c)
            
            escribirContacto()
            messagebox.showinfo("Guardado","El contacto ha sido guardado en la agenda")
            nombre.set("")
            app.set("")
            apm.set("")
            correo.set("")
            telefono.set("")
            consultar()
            lista.clear()
            
            #escribirContacto()
        else:
            messagebox.showerror("ERROR","Correo  inválido")
    else:
        messagebox.showwarning("¡ATENCIÓN!","Debe llenar todos los campos")


def eliminar():
    eliminado = conteliminar.get()

    if (eliminado != ""):

        removido = False
        for elemento in listita:
            arreglo = elemento.split("$")
            if conteliminar.get() == arreglo[3]:
                listita.remove(elemento)
                removido = True
        eliminarContactoArchivo(elemento)
        escribirContacto()
        consultar()
        if removido:
            messagebox.showinfo("Eliminar","Elemento eliminado "+eliminado)
    else:
        messagebox.showwarning("¡ATENCIÓN!","Debe llenar el campo del teléfono que desea eliminar")

def eliminarContactoArchivo(text):
   

    f = open("ag.txt","w")
 
    for linea in listita:
 
        if linea!=text+"\n":
 
      
            f.write(linea)
 

    f.close()

def consultar():
    r = Text(root, width=80, height=15)
    listita.reverse()
    valores = []
    r.insert(INSERT, "Nombre\tApellidos P\t\tApellido M\t\tTeléfono\t\tCorreo\n")
    for elemento in listita:
        arreglo = elemento.split("$")
        valores.append(arreglo[3])
        r.insert(INSERT, arreglo[0]+"\t"+arreglo[1]+"\t\t"+
        arreglo[2]+"\t\t"+arreglo[3]+"\t\t"+arreglo[4]+"\t\n")
    r.place(x=20,y=230)
    spinTelefono = Spinbox(root, value=(valores),textvariable=conteliminar).place(x=450,
    y=50)
    if listita ==[]:
        spinTelefono = Spinbox(root, value=(valores)).place(x=450,y=50)
    r.config(state=DISABLED)

def iniciarArchivo():
    archivo = open("ag.txt","r")
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
    archivo = open("ag.txt","a")
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
root.resizable(0,0)
etiquetaTitulo = Label(root, text="Agenda con archivos",bg=colorFondo, fg=coloLetra).place(x=270,y=10)
etiquetaN = Label(root,text="Nombre",bg=colorFondo,fg=coloLetra).place(x=50,y=50)
cajaN= Entry(root,textvariable=nombre).place(x=150, y=50)
etiquetaApp = Label(root, text="Apellido Paterno",bg=colorFondo,fg=coloLetra).place(x=50,y=80)
cajaApp =Entry(root,textvariable=app).place(x=150,y=80)
etiquetaApm = Label(root,text="Apellido Materno", bg=colorFondo,fg=coloLetra).place(x=50,y=110)
cajaApm =Entry(root,textvariable=apm).place(x=150,y=110)
etiquetaT = Label(root,text="Telefono", bg=colorFondo,fg=coloLetra).place(x=50,y=140)

cajaT = ttk.Entry(
    validate="key",
    textvariable=telefono,

    validatecommand=(root.register(validate_telefono), "%S")
)
cajaT.place(x=150, y=140)

etiquetaC = Label(root,text="Correo", bg=colorFondo,fg=coloLetra).place(x=50,y=170)


cajaC = ttk.Entry(
    validate="key",
    textvariable=correo,

    validatecommand=(root.register(validarCorreo), "%S")
)
cajaC.place(x=150, y=170)

etiquetaEliminar = Label(root,text="Teléfono: ",bg=colorFondo,fg=coloLetra).place(x=370,y=50)

spinTelefono = ttk.Spinbox(
    validate="key",
    textvariable=conteliminar,

    validatecommand=(root.register(validate_telefono), "%S")
)
spinTelefono.place(x=450,y=50)

botonGuardar = Button(root,text="Guardar",command=guardar,bg="#009",fg="white").place(x=180,y=200)
botonEliminar = Button(root,text="Eliminar",command=eliminar,bg="#009",fg="white").place(x=490,y=80)


mainloop()