import tkinter as tk
from tkinter import ttk
import MainWindow as main_window
import IrrigationWindow as irrigation_system

TITLE_FONT = ("ARIAL", 14)

class SettingsWindow(tk.Frame):
    riego = False
    lights = False
    fans = False
    courtains  = False

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.height = 50 # for Temperature
        self.Hheight = 50 # for Humidity
        #says if the temp indicator should increase or decrease 
        #this is usless and this line can be safely deleted if the animation is not needed
        self.temp_inc_dec = True
        self.hum_inc_dec = True
        
        #layout stuff see: http://effbot.org/tkinterbook/grid.htm#Tkinter.Grid.grid_rowconfigure-method
        #and also see: http://effbot.org/tkinterbook/grid.htm#Tkinter.Grid.grid_columnconfigure-method 
        #I had to apply a grid on self (which is the frame) so i can call grid_rowconfigure and grid_columnconfigure
        #because this methods only work in the parent widget that uses a grid to manage the layout`
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(2, minsize=200)
        #self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(1, minsize=200)

        #The back button
        back_button = tk.Button(self, text="Atras",
                command = lambda: controller.show_frame(main_window.MainWindow))
        back_button.grid(row=0, column=0)
               
        #Title Label Pane
        tit_label_pane = ttk.PanedWindow(self, orient="horizontal")
        tit_label_pane.grid(row=1, column=2)
        
        #the Main label
        label = tk.Label(self, text="Ajustes", font=TITLE_FONT)
        tit_label_pane.add(label)
        
        #Temperature information widgets
        temp_adjust_pane = tk.PanedWindow(self, orient="horizontal", bg="black")
        temp_adjust_pane.grid(row=2, column=1)

        #temperature labels
        temp_labels_pane = tk.PanedWindow(self, orient="vertical")
        
        self.temperature_max_label = ttk.Label(self,text="Tempoeratura Maxima:")
        self.temperature_min_label = ttk.Label(self,text="Temperatura Minima:")
        temp_labels_pane.add(self.temperature_max_label)
        temp_labels_pane.add(self.temperature_min_label)
        
        #spinboxes
        temp_spinbox_pane = tk.PanedWindow(self, orient="vertical", bg="black")

        self.max_temp_spinbox = tk.Spinbox(self, from_=0, to=100, width=4)
        self.min_temp_spinbox = tk.Spinbox(self, from_=0, to=100, width=4)
        temp_spinbox_pane.add(self.max_temp_spinbox)
        temp_spinbox_pane.add(self.min_temp_spinbox)

        #set temperature button 
        set_temp_button = ttk.Button(self, text="Applicar")
       
        #Add widgets to main pane (temp_adjust_pane)
        temp_adjust_pane.add(temp_labels_pane)
        temp_adjust_pane.add(temp_spinbox_pane)
        temp_adjust_pane.add(set_temp_button)

       
        #adjustments Panes

        #Riego systme
        rie_adjust_pane = ttk.PanedWindow(self, orient="vertical")
        rie_adjust_pane.grid(row=2, column=4)
        rie_adjust_pane.place(x=560, y=100)

        self.rie_sis_button = ttk.Button(self, text="Activar Sistema de Riego",
                command = lambda: controller.show_frame(irrigation_system.IrrigationWindow))
        #rie_ind_label = ttk.Label(self,text="act/desc")

        rie_adjust_pane.add(self.rie_sis_button)
        #rie_info_pane.add(rie_ind_label)

        #Lights system information widgets
        lights_adjust_pane = ttk.PanedWindow(self, orient="vertical")
        lights_adjust_pane.grid(row=3, column=4)
        lights_adjust_pane.place(x=560, y=200)

        self.lights_ind_button = ttk.Button(self, text="Activar Luces",
                command = lambda: self.enable_disable_lights())

        lights_adjust_pane.add(self.lights_ind_button)

        #fans system information widgets
        fan_adjust_pane = ttk.PanedWindow(self, orient="vertical")
        fan_adjust_pane.grid(row=4, column=4)
        fan_adjust_pane.place(x=560, y=300)

        self.fan_ind_button = ttk.Button(self, text="Activar ventiladores",
                command= lambda: self.enable_disable_fans())

        fan_adjust_pane.add(self.fan_ind_button)

        #curtain system information widgets
        curtain_adjust_pane = ttk.PanedWindow(self, orient="vertical")
        curtain_adjust_pane.grid(row=5, column=4)
        curtain_adjust_pane.place(x=560, y=400)
        
        cur_label = ttk.Label(self, text="Cortinas: ")
        self.cur_ind_combobox = ttk.Combobox(self, values=("Desactivar","Nivel 1", "Nivel 2", "Nivel 3"), text="Cortinas")
        self.cur_button = ttk.Button(self,text="Aplicar", command = lambda: self.enable_disable_curtains())

        curtain_adjust_pane.add(cur_label)
        curtain_adjust_pane.add(self.cur_ind_combobox)
        curtain_adjust_pane.add(self.cur_button)

    #@staticmethod
    def enable_disable_riego_system(self):
        #controls the button text
        #when the button text is equal to "desactivar sistema de Riego"
        #the riego system is enabled and when the button text is equal to
        #"Activar sistema de riego" the riego system is disabled]
        #the button text will change to indicate the state of the riego system 
        #each time the button is pressed
        
        if SettingsWindow.riego == False:
            SettingsWindow.riego = True
            self.enable_riego_system() #Activate the regadores
            self.rie_sis_button.config(text="Desactivar sistema de riego")
        else:
            SettingsWindow.riego = False
            self.disable_riego_system() #Deactivate the Regadores
            self.rie_sis_button.config(text="Activar sistema de riego")
        
    
    def enable_riego_system(self):
        #TODO riego enabled logic here
        print("Riego Activado")

    def disable_riego_system(self):
        #TODO riego disabled logic here
        print("Riego desactivado")

    def enable_disable_lights(self):
        #controls the button text
        #when the button text is equal to "Apagar luces"
        #the lights system is enabled and when the button text is equal to
        #"Encender luces" the lights system is disabled
        #the button text will change to indicate the state of the lights system 
        #each time the button is pressed
        
        if SettingsWindow.lights == False:
            SettingsWindow.lights = True
            self.enable_lights() #Activate the lights
            self.lights_ind_button.config(text="Apagar Luces")
        else:
            SettingsWindow.lights = False
            self.disable_lights() #Deactivate the lights
            self.lights_ind_button.config(text="Encender Luces")
    
    def enable_lights(self):
        #TODO lights enabled logic here 
        print("Luces Encendidas")

    def disable_lights(self):
        #TODO lights disable logic height
        print("Luces Apagadas")
    
    def enable_disable_fans(self):
        #controls the button text
        #when the button text is equal to "Apagar Ventiladores"
        #the fans system is enabled and when the button text is equal to
        #"Encender Ventiladores" the fans system is disabled
        #the button text will change to indicate the state of the fan system 
        #each time the button is pressed
        
        if SettingsWindow.fans == False:
            SettingsWindow.fans = True
            self.enable_fans() #Activate the fans 
            self.fan_ind_button.config(text="Apagar Ventiladores")
        else:
            SettingsWindow.fans = False
            self.disable_fans() #Deactivate the fans
            self.fan_ind_button.config(text="Encender Ventiladores")
    
    def enable_fans(self):
        #TODO fans enabled logic here 
        print("Ventiladores Encendidos")

    def disable_fans(self):
        #TODO fans disable logic height
        print("Ventiladores Apagados")
    
    def enable_disable_curtains(self):
        if self.cur_ind_combobox.get() == "Nivel 1":
            print("Nivel 1 Activo")
            #TODO level 1 curtain Activation logic here
        elif self.cur_ind_combobox.get() == "Nivel 2":
            print("Nivel 2 Activo")
            #TODO level 2 curtain Activation logic here
        elif self.cur_ind_combobox.get() == "Nivel 3":
            print("Nivel 3 Activo")
            #TODO level 3 curtain Activation logic here
        elif self.cur_ind_combobox.get() == "Desactivar":
            print("Cortinas Desactiadas")
            #TODO curtain Deactivation logic here
        else:
            print("Unknow option")
       
