import tkinter as tk
from PIL import Image, ImageTk
import cv2
import random
from DefaultSensor import DefaultSensor
from SensorDatatPlot import SensorDatatPlot

UPDATE_TIME = 1000
VIDEO_UPDATE_TIME = 10
class PCS:
    def __init__(self):
        # 創建主窗口
        self.root = tk.Tk()
        self.root.title("植物照顧系統")
        self.root.geometry("900x700")
        self.root.resizable(False, False)
        self.root.iconbitmap("plant.ico") # 設置UI圖標

        # 创建一个垂直滚动条
        self.scrollbar = tk.Scrollbar(self.root, command=self.on_scroll())
        self.scrollbar.pack(side="right", fill="y")
        
        self.sensor = DefaultSensor()
        self.data_plot = SensorDatatPlot(self.root)

        self.create_humidity_label()
        self.create_temperature_label()

        # 創建一個按鈕，當按下時觸發回調函數
        #self.button = tk.Button(self.root, text="刷新", command=self.refresh)
        #self.button.pack()

        
        
        self.create_menu_bar()

        #顯示植物畫面
        self.video_text = tk.Label(self.root, text="植物畫面")
        self.video_text.pack()

        # 建立一個標籤來顯示相機畫面
        self.video_label = tk.Label(self.root)
        self.video_label.pack()

        self.cap = cv2.VideoCapture(0)

        
        
        # 開始更新畫面
        if not self.update_frame():
            self.create_img()

        self.update()

    def update(self):
        # 讀取輸入框的內容
        temp = self.sensor.read_temperature()
        humi = self.sensor.read_moisture()
        # 將標籤的內容設置為輸入框中的內容
        self.humidity_data.config(text=str(humi)+"％RH")
        self.temperature_data.config(text=str(temp)+"˚C")
        self.data_plot.update_data(temp, humi)
        self.root.after(UPDATE_TIME, self.update)#定期刷新數字

    # 創建菜單欄
    def create_menu_bar(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        Mainmenu = tk.Menu(menubar, tearoff=0)  # 去除虛線
        Mainmenu.add_command(label="退出", command=self.quit_command)
        menubar.add_cascade(label="功能", menu=Mainmenu)

    def create_img(self):
        # 新增圖片
        img = tk.PhotoImage(file="no_web_cam.png")
        self.imgtest = tk.Label(self.root, image=img)
        self.imgtest.image = img  # 避免圖片被垃圾回收
        self.imgtest.pack()

    def update_frame(self):
        ret, frame = self.cap.read() 
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
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
        self.humidity_label = tk.Label(self.root, text="濕度")
        self.humidity_label.pack()
        self.humidity_label.config(yscrollcommand=self.scrollbar.set)
        self.humidity_data = tk.Label(self.root, text="{}％RH".format(self.sensor.read_moisture()))
        self.humidity_data.pack()
        self.humidity_data.config(yscrollcommand=self.scrollbar.set)

    def create_temperature_label(self):
        self.temperature_label = tk.Label(self.root, text="溫度")
        self.temperature_label.pack()
        self.temperature_data = tk.Label(self.root, text="{}˚C".format(self.sensor.read_temperature()))
        self.temperature_data.pack()

    def on_scroll(self, *args):
    # 通过yview来使文本框或列表框滚动
        self.text_box.yview(*args)

    def quit_command(self):
        self.root.quit()

    # 啟動應用程式
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = PCS()
    app.run()
