'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        nombre_max = ""
        nombre_min = ""
        cantidad_max = 0
        cantidad_min = 0
        edad_min = 0
        edad_max= 0
    

        while True:
            nombre = prompt("", "Ingrese su nombre")
            while nombre == None or not nombre.isalpha():
                nombre = prompt("","Ingrese su nombre")
                
            edad = prompt("", "Ingrese su edad")
            while edad == None or not edad.isdigit() or  int(edad) < 25:
                edad = prompt("","Ingrese su edad")
            edad = int(edad)
            cantidad = prompt("","Ingrese la cantida")
            while cantidad == None or not cantidad.isdigit() or int(cantidad) <=0:
                cantidad = prompt("","Ingrese la cantidad")

            cantidad= int(cantidad)
            continar = question("Titulo", "Desea continuar?")

            if cantidad_max == False:
                cantidad_max = True
                cantidad_max = nombre

            cantidad =int(cantidad)
            if cantidad_max > cantidad
            



                


            if not continar:
                break





if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
