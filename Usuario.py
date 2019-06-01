from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import sqlite3


#conn = sqlite3.connect('BD_trabajo.db')

#conn.execute("SELECT * FROM sqlite_master"); DICE QUE NO TIENE TABLAS


#conn.execute("INSERT INTO Usuario (id_usuario,usuario,contrasena) \
#     VALUES (4, 'MJoseph', 7240)");

#conn.commit()
#print ("Records created successfully");
#conn.close()


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
my_gui = Usuario(root)
root.mainloop()