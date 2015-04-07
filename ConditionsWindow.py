import tkinter as tk
from tkinter import ttk
import MainWindow as main_window

TITLE_FONT = ("ARIAL", 14)

class ConditionsWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #layout stuff see: http://effbot.org/tkinterbook/grid.htm#Tkinter.Grid.grid_rowconfigure-method
        #and also see: http://effbot.org/tkinterbook/grid.htm#Tkinter.Grid.grid_columnconfigure-method 
        #I had to apply a grid on self (which is the frame) so i can call grid_rowconfigure and grid_columnconfigure
        #because this methods only work in the parent widget that uses a grid to manage the layout`
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(2, minsize=200)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(1, minsize=200)

        #The back button
        back_button = tk.Button(self, text="Atras",
                command = lambda: controller.show_frame(main_window.MainWindow))
        back_button.grid(row=0, column=0)
               
        #Title Label Pane

        tit_label_pane = ttk.PanedWindow(self, orient="horizontal")
        tit_label_pane.grid(row=1, column=2)
        
        #the Main label
        label = tk.Label(self, text="Condiciones del Invernadero", font=TITLE_FONT)

        tit_label_pane.add(label)
        
        #Temperature information widgets
        temp_range_pane = tk.PanedWindow(self, orient="vertical", bg="black")
        temp_range_pane.grid(row=2, column=1)

        trange_label = ttk.Label(self, text="Rango: min-max")
        temperature_label = ttk.Label(self,text="Temperatura: t")

        temp_range_pane.add(trange_label)
        temp_range_pane.add(temperature_label)

        #Humidity information widgets
        hum_range_pane = tk.PanedWindow(self, orient="vertical", bg="black")
        hum_range_pane.grid(row=3, column=1)

        hrange_label = ttk.Label(self, text="Rango: min-max")
        humidity_label = ttk.Label(self,text="Temperatura: t")

        hum_range_pane.add(hrange_label)
        hum_range_pane.add(humidity_label)

        #######Indicators code goes here#######
        #Temperature indicator
        temp_indicator_pane = tk.PanedWindow(self, bg="black", orient="vertical")
        temp_indicator_pane.grid(row=2, column=2)

        temp_indicator = tk.Canvas(self, width=30, height=100)
        temp_indicator.create_rectangle(0,0,150,100, fill="red")

        temp_indicator_pane.add(temp_indicator)

        #Humidity Indicator
        hum_indicator_pane = tk.PanedWindow(self, bg="black", orient="vertical")
        hum_indicator_pane.grid(row=3, column=2,)

        hum_indicator = tk.Canvas(self, width=30, height=100)
        hum_indicator.create_rectangle(0,0,150,100, fill="red")

        hum_indicator_pane.add(hum_indicator)

        #######################################
        
        #info Paned
        #info_pane = tk.PanedWindow(self, orient="vertical", width=100)
        #info_pane.grid(row=3,column=7)
        #info_pane.grid_rowconfigure(1, weight=1)
        #info_pane.grid_rowconfigure(3,weight=1)
        #info_pane.grid_rowconfigure(4,weight=1)
        #Riego system information widgets
        rie_info_pane = ttk.PanedWindow(self, orient="vertical")
        rie_info_pane.grid(row=2, column=4)
        rie_info_pane.place(x=560, y=100)

        rie_sis_label = ttk.Label(self, text="Sistema de Riego:")
        rie_ind_label = ttk.Label(self,text="act/desc")

        rie_info_pane.add(rie_sis_label)
        rie_info_pane.add(rie_ind_label)

        #Lights system information widgets
        lights_info_pane = ttk.PanedWindow(self, orient="vertical")
        lights_info_pane.grid(row=3, column=4)
        lights_info_pane.place(x=560, y=200)

        lights_ind_label = ttk.Label(self, text="Luces: act/desc")

        lights_info_pane.add(lights_ind_label)

        #fans system information widgets
        fan_info_pane = ttk.PanedWindow(self, orient="vertical")
        fan_info_pane.grid(row=4, column=4)
        fan_info_pane.place(x=560, y=300)

        fan_ind_label = ttk.Label(self, text="Ventiladores: act/desc")

        fan_info_pane.add(fan_ind_label)

        #curtain system information widgets
        cur_info_pane = ttk.PanedWindow(self, orient="vertical")
        cur_info_pane.grid(row=5, column=4)
        cur_info_pane.place(x=560, y=400)
        cur_ind_label = ttk.Label(self, text="Cortinas: act/desc")

        cur_info_pane.add(cur_ind_label)

        #add others pane to the info pane 
        #info_pane.add(rie_info_pane)
        #info_pane.add(lights_info_pane)
        #info_pane.add(fan_info_pane)
        #info_pane.add(cur_info_pane)

