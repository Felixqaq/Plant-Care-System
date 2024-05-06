import ssd1306
from machine import I2C
from machine import *
from htu21d import HTU21D

from machine import Pin,ADC
import utime
from machine import Switch
from machine import LED,udelay

#123

class sensorReader:
   def __init__(self):
      self.adc0 = ADC(Pin.epy.AIN0)
      self.adc1 = ADC(Pin.epy.AIN1)
      self.adc3 = ADC(Pin.epy.AIN3)
   def read_moisture(self):
      return self.read_adc(self,adc0)
   
   def read_light(self):
      return self.read_adc(self,adc1)
   
   def read_sound(self):
      return self.read_adc(self,adc3)
   
   def read_adc(self,ch):
      data = ch.read()
      utime.sleep_ms(10)
      return data
   
class LEDcontroller:
   def __init__(self) :
      self.ledRgb = LED(LED.RGB)
   
   def set_color(self,color_values):
      self.ledRgb.rgb_write(color_values)

sensor_reader = sensorReader()
led_controller = LEDcontroller()

i2c = I2C(0,I2C.MASTER)
oled=ssd1306.SSD1306_I2C(128, 64, i2c)
i2c0 = I2C(0,I2C.MASTER,baudrate=100000)
sensor = HTU21D(i2c0)
oled.text((str(sensor.readTemperatureData()) + ''),0,0,1)
oled.show()
while True:
  soliMoistureValue = sensorReader.read_moisture()
  lightValue = sensorReader.read_light()
  soundValue = sensorReader.read_sound()
  print('Moisture Value:' + str(soliMoistureValue))
  print('Light Value:' + str(lightValue))
  print('Sound Value:' + str(soundValue))
  if (KeyA.value()) == True:
    break

  ledRgb.lightness(20)
  write_led_file('ledRgb.rgb_write(([[255,255,51],[153,153,255],[255,255,0],[102,102,204],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]))')
