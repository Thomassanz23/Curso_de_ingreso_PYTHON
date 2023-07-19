import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        acumualdor_negativos = 0 
        acumualdor_positivos = 0
        contador_negativos = 0 
        contador_positivos = 0
        contador_ceros = 0
        direfencia = 0


        numero_ingresado =''

        while numero_ingresado !=None:
            numero_ingresado = prompt("Ej 10","Ingrese un numero")

            if numero_ingresado != None:
                numero_ingresado = int(numero_ingresado)

                if numero_ingresado < 0:
                    acumualdor_negativos += numero_ingresado
                    contador_negativos += 1
                elif numero_ingresado > 0:
                    acumualdor_positivos += numero_ingresado
                    contador_positivos += 1
                
                else:
                    contador_ceros += 1

        direfencia =contador_positivos - contador_negativos

        mensaje = f"La suma de los negativos es:{acumualdor_negativos} \n"
        mensaje += f"La suma de los positivos{acumualdor_positivos}\n"
        mensaje += f"cantidad a negativos {contador_negativos}\n"
        mensaje += f"cantidad a positivos{contador_positivos}\n"
        mensaje += f"cantidad de ceroz{contador_ceros}\n"
        mensaje += f"Diferecian entre la cantidad de los numero de pisiticos ingresador y los negativos es :{direfencia}\n"

        alert ("respuestas", message=mensaje)

                


                
                
                
            
        pass

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
