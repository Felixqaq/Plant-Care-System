import tkinter as tk
from PIL import Image, ImageTk
import cv2


#plant care system

class PCS:
    def __init__(self):
        # 創建主窗口
        self.root = tk.Tk()
        self.root.title("植物照顧系統")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        self.root.iconbitmap("plant.ico")  # 設置窗口圖標

        # 創建一個標籤
        self.label = tk.Label(self.root, text="Hello, World!")
        self.label.pack()

        # 創建一個輸入框
        self.entry = tk.Entry(self.root)
        self.entry.pack()

        # 創建一個按鈕，當按下時觸發回調函數
        self.button = tk.Button(self.root, text="按我", command=self.on_button_click)
        self.button.pack()

        # 創建菜單欄
        self.create_menu_bar()

        # 創建圖片
        self.create_img()

        #顯示植物畫面
        self.video_text = tk.Label(self.root, text="植物畫面")
        self.video_text.pack()

        # 建立一個標籤來顯示相機畫面
        self.video_label = tk.Label(self.root)
        self.video_label.pack()

        # 使用 OpenCV 捕獲相機視訊
        self.cap = cv2.VideoCapture(0)

        # 開始更新畫面
        self.update_frame()


    # 按下按鈕時的回調函數
    def on_button_click(self):
        # 讀取輸入框的內容
        user_input = self.entry.get()
        # 將標籤的內容設置為輸入框中的內容
        self.label.config(text=user_input)
        print("success")

    # 創建菜單欄
    def create_menu_bar(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        Mainmenu = tk.Menu(menubar, tearoff=0)  # 去除虛線
        # Mainmenu.add_command(label="開啟")
        # Mainmenu.add_command(label="儲存")
        # Mainmenu.add_command(label="另存")
        Mainmenu.add_command(label="退出", command=self.quit_command)
        menubar.add_cascade(label="功能", menu=Mainmenu)

    # 創建圖片
    def create_img(self):
        # 新增圖片
        img = tk.PhotoImage(file="unicorn.png")
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

    def quit_command(self):
        self.root.quit()

    # 啟動應用程式
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = PCS()
    app.run()
