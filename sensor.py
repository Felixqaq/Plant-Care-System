import RPi.GPIO as GPIO
import time
import adafruit_dht
from SensorInterface import SensorInterface 

class SensorReader(SensorInterface):
    def __init__(self):
        # 初始化 DHT11 溫濕度感測器
        self.dht_device = adafruit_dht.DHT11(board.D4)  # DHT11 連接到樹莓派的 GPIO 4

        # 初始化 GPIO 設定
        GPIO.setmode(GPIO.BCM)
        
        # 設定數位濕度感測器的 GPIO 針腳
        self.moisture_pin = 17  # GPIO 17
        GPIO.setup(self.moisture_pin, GPIO.IN)

        # 設定數位光線感測器的 GPIO 針腳
        self.light_pin = 27  # GPIO 27
        GPIO.setup(self.light_pin, GPIO.IN)

        # 設定數位聲音感測器的 GPIO 針腳
        self.sound_pin = 22  # GPIO 22
        GPIO.setup(self.sound_pin, GPIO.IN)

    def read_moisture(self):
        # 讀取數位濕度感測器的值
        return GPIO.input(self.moisture_pin)

    def read_light(self):
        # 讀取數位光線感測器的值
        return GPIO.input(self.light_pin)

    def read_sound(self):
        # 讀取數位聲音感測器的值
        return GPIO.input(self.sound_pin)

    def read_temperature(self):
        # 讀取溫度和濕度數值
        return self.dht_device.temperature

class LEDController:
    def __init__(self):
        # 初始化 LED 控制器
        self.led_pin = 18  # GPIO 18
        GPIO.setup(self.led_pin, GPIO.OUT)

    def set_color(self, color_values):
        # 控制 LED 顏色
        # 這裡假設你有一個特定的方法來控制 RGB LED
        pass

# 創建感測器讀取器和 LED 控制器對象
sensor_reader = SensorReader()
led_controller = LEDController()

# 顯示溫度
temperature = sensor_reader.read_temperature()
print("Temperature:", temperature)

# 進行感測器讀取並控制 LED
while True:
    soliMoistureValue = sensor_reader.read_moisture()
    lightValue = sensor_reader.read_light()
    soundValue = sensor_reader.read_sound()
    
    print('Moisture Value:', soliMoistureValue)
    print('Light Value:', lightValue)
    print('Sound Value:', soundValue)
    
    # 控制 LED
    led_controller.set_color([[255,255,51],[153,153,255],[255,255,0],[102,102,204],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]])

    # 添加延遲以避免太頻繁地讀取
    time.sleep(1)
