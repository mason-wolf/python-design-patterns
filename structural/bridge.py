from abc import ABC, abstractmethod

# Bridge is a structural design pattern that lets you split a large class 
# or a set of closely related classes into two separate hierarchies—abstraction 
# and implementation—which can be developed independently of each other.

# Operating System Abstraction Interface
class IOs(ABC):

    @staticmethod
    @abstractmethod
    def read():
        pass

# Os Implementer
class IOsClient(ABC):

    @staticmethod
    @abstractmethod
    def read_file():
        pass

class Linux(IOs):
    def __init__(self, implementor):
        self.implementer = implementor()
    
    def read(self):
        self.implementer.read_file()

class Windows(IOs):
    def __init__(self, implementor):
        self.implementer = implementor()
    
    def read(self):
        self.implementer.read_file()

class LinuxClient(IOsClient):
    def read_file(self):
        print("linux")

class WindowsClient(IOsClient):
    def read_file(self):
        print("windows")

windows = Windows(WindowsClient)
windows.read()

linux = Linux(LinuxClient)
linux.read()
