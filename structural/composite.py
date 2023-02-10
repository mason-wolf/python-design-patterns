from abc import ABC, abstractmethod

"""
Composite is a structural design pattern that allows composing 
objects into a tree-like structure and work with the it as if it was a singular object.
"""
class IComponent(ABC):

    @abstractmethod
    def get_size(self):
        """returns size in mb"""

class File(IComponent):

    def __init__(self, name, size):
        self._name = name
        self._size = size
    
    def get_size(self):
        return self._size

class Folder(IComponent):

    def __init__(self, name, components):
        self._name = name
        self._components = components
    
    def get_size(self):
        total_size = 0
        for c in self._components:
            total_size += c.get_size()
        return total_size


file1 = File("data.pdf", 10)
file2 = File("taxes.xsl", 4)

files = []
files.append(file1)
files.append(file2)

photo = File("beach.png", 25)
photos = []
photos.append(photo)

folder1 = Folder("documents", files)
folder2 = Folder("pictures", photos)
folder1._components.append(folder2)

print(folder1.get_size())