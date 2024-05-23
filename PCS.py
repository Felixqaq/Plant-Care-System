import tkinter as tk
from PIL import Image, ImageTk
import cv2
import random
from DefaultSensor import DefaultSensor
from SensorDataPlot import SensorDatatPlot
from control import control
# from sensor import SensorReader

UPDATE_TIME = 1000
VIDEO_UPDATE_TIME = 10
IMG_SIZE = (50, 50)
VIDEO_SIZE = (200, 200)

class PCS:
    def __init__(self):
        # 創建主窗口
        self.root = tk.Tk()
        self.root.title("植物照顧系統")
        self.root.geometry("675x600")
        self.root.resizable(True, True)
        self.root.iconphoto(False, tk.PhotoImage(file='./image/plant.png'))# 設置UI圖標

        self.sensor = DefaultSensor()
        self.control = control()

        self.create_humidity_label()
        self.create_temperature_label()
        self.create_light_label()
        self.create_moisture_label()
        self.create_button()
        self.create_menu_bar()

        # 顯示植物畫面
        self.video_text = tk.Label(self.root, text="植物畫面")
        self.video_text.grid(row=0, column=0)
        self.video_label = tk.Label(self.root)
        self.video_label.grid(row=1, column=0)

        self.cap = cv2.VideoCapture(0)

        self.data_plot = SensorDatatPlot(self.root)
        
        # 開始更新畫面
        if not self.update_frame():
            self.create_img()

        self.update()

    def update(self):
        temp = self.sensor.read_temperature()
        humi = self.sensor.read_moisture()
        self.humidity_data.config(text=str(humi)+"％RH")
        self.temperature_data.config(text=str(temp)+"˚C")

        if self.sensor.read_light() == 0:
            self.light_label.config(image=self.light_dark_image)
        else:
            self.light_label.config(image=self.light_bright_image)

        if self.sensor.read_moisture() == 0:
            self.moisture_label.config(image=self.moisture_dry_image)
        else:
            self.moisture_label.config(image=self.moisture_wet_image)
        self.control.update()
        self.data_plot.update_data(temp, humi)
        self.root.after(UPDATE_TIME, self.update)#定期刷新

    def create_menu_bar(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        Mainmenu = tk.Menu(menubar, tearoff=0)  # 去除虛線
        Mainmenu.add_command(label="退出", command=self.quit_command)
        menubar.add_cascade(label="功能", menu=Mainmenu)
    
    def create_img(self):
        img = tk.PhotoImage(file="./image/no_web_cam.png")
        self.imgtest = tk.Label(self.root, image=img)
        self.imgtest.image = img  # 避免圖片被垃圾回收
        self.imgtest.grid(row=1, column=0)

    def update_frame(self):
        ret, frame = self.cap.read() 
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb).resize(VIDEO_SIZE)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)
        # 設定定時器，持續更新畫面
        self.video_label.after(VIDEO_UPDATE_TIME, self.update_frame)
        if ret:
            return True
        else:
            return False
        
    def create_humidity_label(self):
        image = Image.open('./image/hum.png').resize(IMG_SIZE)
        self.humidity_image = ImageTk.PhotoImage(image)
        self.humidity_label = tk.Label(self.root, image=self.humidity_image)
        self.humidity_label.grid(row=0, column=1)
        self.humidity_data = tk.Label(self.root, text="{}％RH".format(self.sensor.read_moisture()))
        self.humidity_data.grid(row=1, column=1)

    def create_temperature_label(self):
        image = Image.open('./image/temp.png').resize(IMG_SIZE)
        self.temperature_image = ImageTk.PhotoImage(image)
        self.temperature_label = tk.Label(self.root, image=self.temperature_image)
        self.temperature_label.grid(row=0, column=2)
        self.temperature_data = tk.Label(self.root, text="{}˚C".format(self.sensor.read_temperature()))
        self.temperature_data.grid(row=1, column=2)
    
    def create_light_label(self):
        image = Image.open('./image/bright.png').resize(IMG_SIZE)
        self.light_bright_image = ImageTk.PhotoImage(image)
        image = Image.open('./image/dark.png').resize(IMG_SIZE)
        self.light_dark_image = ImageTk.PhotoImage(image)
        self.light_label = tk.Label(self.root, image=self.light_bright_image)
        self.light_label.grid(row=0, column=3)

    def create_moisture_label(self):
        image = Image.open('./image/wet.png').resize(IMG_SIZE)
        self.moisture_wet_image = ImageTk.PhotoImage(image)
        image = Image.open('./image/dry.png').resize(IMG_SIZE)
        self.moisture_dry_image = ImageTk.PhotoImage(image)
        self.moisture_label = tk.Label(self.root, image=self.moisture_wet_image)
        self.moisture_label.grid(row=1, column=3)

    def create_button(self):
        self.on_button = tk.Button(self.root, text="On")
        self.on_button.grid(row=2, column=1)
        self.off_button = tk.Button(self.root, text="Off")
        # self.off_button = tk.Button(self.root, text="Off", command=self.update_temperature_label)
        self.off_button.grid(row=2, column=2)

    def quit_command(self):
        self.root.quit()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = PCS()
    app.run()
