import abc

class MovingI(abc.ABC):
    
    @abc.abstractmethod
    def move(self,dt):
        pass