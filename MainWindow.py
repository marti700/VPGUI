import tkinter as tk
from tkinter import ttk
import ConditionsWindow as conditions_window

TITLE_FONT = ("ARIAL", 14)

class MainWindow(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #buttons and main lable panes
        buttons_pane = ttk.PanedWindow(self, orient="horizontal")
        buttons_pane.grid(row=5, column=2)
        
        win_tittle_pane = ttk.PanedWindow(self, orient="horizontal")
        win_tittle_pane.grid(row=1, column=2)
        

        #title label
        label = ttk.Label(self, text="Menú principal", font=TITLE_FONT)
        label.grid(row=1, column=5)

        #buttons
        conditions_button = ttk.Button(self, text="condiciones",
                command = lambda: controller.show_frame(conditions_window.ConditionsWindow))
        conditions_button.grid(row=1, column=2)
        
        settings_button = ttk.Button(self, text="Ajustes")
        settings_button.grid(row=1, column=4)

        graph_button = ttk.Button(self, text="Gráfica de Tendencias")
        graph_button.grid(row=1, column=6)

        alarms_button = ttk.Button(self, text="Pantallas de Alarma")
        alarms_button.grid(row=1, column= 8)

        #add buttons to pane
        buttons_pane.add(conditions_button)
        buttons_pane.add(settings_button)
        buttons_pane.add(graph_button)
        buttons_pane.add(alarms_button)

        #add title label to pane
        win_tittle_pane.add(label)


