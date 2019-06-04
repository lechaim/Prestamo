from tkinter import *
import tkinter.messagebox
from tkinter import ttk

class Principal:
	
	def __init__(self, root):
		self.root = root
		root.title("PretaO")
		root.geometry("650x500")

		self.btnCalcular = Button(root, text = "Abridor de la clase prestamo", command= self.abreClasePrestamo)
		self.btnCalcular.grid(row=4, column=0, pady =15, padx = 5)


	def abreClasePrestamo(self):
		Principal().destroy()
		Usuario(root)


class Usuario:

	def __init__(self, root):
		self.root = root
		root.title("Usuario")
		root.geometry("350x300")

		#labels
		self.lblNombreUsuario = Label(root, text="Usuario")
		self.lblNombreUsuario.grid(row=0, column=0, pady = 10, padx = 15, sticky=W)       

		self.lblContrasena = Label(root, text="Contraseña")
		self.lblContrasena.grid(row=1, column=0, pady = 10, padx = 15, sticky=W)
class Principal:
	
	def __init__(self, root):
		self.root = root
		root.title("PretaO")
		root.geometry("650x500")

		self.btnCalcular = Button(root, text = "Abridor de la clase prestamo", command= self.abreClasePrestamo)
		self.btnCalcular.grid(row=4, column=0, pady =15, padx = 5)


	def abreClasePrestamo(self):
		Usuario(root)
		# textboxes

		self.txtNombreUsuario = Entry(root)
		self.txtNombreUsuario.grid(row=0, column=1, pady = 10, padx = 50)

		self.txtContrasena =  Entry(root, show = "*")
		self.txtContrasena.grid(row=1, column=1, pady = 10, padx = 5)

		#botones

		self.btnLogin = Button(root, text = "LOG IN", command = self.logIn)
		self.btnLogin.grid(row=3, column=0, pady =15, padx = 5)

		self.btnOlvide = Button(root, text = "Olvidé mi contraseña", command = self.logIn)
		self.btnOlvide.grid(row=3, column=1, pady =15, padx = 5)


		#funciones
	def logIn(self):


		nombre = self.txtNombreUsuario.get()
		contrasena = self.txtContrasena.get()

		conn = sqlite3.connect('BD_trabajo.db')
		cursor = conn.cursor()

		#cursor.execute("INSERT INTO Usuario (id_usuario,nombre_usuario,contrasena) VALUES (?,?,?)", (11, nombre, contrasena)); insertar (para futuras referencia)

		cursor.execute("SELECT nombre_usuario, contrasena FROM Usuario WHERE nombre_usuario = ? AND contrasena= ?", (nombre, contrasena))
		
		if len(cursor.fetchall()) > 0:
			tkinter.messagebox.showinfo("Mensaje", "Bienvenido!")
		else:
			tkinter.messagebox.showinfo("Mensaje", "Nombre de usuario o contraseña incorrecta, por favor verifique sus datos.")

		#result = cursor.fetchone()

		#tkinter.messagebox.showinfo("Error", "Los datos han sido suministrados de la manera correcta")
		#conn.close()
		#except:

			#tkinter.messagebox.showinfo("Error", "Por favor introduzca los datos de la manera correcta")
			#conn.close()

root = Tk()
my_gui = Principal(root)
root.mainloop()