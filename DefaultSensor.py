from SensorInterface import SensorInterface
import random

class DefaultSensor(SensorInterface):
    def __init__(self):
        pass

    def read_moisture(self):
        return random.randint(0, 1)

    def read_light(self):
        return random.randint(0, 1)

    def read_sound(self):
        return random.randint(1, 100)
    
    def read_temperature(self):
        return random.randint(10, 40)