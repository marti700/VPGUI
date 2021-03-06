import tkinter as tk
from tkinter import ttk
import MainWindow as main_window

TITLE_FONT = ("ARIAL", 14)

class ConditionsWindow(tk.Frame):
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
        self.temperature_label = ttk.Label(self,text="Temperatura: t")

        temp_range_pane.add(trange_label)
        temp_range_pane.add(self.temperature_label)

        #Humidity information widgets
        hum_range_pane = tk.PanedWindow(self, orient="vertical", bg="black")
        hum_range_pane.grid(row=3, column=1)

        hrange_label = ttk.Label(self, text="Rango: min-max")
        self.humidity_label = ttk.Label(self,text="Humedad: h")

        hum_range_pane.add(hrange_label)
        hum_range_pane.add(self.humidity_label)

        #######Indicators code goes here#######
        #Temperature indicator
        temp_indicator_pane = tk.PanedWindow(self, bg="black", orient="vertical")
        temp_indicator_pane.grid(row=2, column=2)

        self.temp_indicator = tk.Canvas(self, width=30, height=100)
        #self.temp_indicator.create_rectangle(0, 0,150,100, fill="red", tag ="tempIndicator")

        temp_indicator_pane.add(self.temp_indicator)

        #Humidity Indicator
        hum_indicator_pane = tk.PanedWindow(self, bg="black", orient="vertical")
        hum_indicator_pane.grid(row=3, column=2,)

        self.hum_indicator = tk.Canvas(self, width=30, height=100)
        #hum_indicator.create_rectangle(0,0,150,100, fill="red")

        hum_indicator_pane.add(self.hum_indicator)

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

        rie_sis_label = tk.Label(self, text="Sistema de Riego:")
        self.rie_ind_label = ttk.Label(self,text="act/desc")

        rie_info_pane.add(rie_sis_label)
        rie_info_pane.add(self.rie_ind_label)

        #Lights system information widgetst
        lights_info_pane = ttk.PanedWindow(self, orient="vertical")
        lights_info_pane.grid(row=3, column=4)
        lights_info_pane.place(x=560, y=200)

        self.lights_ind_label = tk.Label(self, text="Luces: act/desc")

        lights_info_pane.add(self.lights_ind_label)

        #fans system information widgets
        fan_info_pane = ttk.PanedWindow(self, orient="vertical")
        fan_info_pane.grid(row=4, column=4)
        fan_info_pane.place(x=560, y=300)

        self.fan_ind_label = tk.Label(self, text="Ventiladores: act/desc")

        fan_info_pane.add(self.fan_ind_label)

        #curtain system information widgets
        cur_info_pane = ttk.PanedWindow(self, orient="vertical")
        cur_info_pane.grid(row=5, column=4)
        cur_info_pane.place(x=560, y=400)
        
        self.cur_ind_label = tk.Label(self, text="Cortinas: act/desc")

        cur_info_pane.add(self.cur_ind_label)

        #add others pane to the info pane 
        #info_pane.add(rie_info_pane)
        #info_pane.add(lights_info_pane)
        #info_pane.add(fan_info_pane)
        #info_pane.add(cur_info_pane)

        self.animate_temp_indicator() #call animation for Temperature indicator
        self.animate_hum_indicator()  #call animation for Humidity inidicator
    
    def animate_temp_indicator(self):
        print("Temperature: " + str(self.height)) 
        rect = self.temp_indicator.create_rectangle(0, self.height,150,100, tag ="tempIndicator") #!!!!!
        self.temp_indicator.move("tempIndicator", 0, self.height)
        #this line can be deleted this is used just to ilustrate how the indicator widget will behave
        self.after(300, self.animate_temp_indicator)

        #change label temperature text
        self.temperature_label.config(text = "Temperatura " + str(self.height) + "°C") #!!!!!!!!!
        
        self.temp_indicator.update()
        #controls indicator increase and decrease 
        #this is for animation prouporses and may 
        #not be necesary
        if self.height == 50 or self.height == 0:
            if self.temp_inc_dec:
                print(self.temp_inc_dec)
                self.temp_inc_dec  = False
            else:
                print(self.temp_inc_dec)
                self.temp_inc_dec  = True
        
        if self.temp_inc_dec:
            self.height += 2
        else:
            self.height -= 2

        #controls indicator colors
        #!!!!!!!!!!!!!!!!!!!!!!!!
        if self.height in range(0,17):
            self.temp_indicator.itemconfig(rect, fill="red")
        elif self.height in range(17,33):
            self.temp_indicator.itemconfig(rect, fill="green")
        elif self.height in range(33,51):
            self.temp_indicator.itemconfig(rect, fill="blue")
        
        
    def animate_hum_indicator(self):
        print("Humidity: "+ str(self.Hheight)) 
        rect = self.hum_indicator.create_rectangle(0, self.Hheight,150,100, tag ="tempIndicator") #!!!!!
        self.hum_indicator.move("tempIndicator", 0, self.Hheight)
        #this line can be deleted this is used just to ilustrate how the indicator widget will behave
        self.after(300, self.animate_hum_indicator)

        #change label temperature text
        self.humidity_label.config(text = "Humedad " + str(self.Hheight) + "°C") #!!!!!!!!!
        
        self.hum_indicator.update()
        #controls indicator increase and decrease 
        #this is for animation prouporses and may 
        #not be necesary
        if self.Hheight == 50 or self.Hheight == 0:
            if self.hum_inc_dec:
                print(self.hum_inc_dec)
                self.hum_inc_dec  = False
            else:
                print(self.hum_inc_dec)
                self.hum_inc_dec  = True
        
        if self.hum_inc_dec:
            self.Hheight += 2
        else:
            self.Hheight -= 2

        #controls indicator colors
        #!!!!!!!!!!!!!!!!!!!!!!!
        if self.Hheight in range(0,17):
            self.hum_indicator.itemconfig(rect, fill="red")
        elif self.Hheight in range(17,33):
            self.hum_indicator.itemconfig(rect, fill="green")
        elif self.Hheight in range(33,51):
            self.hum_indicator.itemconfig(rect, fill="blue")
    
    def set_lights_state(self, state, state_color=" "):
        # if state_color == " ": 
        #    state_color = self.cur_ind_label["bg"] 
        
        self.lights_ind_label.config(text=state, bg=state_color)

    def set_fan_state(self, state, state_color=" "):
         #if state_color == " ": 
         #   state_color = self.cur_ind_label["bg"]
        
        self.fan_ind_label.config(text=state, bg=state_color)

    def set_curtain_state(self, state, state_color=" "):
        #if  state_color == " ": 
        #    state_color = self.cur_ind_label["bg"]
        
        self.cur_ind_label.config(text=state, bg=state_color)

