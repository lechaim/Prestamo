from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from datetime import date, datetime, timedelta
# usr/bin/bash -tt

class Prestamo:
    def __init__(self, root):
        self.root = root
        root.title("Simple GUI")
        root.geometry("350x300")
        #root.resizable(0,0)  

        #root.overrideredirect(True) QUITA LA X

        #labels
        self.lblCantidad = Label(root, text="Cantidad")
        self.lblCantidad.grid(row=0, column=0, pady = 10, padx = 5)       

        self.lblInteres = Label(root, text="Interés")
        self.lblInteres.grid(row=1, column=0, pady = 10, padx = 5)

        self.lblTipoPago = Label(root, text="Tipo de pago")
        self.lblTipoPago.grid(row=2, column=0, pady = 10, padx = 5)

        self.lblTiempo = Label(root, text="Tiempo de pago")
        self.lblTiempo.grid(row=3, column=0, pady = 10, padx = 15)

        # textboxes

        self.txtCantidad = Entry(root)
        self.txtCantidad.grid(row=0, column=1, pady = 10, padx = 5)

        self.txtInteres =  Entry(root)
        self.txtInteres.grid(row=1, column=1, pady = 10, padx = 5)

        self.cmbTipoPago = ttk.Combobox(root, values = ["Semanal", "Quincenal", "Mensual"], width = 17)
        self.cmbTipoPago.grid(row=2, column=1, pady = 10, padx = 5)

        self.txtTiempo = Entry(root)
        self.txtTiempo.grid(row=3, column=1, pady = 10, padx = 5)
        
        #botones

        self.btnCalcular = Button(root, text = "Calcular", command = self.calcular).grid(row=4, column=0, pady = 10, padx = 5)

        self.btnLimpiar = Button(root, text = "Limpiar", command = self.borrar ).grid(row=4, column=1, pady = 10, padx = 5)

        self.btnCerrar = Button(root, text = "Cerrar", command = self.cerrar ).grid(row=4, column=2, pady = 10, padx = 5)

        #funciones

    def borrar(self):
        self.txtInteres.delete("0", END)
        self.txtCantidad.delete("0", END)
        self.txtTiempo.delete("0", END)
        self.cmbTipoPago.delete("0",END)
    	

    def calcular(self):

    	try:
    		rafar = ""

    		interes = int(self.txtInteres.get()) / 100
    		cantidad = int(self.txtCantidad.get())
    		resultado = (cantidad + (cantidad * interes)) / int(self.txtTiempo.get())
            

    		self.perdelta(date.today(), int(self.txtTiempo.get()), 7, resultado)

    		#tkinter.messagebox.showinfo("title", total)
    	except:

    		tkinter.messagebox.showinfo("eroir", "Ha introducido los datos de mala forma")


    def cerrar(self):
    	self.root.destroy()  #funcion para cerrar en un boton

    def perdelta(self, start, end, delta, resultado):
        curr = start
        rafar = ""
        delta = timedelta(days=delta)
        rafar += "El prestamos fue expedido el dia {}\n".format(start)

        for e in range(end):

	        
            curr += delta
            rafar += "Deberá pagar {} pesos el día {}\n".format(resultado, curr)
            
        return tkinter.messagebox.showinfo("title", rafar)     
         

root = Tk()
my_gui = Prestamo(root)
root.mainloop()