from DefaultSensor import DefaultSensor
import RPi.GPIO as GPIO

class control:
    def __init__(self) :
        self.sensor = DefaultSensor()
    def LEDswitch(self):
        if self.sensor.read_light == False:
            return GPIO.output(22,GPIO.HIGH)
        else :
            return GPIO.output(22,GPIO.LOW)
