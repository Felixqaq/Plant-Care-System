import tkinter as tk
from PIL import Image, ImageTk
import cv2
import random

#plant care system

class PCS:
    def __init__(self):
        # 創建主窗口
        self.root = tk.Tk()
        self.root.title("植物照顧系統")
        self.root.geometry("900x700")
        self.root.resizable(False, False)
        self.root.iconbitmap("plant.ico")  # 設置UI圖標

        # 創建一個濕度標籤
        self.create_humidity_label()

        # 創建一個溫度標籤
        self.create_temperature_label()

        #self.refresh_data()

        # 創建一個按鈕，當按下時觸發回調函數
        #self.button = tk.Button(self.root, text="刷新", command=self.refresh)
        #self.button.pack()

        # 創建菜單欄
        self.create_menu_bar()

        #顯示植物畫面
        self.video_text = tk.Label(self.root, text="植物畫面")
        self.video_text.pack()

        # 建立一個標籤來顯示相機畫面
        self.video_label = tk.Label(self.root)
        self.video_label.pack()

        # 使用 OpenCV 捕獲相機視訊
        self.cap = cv2.VideoCapture(0)

        # 開始更新畫面
        if not self.update_frame():
            # 創建圖片
            self.create_img()
        
    def refresh_data(self):
        # 讀取輸入框的內容
        temp = random.randint(0, 30)
        humi = random.randint(0, 100)
        # 將標籤的內容設置為輸入框中的內容
        self.humidity_data.config(text=str(humi)+"％RH")
        self.temperature_data.config(text=str(temp)+"˚C")
        self.root.after(1000, self.refresh_data)#定期刷新數字

    # 創建菜單欄
    def create_menu_bar(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        Mainmenu = tk.Menu(menubar, tearoff=0)  # 去除虛線
        Mainmenu.add_command(label="退出", command=self.quit_command)
        menubar.add_cascade(label="功能", menu=Mainmenu)

    # 創建圖片
    def create_img(self):
        # 新增圖片
        img = tk.PhotoImage(file="no_web_cam.png")
        self.imgtest = tk.Label(self.root, image=img)
        self.imgtest.image = img  # 避免圖片被垃圾回收
        self.imgtest.pack()

    def update_frame(self):
        ret, frame = self.cap.read()  # 讀取一幀相機畫面
        if ret:
            # 將 OpenCV 的 BGR 圖片轉換為 RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # 使用 PIL 來處理圖像
            img = Image.fromarray(frame_rgb)
            imgtk = ImageTk.PhotoImage(image=img)
            # 更新 Tkinter 標籤上的圖像
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)
        # 設定定時器，持續更新畫面
        self.video_label.after(10, self.update_frame)
        if ret:
            return True
        else:
            return False
        
    def create_humidity_label(self):
        self.humidity_label = tk.Label(self.root, text="濕度")
        self.humidity_label.pack()
        self.humidity_data = tk.Label(self.root, text="50％RH")
        self.humidity_data.pack()

    def create_temperature_label(self):
        self.temperature_label = tk.Label(self.root, text="溫度")
        self.temperature_label.pack()
        self.temperature_data = tk.Label(self.root, text="25˚C")
        self.temperature_data.pack()

    def quit_command(self):
        self.root.quit()

    # 啟動應用程式
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = PCS()
    app.run()
