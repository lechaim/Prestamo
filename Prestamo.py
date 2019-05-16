from tkinter import *
from tkinter import ttk

class Prestamo:
    def __init__(self, root):
        self.root = root
        root.title("Simple GUI")
        root.geometry("350x300")

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
        self.btnLimpiar = Button(root, text = "Limpiar", ).grid(row=4, column=1, pady = 10, padx = 5)


        #funciones

        interes = self.txtInteres.get()
        cantidad = self.txtCantidad.get()


    def borrar(self):
    	self.txtTiempo.delete(0, "END")
    	self.txtTiempo.update()

    def calcular(self):
    	newWindow = Toplevel(root)
    	newWindow.title("Pagos a realizar")
    	newWindow.geometry("350x300")

    	self.calculo = Label(newWindow, text="Aqui")
    	self.calculo.grid(row=0, column=0, pady = 10, padx = 5)


root = Tk()
my_gui = Prestamo(root)
root.mainloop()