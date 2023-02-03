from abc import ABC, abstractmethod
import copy

"""
Prototype is a creational design pattern that lets you copy
existing objects without making your code dependent on their classes.
Below we're creating a baseline security configuration prototype
and spinning up different instances of an 'app'.
"""
class SecurityConfig(ABC):

    def __init__(self):
        self.version = 1
        self.connection = "API_SECURITY_URL"
        self.environment = "DEV"
        self.port = 0

    @abstractmethod
    def get_config(self):
        pass
    
    def clone(self):
        return copy.copy(self)

class Config(SecurityConfig):

    def __init__(self):
        super().__init__()

    def get_config(self):
        print("***************************************")
        print("Version:", self.version)
        print("Connection:", self.connection)
        print("Port:", self.port)
        print("Environment:", self.environment)

class App:
    config = Config()

    def run(self):
        print("App running with " + self.config.environment + " config.")


app = App()

app.config = Config()
app.run()
print("Default Configuration")
app.config.get_config()

# Clone default configurations into new environments.
app_test = App()
app_test.config = app.config.clone()
app_test.config.connection = "10.50.681.12"
app_test.config.port = 80
app_test.config.environment = "TEST"
app_test.config.get_config()
app_test.run()

app_prod = App()
app_prod.config = app.config.clone()
app_prod.config.connection = "10.50.681.10"
app_prod.config.port = 8080
app_prod.config.environment = "PROD"
app_prod.config.get_config()
app_prod.run()



    