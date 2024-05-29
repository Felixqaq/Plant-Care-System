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
    def LEDswitch(self):
        if self.sensor.read_light() == 0:            
            return GPIO.output(led_pin,GPIO.HIGH)
        else :
            return GPIO.output(led_pin,GPIO.LOW)
    def set_angle(self,angle):
        duty = 2 + (angle / 18)  # 將角度轉換為占空比
        GPIO.output(servo_pin, True)
        pwm.ChangeDutyCycle(duty)
        time.sleep(1)
        GPIO.output(servo_pin, False)
        pwm.ChangeDutyCycle(0)


    def update(self):
        self.set_angle(50)
        self.LEDswitch()
        return
    

