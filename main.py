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
        
        frame = self.frames[cont]
        frame.tkraise()

application = Main()
#gives a resolution of 800X400 to the window
application.geometry('{}x{}'.format(800, 480)) 
application.mainloop()


