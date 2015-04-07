import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import ConditionsWindow as conditions_window

TITLE_FONT = ("ARIAL", 14)

class MainWindow(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
       
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0,minsize=150)
        self.grid_rowconfigure(1,minsize=300)
        self.grid_columnconfigure(1, minsize=170)
        #title label pane
        win_tittle_pane = ttk.PanedWindow(self, orient="horizontal")
        win_tittle_pane.grid(row=0, column=2)
        
        #buttons and main lable panes
        buttons_pane = ttk.PanedWindow(self, orient="horizontal")
        buttons_pane.grid(row=1, column=2)
        
        
        #title label
        label = ttk.Label(self, text="Menú principal", font=TITLE_FONT)
        label.grid(row=1, column=5)

        #buttons
        conditions_button = ttk.Button(self, text="condiciones",
                command = lambda: controller.show_frame(conditions_window.ConditionsWindow))
        
        settings_button = ttk.Button(self, text="Ajustes")

        graph_button = ttk.Button(self, text="Gráfica de Tendencias")

        alarms_button = ttk.Button(self, text="Pantallas de Alarma")

        #add buttons to pane
        buttons_pane.add(conditions_button)
        buttons_pane.add(settings_button)
        buttons_pane.add(graph_button)
        buttons_pane.add(alarms_button)

        #add title label to pane
        win_tittle_pane.add(label)


