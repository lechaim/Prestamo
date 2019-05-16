from tkinter import *

class Prestamo:
	def __init__(self, root):
		self.root = root
		root.title("Simple GUI")

		self.lblCantidad = Label(root, text="Cantidad")
		self.lblCantidad.pack()

		self.lblInteres = Label(root, text="Interés")
		self.lblInteres.pack()

		self.lblTipoPago = Label(root, text="Tipo de pago")
		self.lblTipoPago.pack()

		self.lblTiempo = Label(root, text="Tiempo de pago")
		self.lblTiempo.pack()
        
        #comentario de prueba
        sasa


root = Tk()
my_gui = Prestamo(root)
root.mainloop()