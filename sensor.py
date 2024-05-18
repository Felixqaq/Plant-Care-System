import RPi.GPIO as GPIO
import time
import adafruit_dht
import board
from adafruit_htu21d import HTU21D

import board
from adafruit_htu21d import HTU21D

class SensorReader:
    def __init__(self):
        # 初始化溫濕度感測器
        i2c = board.I2C()
        self.sensor = HTU21D(i2c)

        # 初始化 GPIO 設定
        GPIO.setmode(GPIO.BCM)
        
        # 設定數位濕度感測器的 GPIO 針腳
        self.moisture_pin = 17  # GPIO 17
        GPIO.setup(self.moisture_pin, GPIO.IN)

        # 設定數位光線感測器的 GPIO 針腳
        self.light_pin = 27  # GPIO 27
        GPIO.setup(self.light_pin, GPIO.IN)

    def read_moisture(self):
        # 讀取數位濕度感測器的值
        return GPIO.input(self.moisture_pin)

    def read_light(self):
        # 讀取數位光線感測器的值
        return GPIO.input(self.light_pin)

    def read_temperature(self):
        # 讀取溫度數值
        return self.sensor.temperature
    def read_humidty(self):
        # 讀取溫度數值
        return self.sensor.relative_humidity
<<<<<<< HEAD
=======

>>>>>>> 384e3e7cdb527b71035dbaa7a81625a8c9f1a1d7

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
<<<<<<< HEAD
#led_controller = LEDController()
=======

#led_controller = LEDController()

>>>>>>> 384e3e7cdb527b71035dbaa7a81625a8c9f1a1d7

# 顯示溫度
temperature = sensor_reader.read_temperature()
print("Temperature:", temperature)

<<<<<<< HEAD
=======

>>>>>>> 384e3e7cdb527b71035dbaa7a81625a8c9f1a1d7
# 顯示濕度
humidty = sensor_reader.read_humidty()
print("humidty:", humidty)

# 進行感測器讀取並控制 LED
while True:
    
    # 顯示溫度
    temperature = sensor_reader.read_temperature()
    print("Temperature:", temperature)

    # 顯示濕度
    humidty = sensor_reader.read_humidty()
    print("humidty:", humidty)
    soliMoistureValue = sensor_reader.read_moisture()
    lightValue = sensor_reader.read_light()
    
    
    print('Moisture Value:', soliMoistureValue)
    print('Light Value:', lightValue)
    
    
    # 控制 LED
    #led_controller.set_color([[255,255,51],[153,153,255],[255,255,0],[102,102,204],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]])
<<<<<<< HEAD
=======

>>>>>>> 384e3e7cdb527b71035dbaa7a81625a8c9f1a1d7

    # 添加延遲以避免太頻繁地讀取
    time.sleep(1)
