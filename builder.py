from abc import ABC, abstractmethod

"""
Builder pattern allows you to construct complex
objects step by step. The pattern allows you to 
produce different types and representations of an 
object using the same construction code.
"""
class Aircraft:

    def __init__(self):
        self.__wings = None
        self.__fuselage = None
        self.__engine = None

    def set_wings(self, wings):
        self.__wings = wings
    
    def set_fuselage(self, fuselage):
        self.__fuselage = fuselage
    
    def set_engine(self, engine):
        self.__engine = engine
    
    def get_aircraft_details(self):
        print(f"Wing Span: { self.__wings.length}, Engine: { self.__engine.engine_type }, Fuel Capacity: { self.__fuselage.fuel_capacity}")

class Wings:
    length = None

class Fuselage:
    fuel_capacity = None

class Engine:
    engine_type = None

class IBuilder(ABC):
    @abstractmethod
    def get_wings(self):
        "wings"

    @abstractmethod
    def get_fuselage(self):
        "fuselage"
    
    @abstractmethod
    def get_engine(self):
        "engine"

class FighterAircraftBuilder(IBuilder):

    def get_wings(self):
        wings = Wings()
        wings.length = 33
        return wings
    
    def get_fuselage(self):
        fuselage = Fuselage()
        fuselage.fuel_capacity = 450
        return fuselage
    
    def get_engine(self):
        engine = Engine()
        engine.engine_type = "F100-PW-229"
        return engine

class BomberAircraftBuilder(IBuilder):

    def get_engine(self):
        return super().get_engine()
    def get_fuselage(self):
        return super().get_fuselage()
    def get_wings(self):
        return super().get_wings()

class AircraftDirector:

    __builder = None

    def set_builder(self, builder):
        self.__builder = builder
    
    def get_aircraft(self):
        aircraft = Aircraft()

        wings = self.__builder.get_wings()
        aircraft.set_wings(wings)

        engine = self.__builder.get_engine()
        aircraft.set_engine(engine)

        fuselage = self.__builder.get_fuselage()
        aircraft.set_fuselage(fuselage)

        return aircraft

fighter_aircraft_builder = FighterAircraftBuilder()
bomber_aircraft_builder = BomberAircraftBuilder()

aircraft_director = AircraftDirector()

aircraft_director.set_builder(fighter_aircraft_builder)

fighter_aircraft = aircraft_director.get_aircraft()
fighter_aircraft.get_aircraft_details()

