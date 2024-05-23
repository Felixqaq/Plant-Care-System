import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
from datetime import datetime
import matplotlib.dates as mdates

class SensorDatatPlot:
    def __init__(self, root):
        self.root = root

        self.temperature_data = []
        self.humidity_data = []
        self.time_data = []


        # 创建Matplotlib图表
        self.fig = Figure(figsize=(5, 3), dpi=100)

        # 温度子图
        self.ax_temp = self.fig.add_subplot(211)
        self.line_temp, = self.ax_temp.plot(self.temperature_data, marker='o', color='r')
        self.ax_temp.set_title("Temperature Monitor")
        self.ax_temp.set_ylabel("Temperature (°C)")
        self.ax_temp.grid(True)
        self.ax_temp.xaxis.set_major_formatter(mdates.DateFormatter('%M:%S'))

        # 增加間距
        self.fig.subplots_adjust(hspace=0.6)

        # 湿度子图
        self.ax_hum = self.fig.add_subplot(212)
        self.line_hum, = self.ax_hum.plot(self.humidity_data, marker='o', color='b')
        self.ax_hum.set_title("Humidity Monitor")
        self.ax_hum.set_ylabel("Humidity (%)")
        self.ax_hum.grid(True)
        self.ax_hum.xaxis.set_major_formatter(mdates.DateFormatter('%M:%S'))
        
        # 创建画布并嵌入到Tkinter窗口中
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().grid(row=2, column=0)



    def update_data(self, temp_value, hum_value):
        # 模拟实时数据更新
        new_time = datetime.now()
        self.temperature_data.append(temp_value)
        self.humidity_data.append(hum_value)
        self.time_data.append(new_time)

        if len(self.temperature_data) > 10:
            self.temperature_data.pop(0)
            self.humidity_data.pop(0)
            self.time_data.pop(0)

        # 更新折线图
        self.line_temp.set_ydata(self.temperature_data)
        self.line_temp.set_xdata(self.time_data)
        self.ax_temp.relim()
        self.ax_temp.autoscale_view()

        self.line_hum.set_ydata(self.humidity_data)
        self.line_hum.set_xdata(self.time_data)
        self.ax_hum.relim()
        self.ax_hum.autoscale_view()

        self.canvas.draw()
