from abc import ABC, abstractmethod

# 定义一个抽象基类 Animal，使用 ABC
class SensorInterface(ABC):
    def __init__(self, name):
        self.name = name
    
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