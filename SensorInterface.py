from abc import ABC, abstractmethod

class SensorInterface(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def read_moisture(self):
        pass

    @abstractmethod
    def read_light(self):
        pass

    @abstractmethod
    def read_sound(self):
        pass
    
    @abstractmethod 
    def read_temperature(self):
        pass