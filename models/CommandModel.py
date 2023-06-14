from abc import ABC, abstractmethod

class Command(ABC):
    
    def __init__(self, name):
        self.commandName = name

    @abstractmethod
    def RunThisCommand(self, command : dict) -> str:
        pass

    def GetCommandName(self):
        return self.commandName

# class DerivedClass(Command):
    
#     def abstract_method(self):
#         print("Implementation of abstract_method in DerivedClass")

# # Creating an instance of the derived class
# obj = DerivedClass()

# # Calling the abstract method
# obj.abstract_method()
