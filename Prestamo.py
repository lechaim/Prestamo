from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from datetime import date, datetime, timedelta
# usr/bin/bash -tt

class Prestamo:
	def __init__(self, root):
		self.root = root
		root.title("Simple GUI")
		root.geometry("650x500")

		menu = Menu(root)
		self.root.config(menu=menu)

		file = Menu(menu)

		file.add_command(label = "Exit")
		menu.add_cascade(label = "File", menu = file)

		#root.resizable(0,0)  
		#root.overrideredirect(True) QUITA LA X

		root.bind("<Return>", self.pulsarEnter)

		#labels
		self.lblCantidad = Label(root, text="Cantidad")
		self.lblCantidad.grid(row=0, column=0, pady = 10, padx = 15, sticky=W)       

		self.lblInteres = Label(root, text="Interés")
		self.lblInteres.grid(row=1, column=0, pady = 10, padx = 15, sticky=W)

		self.lblTipoPago = Label(root, text="Tipo de pago")
		self.lblTipoPago.grid(row=2, column=0, pady = 10, padx = 15, sticky=W)

		self.lblTiempo = Label(root, text="Tiempo de pago")
		self.lblTiempo.grid(row=3, column=0, pady = 10, padx = 15, sticky=W)

		# textboxes

		self.txtCantidad = Entry(root)
		self.txtCantidad.grid(row=0, column=1, pady = 10, padx = 50)

		self.txtInteres =  Entry(root)
		self.txtInteres.grid(row=1, column=1, pady = 10, padx = 5)

		self.cmbTipoPago = ttk.Combobox(root, values = ["Semanal", "Quincenal", "Mensual"], width = 17)
		self.cmbTipoPago.grid(row=2, column=1, pady = 10, padx = 5)
		self.cmbTipoPago.set("Semanal")

		self.txtTiempo = Entry(root)
		self.txtTiempo.grid(row=3, column=1, pady = 10, padx = 5)
		
		#botones

		self.btnCalcular = Button(root, text = "Calcular", command = self.calcular)
		self.btnCalcular.grid(row=4, column=0, pady =15, padx = 5)

		self.btnLimpiar = Button(root, text = "Limpiar", command = self.borrar )
		self.btnLimpiar.grid(row=4, column=1, pady = 15, padx = 5, sticky=W)

		self.btnCerrar = Button(root, text = "Cerrar", command = self.cerrar)
		self.btnCerrar.grid(row=4, column=2, pady = 15, padx = 5, sticky=SW)

		#funciones

	def borrar(self):
		self.txtInteres.delete("0", END)
		self.txtCantidad.delete("0", END)
		self.txtTiempo.delete("0", END)
		self.cmbTipoPago.delete("0",END)
		

	def calcular(self):

		try:

			interes = int(self.txtInteres.get()) / 100
			cantidad = int(self.txtCantidad.get())
			resultado = (cantidad + (cantidad * interes)) / int(self.txtTiempo.get())
			tipo_pago = self.cmbTipoPago.get()

			if tipo_pago == "Semanal":
				tipo_pago = 7

			elif tipo_pago == "Quincenal":
				tipo_pago = 15

			else:
				tipo_pago = 30


			self.perdelta(date.today(), int(self.txtTiempo.get()), tipo_pago, resultado)

		except:

			tkinter.messagebox.showinfo("eroir", "Ha introducido los datos de mala forma")


	def cerrar(self):
		self.root.destroy()  #funcion para cerrar en un boton

	def perdelta(self, start, end, delta, resultado):
		curr = start
		rafar = ""
		delta = timedelta(days=delta)
		rafar += "El prestamos fue expedido el dia {}\n\n".format(start)

		for e in range(end):

			
			curr += delta
			rafar += "Deberá pagar {} pesos el día {}\n".format(resultado, curr)
			
		return tkinter.messagebox.showinfo("title", rafar)     

	def pulsarEnter(self, event=None):

		self.calcular()


root = Tk()
my_gui = Prestamo(root)
root.mainloop()