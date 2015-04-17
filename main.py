import tkinter as tk
import MainWindow as main_window
import ConditionsWindow as conditions_window
import SettingsWindow as settings_window
import IrrigationWindow as irrigation_window

class Main(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
        for Fr in (main_window.MainWindow, conditions_window.ConditionsWindow, settings_window.SettingsWindow, irrigation_window.IrrigationWindow):
            frame = Fr(container, self)
            self.frames[Fr] = frame  # adds the frame to self.frames
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(main_window.MainWindow)

    def show_frame(self, cont):
       
        #has_method_set_lights_state = getattr(self.frames[cont], "set_lights_state", None) #check if the window has an attribute "set_lights_state"
        #has_method_set_fan_state = getattr(self.frames[cont], "set_fan_state", None) #check if the window has an attibute "set_fan_state"
        #has_method_set_curtain_state = getattr(self.frames[cont], "set_courtain_state", None) #check if the window has an attribute "set_curtain_state"
        
        #this try expand block updates the Condition window labels with their apropiate values
        try:
            if settings_window.SettingsWindow.lights == True:
                self.frames[cont].set_lights_state("Luces Encendidas")
            
            elif settings_window.SettingsWindow.lights == False:
                self.frames[cont].set_lights_state("Luces apagadas")
            
            if settings_window.SettingsWindow.fans == True:
                self.frames[cont].set_fan_state("Ventiladores Encendidos")
            
            elif settings_window.SettingsWindow.fans == False:
                self.frames[cont].set_fan_state("Ventiladores Apagados")
            
            self.frames[cont].set_curtain_state("Cortinas Activas " + settings_window.SettingsWindow.cur_level)
            
        except AttributeError:
            pass

        frame = self.frames[cont]
        frame.tkraise()

application = Main()
#gives a resolution of 800X400 to the window
application.geometry('{}x{}'.format(800, 480)) 
application.mainloop()


