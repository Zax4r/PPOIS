import abc

class InputI(abc.ABC):
    
    @abc.abstractmethod
    def input(self):
        pass