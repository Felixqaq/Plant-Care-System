#from DefaultSensor import DefaultSensor
from sensor import SensorReader
import time
import RPi.GPIO as GPIO

led_pin = 26
servo_pin = 16

GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.output(led_pin, GPIO.LOW)

GPIO.setmode(GPIO.BCM) 

pwm = GPIO.PWM(servo_pin, 50)  # 50Hz
pwm.start(0)
class control:
    def __init__(self) :
        self.sensor = SensorReader()
        self.set_angle(0)
    def LEDswitch(self):
        if self.sensor.read_light() == 0:            
            return GPIO.output(led_pin,GPIO.HIGH)
        else :
            return GPIO.output(led_pin,GPIO.LOW)
    def set_angle(self, angle):
        duty = 2 + (angle / 18)  # 将角度转换为占空比
        pwm.ChangeDutyCycle(duty)



    def update(self):
        #self.set_angle(50)
        self.LEDswitch()
        return
    


