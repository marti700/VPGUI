import tkinter as tk
from tkinter import ttk
import MainWindow as main_window

TITLE_FONT = ("ARIAL", 14)

class ConditionsWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
       
        #The back button
        back_button = tk.Button(self, text="Atras",
                command = lambda: controller.show_frame(main_window.MainWindow))
        back_button.pack()
               
        #the Main label
        label = tk.Label(self, text="Condiciones del Invernadero", font=TITLE_FONT)
        label.pack()
        
        #Temperature information widgets
        temp_range_pane = ttk.PanedWindow(self, orient="vertical")
        temp_range_pane.pack(fill="both", expand=1)

        trange_label = ttk.Label(self, text="Rango: min-max")
        temperature_label = ttk.Label(self,text="Temperatura: t")

        temp_range_pane.add(trange_label)
        temp_range_pane.add(temperature_label)

        #Humidity information widgets
        hum_range_pane = ttk.PanedWindow(self, orient="vertical")
        hum_range_pane.pack(fill="both", expand=1)

        hrange_label = ttk.Label(self, text="Rango: min-max")
        humidity_label = ttk.Label(self,text="Temperatura: t")

        hum_range_pane.add(hrange_label)
        hum_range_pane.add(humidity_label)


        #Riego system information widgets
        rie_info_pane = ttk.PanedWindow(self, orient="vertical")
        rie_info_pane.pack(fill="both", expand=1)

        rie_sis_label = ttk.Label(self, text="Sistema de Riego:")
        rie_ind_label = ttk.Label(self,text="act/desc")

        rie_info_pane.add(rie_sis_label)
        rie_info_pane.add(rie_ind_label)

        #Lights system information widgets
        lights_info_pane = ttk.PanedWindow(self, orient="vertical")
        lights_info_pane.pack(fill="both", expand=1)

        lights_ind_label = ttk.Label(self, text="Luces: act/desc")

        rie_info_pane.add(lights_ind_label)

        #fans system information widgets
        fan_info_pane = ttk.PanedWindow(self, orient="vertical")
        fan_info_pane.pack(fill="both", expand=1)

        fan_ind_label = ttk.Label(self, text="Ventiladores: act/desc")

        fan_info_pane.add(fan_ind_label)

        #curtain system information widgets
        cur_info_pane = ttk.PanedWindow(self, orient="vertical")
        cur_info_pane.pack(fill="both", expand=1)

        cur_ind_label = ttk.Label(self, text="Cortinas: act/desc")

        cur_info_pane.add(cur_ind_label)


