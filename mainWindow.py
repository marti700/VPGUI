import tkinter as tk

TITLE_FONT = ("ARIAL", 14)

class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Menú principal", font=TITLE_FONT)
        label.pack()

        conditions_button = tk.Button(self, text="condiciones")
        conditions_button.pack()
        
        settings_button = tk.Button(self, text="Ajustes")
        settings_button.pack()

        graph_button = tk.Button(self, text="Gráfica de Tendencias")
        graph_button.pack()

        alarms_button = tk.Button(self, text="Pantallas de Alarma")
        alarms_button.pack()





