from abc import ABC, abstractmethod

"""
Provides an interface for creating objects in a superclass,
but allows subclasses to alter the type of objects that will
be created.
"""
class Server(ABC):

    @abstractmethod
    def set_ip(self):
        pass

    @abstractmethod
    def get_ip(self):
        pass

class DNSServer(Server):

    ip = 0

    def __init__(self) -> None:
        super().__init__()
    
    def get_ip(self):
        print("DNS:", self.ip)
        return super().get_ip()
    
    def set_ip(self, ip):
        self.ip = ip

class MailServer(Server):

    ip = 0

    def __init__(self) -> None:
        super().__init__()
    
    def get_ip(self):
        print("SMTP:", self.ip)
        return super().get_ip()

    def set_ip(self, ip):
        self.ip = ip

class ServerFactory:

    def create_server(self, serverType, ip):
        if serverType == 'dns':
            dns_server = DNSServer()
            dns_server.set_ip(ip)
            dns_server.get_ip()
            return dns_server
        if serverType == 'mail':
            mail_server = MailServer()
            mail_server.set_ip(ip)
            mail_server.get_ip()
            return mail_server


server_factory = ServerFactory()
dns = server_factory.create_server("dns", "10.2.36.41")
mailServer = server_factory.create_server("mail", "201.86.56.23")



