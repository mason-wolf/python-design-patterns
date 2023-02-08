from abc import ABC, abstractmethod

"""
Adapter is a structural design pattern which allows incompatible objects to collaborate.
The Adapter acts as a wrapper between two objects.
"""

class JsonInterface(ABC):

    @abstractmethod
    def get_data():
        pass

    @abstractmethod
    def get_type():
        pass

class XmlInterface(ABC):

    @abstractmethod
    def get_data():
        pass

    @abstractmethod
    def get_type():
        pass

class XmlData(XmlInterface):

    def get_data(self):
        print("some xml")
    
    def get_type(self):
        return "xml"

class XmlToJsonAdapter(JsonInterface):
    _xml = None

    def __init__(self, xml):
        self._xml = xml
    
    def get_data(self):
        print("converting xml to json")

    def get_type(self):
        return self._xml.get_type()

class DataService:
    _data = None
    
    def __init__(self, data):
        self._data = data
    
    def send(self):
            self._data.get_data()


xml = XmlData()
json_adapter = XmlToJsonAdapter(xml)
data_service = DataService(json_adapter)
data_service.send()

