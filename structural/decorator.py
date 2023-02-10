from abc import ABC, abstractmethod

""" 
Decorator is a structural pattern that allows adding new behaviors 
to objects dynamically by placing them inside special wrapper objects, called decorators. 
"""

class IMessage(ABC):
    @staticmethod
    @abstractmethod
    def get_message():
        pass 

class Notification(IMessage):

    def __init__(self, message):
        self._message = message

    def get_message(self):
        return self._message
    
    def send(self):
        print("\n**** Notification ****")
        print("sending message")
        
# Decorator class
class Broadcast(IMessage):

    def __init__(self, notification):
        self._notification = notification

    def get_message(self):
        print(self._notification)
    
    def send(self):
        print("\n**** Broadcast ****")
        print("sending email: ", self._notification.get_message())
        print("sending SMS: ", self._notification.get_message())
        print("sending alert: ", self._notification.get_message())

notification = Notification("testing, testing")
# send via one source
notification.send()

# sending same message via multiple sources
Broadcast(notification).send()


# Alternative pythonic approach
def broadcast(function):
    def wrapper():
        function()
        print("sending email")
        print("sending SMS")
        print("sending alert")
    return wrapper

@broadcast
def send():
    print("\n\ntesting, testing")

# send()

# Decorator with custom arguments.
# Will fire before inner function is executed.
def custom_alert(**kwargs):
    def contents(function):
        print("\n", kwargs['alert_type'])
        function()
        return function
    return contents

@custom_alert(alert_type = "WARNING, WARNING")
def alert():
    print("something bad is happening")

        