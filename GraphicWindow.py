import tkinter as tk
from tkinter import ttk
import MainWindow as main_window

TITLE_FONT = ("ARIAL", 14)

class GraphicWindow(tk.Frame):
    temperature = []
    temp_max = 50;
    time = []
    time_max = 1000; #in miliseconds
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #layout stuff see: http://effbot.org/tkinterbook/grid.htm#Tkinter.Grid.grid_rowconfigure-method
        #and also see: http://effbot.org/tkinterbook/grid.htm#Tkinter.Grid.grid_columnconfigure-method 
        #I had to apply a grid on self (which is the frame) so i can call grid_rowconfigure and grid_columnconfigure
        #because this methods only work in the parent widget that uses a grid to manage the layout`
        #self.grid(row=0, column=0, sticky="nsew")
        #self.grid_rowconfigure(2, minsize=200)
        #self.grid_rowconfigure(3, weight=1)
        #self.grid_columnconfigure(1, minsize=200)

        #The back button
        back_button = tk.Button(self, text="Atras",
                command = lambda: controller.show_frame(main_window.MainWindow))
        back_button.grid(row=0, column=0)
               
        #Title Label Pane

        tit_label_pane = ttk.PanedWindow(self, orient="horizontal")
        tit_label_pane.grid(row=1, column=1, sticky="w")
        
        #the Main label
        label = tk.Label(self, text="                                             Grafica de Tendencias", font=TITLE_FONT)

        tit_label_pane.add(label)

        #graph canvas
        self.graph_canvas = tk.Canvas(self, width=600, height=400, bg="grey")
        self.graph_canvas.grid(row=2, column=1)
        #self.draw_graph(GraphicWindow.temperature, GraphicWindow.time)
        self.get_temperature()
        self.get_time()
 
    def draw_graph(self, temperature, time):
        j = 0;
        for i in GraphicWindow.time:
            self.graph_canvas.create_text(int(600-(GraphicWindow.time[j]*(600/GraphicWindow.time_max))), 400-temperature[j], text="*", fill="red")
            j += 1
            print(j)

    def get_time(self):
        GraphicWindow.time_max += 1000
        GraphicWindow.time.append(GraphicWindow.time_max)
        self.after(1000, self.get_time) 
    
    def get_temperature(self):
        #here read the temperature from the sensor and add it to the temperature list
        #this code is ilustrative and should be replaced. Instead read the temperature from the sensor and save it to GraphicWindow.temperature
        for temp in range(0,2001):
            if temp > 20 and temp % 2 == 0:
                GraphicWindow.temperature.append(temp - 7)
            elif temp > 20 and temp % 2 != 0:
                GraphicWindow.temperature.append(temp - 4)

        #self.after(1000, get_temperature)
