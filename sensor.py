import RPi.GPIO as GPIO
import time
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
        return int(self.sensor.temperature)
    def read_humidty(self):
        # 讀取溫度數值
        return int(self.sensor.relative_humidity)

# 創建感測器讀取器對象
sensor_reader = SensorReader()


# 顯示溫度
# temperature = sensor_reader.read_temperature()
# print("Temperature:", temperature)

# # 顯示濕度
# humidty = sensor_reader.read_humidty()
# print("humidty:", humidty)

# # 進行感測器讀取
# while True:
    
#     # 顯示溫度
#     temperature = sensor_reader.read_temperature()
#     print("Temperature:", temperature)

#     # 顯示濕度
#     humidty = sensor_reader.read_humidty()
#     print("humidty:", humidty)
#     soliMoistureValue = sensor_reader.read_moisture()
#     lightValue = sensor_reader.read_light()
    
    
#     #print('Moisture Value:', soliMoistureValue)
#     print('Light Value:', lightValue)
    
#     time.sleep(1)
