from DefaultSensor import DefaultSensor
import RPi.GPIO as GPIO

test = DefaultSensor()
class control:
        
    def LEDswitch(self):
        if test.read_light == False:
            return GPIO.output(22,GPIO.HIGH)
        else :
            return GPIO.output(22,GPIO.LOW)
