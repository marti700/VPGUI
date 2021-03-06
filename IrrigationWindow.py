import tkinter as tk
from tkinter import ttk
import SettingsWindow as settings_window

TITLE_FONT = ("ARIAL", 14)

class IrrigationWindow(tk.Frame):
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
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(1, minsize=200)

        #The back button
        back_button = tk.Button(self, text="Atras",
                command = lambda: controller.show_frame(settings_window.SettingsWindow))
        back_button.grid(row=0, column=0)
               
        #Title Label Pane

        tit_label_pane = ttk.PanedWindow(self, orient="horizontal")
        tit_label_pane.grid(row=1, column=2)
        
        #the Main label
        label = tk.Label(self, text="Sistema de Riego", font=TITLE_FONT)

        tit_label_pane.add(label)
        
        # Irrigation Tanks 
        irrigation_tanks_pane = tk.PanedWindow
        #First Tank
        tank1_pane = tk.PanedWindow(self, orient="vertical", bg="black")
        tank1_pane.grid(row=2, column=1)
        
        tank1_label = ttk.Label(self, text="Tanque 1")
        
        #First tank pane entry
        tank1_entry_pane = ttk.PanedWindow(self, orient="horizontal")

        #tank 2 Label
        tank1_level_label = ttk.Label(self,text="ML")
        #tank 1 Entry
        self.tank1_level_entry = ttk.Entry(self)

        #add widgets to entry pane
        tank1_entry_pane.add(self.tank1_level_entry)
        tank1_entry_pane.add(tank1_level_label)

        tank1_pane.add(tank1_label)
        tank1_pane.add(tank1_entry_pane)

        #Second Tank
        tank2_pane = tk.PanedWindow(self, orient="vertical", bg="black")
        tank2_pane.grid(row=2, column=2)
        
        tank2_label = ttk.Label(self, text="Tanque 2")
        
        #First tank pane entry
        tank2_entry_pane = ttk.PanedWindow(self, orient="horizontal")

        #tank 2 Label
        tank2_level_label = ttk.Label(self,text="ML")
        #tank 2 Entry
        self.tank2_level_entry = ttk.Entry(self)

        #add widgets to entry pane
        tank2_entry_pane.add(self.tank2_level_entry)
        tank2_entry_pane.add(tank2_level_label)

        
        tank2_pane.add(tank2_label)
        tank2_pane.add(tank2_entry_pane)

        #Third Tank
        tank3_pane = tk.PanedWindow(self, orient="vertical", bg="black")
        tank3_pane.grid(row=2, column=3)
        
        tank3_label = ttk.Label(self, text="Tanque 3")
        
        #First tank pane entry
        tank3_entry_pane = ttk.PanedWindow(self, orient="horizontal")

        #tank 2 Label
        tank3_level_label = ttk.Label(self,text="ML")
        #tank 3 Entry
        self.tank3_level_entry = ttk.Entry(self)

        #add widgets to entry pane
        tank3_entry_pane.add(self.tank3_level_entry)
        tank3_entry_pane.add(tank3_level_label)

        
        tank3_pane.add(tank3_label)
        tank3_pane.add(tank3_entry_pane)

        #timers
        #timer 1
        timer_pane = tk.PanedWindow(self, orient="vertical", bg="black")
        timer_pane.grid(row=3, column=1)
        
        schedule = ttk.Label(self, text="timer 1")
        
        #start timer
        start_timer_pane = tk.PanedWindow(self, orient="horizontal")
        
        start_timer_label = ttk.Label(self, text="Inicio")

        #start timer entries
        self.start_timer_hours_entry = ttk.Entry(self, width=5)
        self.start_timer_minutes_entry = ttk.Entry(self, width=5)
        self.start_timer_seconds_entry = ttk.Entry(self, width=5)

        #add labels to start label and entries to start pane 
        start_timer_pane.add(start_timer_label)
        start_timer_pane.add(self.start_timer_hours_entry)
        start_timer_pane.add(self.start_timer_minutes_entry)
        start_timer_pane.add(self.start_timer_seconds_entry)

        #end timer
        end_timer_pane = tk.PanedWindow(self, orient="horizontal")
        
        end_timer_label = ttk.Label(self, text="Final")

        #end timer entries
        self.end_timer_hours_entry = ttk.Entry(self, width=5)
        self.end_timer_minutes_entry = ttk.Entry(self, width=5)
        self.end_timer_seconds_entry = ttk.Entry(self, width=5)

        #add labels to end label and entries to end pane 
        end_timer_pane.add(end_timer_label)
        end_timer_pane.add(self.end_timer_hours_entry)
        end_timer_pane.add(self.end_timer_minutes_entry)
        end_timer_pane.add(self.end_timer_seconds_entry)

        #add schedule timer to start timer pane 
        timer_pane.add(schedule)
        timer_pane.add(start_timer_pane)
        timer_pane.add(end_timer_pane)
        
        #timer 2
        
        timer2_pane = tk.PanedWindow(self, orient="vertical", bg="black")
        timer2_pane.grid(row=3, column=2)
        
        timer2_label = ttk.Label(self, text="Timer 2")
        
        #start timer 2  
        start_timer2_pane = tk.PanedWindow(self, orient="horizontal")
        
        start_timer2_label = ttk.Label(self, text="Inicio")

        #start timer entries
        self.start_timer2_hours_entry = ttk.Entry(self, width=5)
        self.start_timer2_minutes_entry = ttk.Entry(self, width=5)
        self.start_timer2_seconds_entry = ttk.Entry(self, width=5)

        #add labels to start label and entries to start pane 
        start_timer2_pane.add(start_timer2_label)
        start_timer2_pane.add(self.start_timer2_hours_entry)
        start_timer2_pane.add(self.start_timer2_minutes_entry)
        start_timer2_pane.add(self.start_timer2_seconds_entry)

        #end timer
        end_timer2_pane = tk.PanedWindow(self, orient="horizontal")
        
        end_timer2_label = ttk.Label(self, text="Final")

        #end timer entries
        self.end_timer2_hours_entry = ttk.Entry(self, width=5)
        self.end_timer2_minutes_entry = ttk.Entry(self, width=5)
        self.end_timer2_seconds_entry = ttk.Entry(self, width=5)

        #add labels to end label and entries to end pane 
        end_timer2_pane.add(end_timer2_label)
        end_timer2_pane.add(self.end_timer2_hours_entry)
        end_timer2_pane.add(self.end_timer2_minutes_entry)
        end_timer2_pane.add(self.end_timer2_seconds_entry)

        #add schedule timer to start timer pane 
        timer2_pane.add(timer2_label)
        timer2_pane.add(start_timer2_pane)
        timer2_pane.add(end_timer2_pane)
        
        #timer 3
        
        timer3_pane = tk.PanedWindow(self, orient="vertical", bg="black")
        timer3_pane.grid(row=3, column=3)
        
        timer3_label = ttk.Label(self, text="Timer 3")
        
        #start timer 3  
        start_timer3_pane = tk.PanedWindow(self, orient="horizontal")
        
        start_timer3_label = ttk.Label(self, text="Inicio")

        #start timer entries
        self.start_timer3_hours_entry = ttk.Entry(self, width=5)
        self.start_timer3_minutes_entry = ttk.Entry(self, width=5)
        self.start_timer3_seconds_entry = ttk.Entry(self, width=5)

        #add labels to start label and entries to start pane 
        start_timer3_pane.add(start_timer3_label)
        start_timer3_pane.add(self.start_timer3_hours_entry)
        start_timer3_pane.add(self.start_timer3_minutes_entry)
        start_timer3_pane.add(self.start_timer3_seconds_entry)

        #end timer
        end_timer3_pane = tk.PanedWindow(self, orient="horizontal")
        
        end_timer3_label = ttk.Label(self, text="Final")

        #end timer entries
        self.end_timer3_hours_entry = ttk.Entry(self, width=5)
        self.end_timer3_minutes_entry = ttk.Entry(self, width=5)
        self.end_timer3_seconds_entry = ttk.Entry(self, width=5)

        #add labels to end label and entries to end pane 
        end_timer3_pane.add(end_timer3_label)
        end_timer3_pane.add(self.end_timer3_hours_entry)
        end_timer3_pane.add(self.end_timer3_minutes_entry)
        end_timer3_pane.add(self.end_timer3_seconds_entry)

        #add schedule timer to start timer pane 
        timer3_pane.add(timer3_label)
        timer3_pane.add(start_timer3_pane)
        timer3_pane.add(end_timer3_pane)


        #button(S) pane 
        buttons_pane = tk.PanedWindow(self, orient="horizontal")
        buttons_pane.grid(row=4, column=4, sticky="e")
        
        set_button = tk.Button(self, text="Aplicar", 
                command = lambda: self.set_irrigation_timer())

        buttons_pane.add(set_button)

    def set_irrigation_timer(self):
        #TODO irrigation system logic here
        
        #this variables takes the entries text
        
        #taks entries
        tank1 = int(self.tank1_level_entry.get())
        tank2 = int(self.tank2_level_entry.get())
        tank3 = int(self.tank3_level_entry.get())

        #timer 1 entries
        start_hour = int(self.start_timer_hours_entry.get())
        start_minute = int(self.start_timer_minutes_entry.get())
        start_seconds = int(self.start_timer_seconds_entry.get())

        end_hour = int(self.end_timer_hours_entry.get())
        end_minutes = int(self.end_timer_minutes_entry.get())
        end_seconds = int(self.end_timer_seconds_entry.get())

        
        #timer 2 entries
        start2_hour = int(self.start_timer2_hours_entry.get())
        start2_minute = int(self.start_timer2_minutes_entry.get())
        start2_seconds = int(self.start_timer2_seconds_entry.get())

        end2_hour = int(self.end_timer2_hours_entry.get())
        end2_minutes = int(self.end_timer2_minutes_entry.get())
        end2_seconds = int(self.end_timer2_seconds_entry.get())

        #timer 3 entries
        start3_hour = int(self.start_timer3_hours_entry.get())
        start3_minute = int(self.start_timer3_minutes_entry.get())
        start3_seconds = int(self.start_timer3_seconds_entry.get())

        end3_hour = int(self.end_timer3_hours_entry.get())
        end3_minutes = int(self.end_timer3_minutes_entry.get())
        end3_seconds = int(self.end_timer3_seconds_entry.get())

        print("Timer set!!!!!!!!!!!!!!!!!!!!!!!1") #delete this line
        
       
