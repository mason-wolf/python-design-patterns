"""
Singleton is a creational design pattern that lets you ensure that a 
class has only one instance, while providing a global access point to this instance.
"""

class Logger(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new instance")
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

log = Logger()
nextLog = Logger()

print("Same instance in use? ", log is nextLog)