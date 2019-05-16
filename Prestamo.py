from tkinter import *
from tkinter import ttk

class Prestamo:
    def __init__(self, root):
        self.root = root
        root.title("Simple GUI")
        root.geometry("550x650")

        #labels
        self.lblCantidad = Label(root, text="Cantidad").grid(row=0, column=0)       

        self.lblInteres = Label(root, text="Interés").grid(row=1, column=0)

        self.lblTipoPago = Label(root, text="Tipo de pago").grid(row=2, column=0)

        self.lblTiempo = Label(root, text="Tiempo de pago").grid(row=3, column=0)

        # textboxes

        self.txtCantidad = Entry(root).grid(row=0, column=1)

        self.txtInteres =  Entry(root).grid(row=1, column=1)

        self.cmbTipoPago = ttk.Combobox(root, values = ["Semanal", "Quincenal", "Mensual"], width = 18).grid(row=2, column=1)

        self.txtTiempo = Entry(root).grid(row=3, column=1)
        #ubuntu



root = Tk()
my_gui = Prestamo(root)
root.mainloop()