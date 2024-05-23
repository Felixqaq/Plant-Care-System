from DefaultSensor import DefaultSensor
import RPi.GPIO as GPIO

class control:
    def __init__(self) :
        self.sensor = DefaultSensor()
    def LEDswitch(self):
        if self.sensor.read_light == 2:
            return GPIO.output(22,GPIO.HIGH)
        else :
            return GPIO.output(22,GPIO.LOW)
    def update(self):
        return self.LEDswitch()