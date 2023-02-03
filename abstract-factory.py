from abc import ABC, abstractmethod

"""
The abstract factory design pattern provides an interface
for creating families of related objects without specifying 
their concrete classes.
"""

class Device(ABC):

    ip_address = 0

    @abstractmethod
    def get_device_info(self):
        pass

    def set_ip_address(self, ip_address):
        self.ip_address = ip_address

    def get_ip_address(self):
        return self.ip_address

class Workstation(Device):

    CLASSIFICATION = ""

    def get_device_info(self):
        return "NODE IP:\t" + str(self.get_ip_address() + "\tCLASSIFICATION:\t" +  str(self.CLASSIFICATION))

"""
Abstract factory interface that declares methods
that return different abstract products which are
a family and related by a high-level concept.
"""
class DeviceFactory(ABC):
    @abstractmethod
    def create_device(self, ip_address) -> Device:
        pass

"""
Concrete factory that produces a family of products
that belong to a single variant.
"""
class UnclassifiedFactory(DeviceFactory):
    def create_device(self, ip_address):
        workstation = Workstation()
        workstation.CLASSIFICATION = "UNCLASSIFIED"
        workstation.set_ip_address(ip_address)
        return workstation

class ClassifiedFactory(DeviceFactory):
    def create_device(self, ip_address):
        workstation = Workstation()
        workstation.CLASSIFICATION = "CLASSIFIED"
        workstation.set_ip_address(ip_address)
        return workstation

unclass_factory = UnclassifiedFactory()
classified_workstation = ClassifiedFactory()

unclass_workstation = unclass_factory.create_device("184.12.9.12")
classified_workstation = classified_workstation.create_device("210.86.5.1")

print(unclass_workstation.get_device_info())
print(classified_workstation.get_device_info())