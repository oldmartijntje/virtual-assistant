from abc import ABC, abstractmethod
import models.CommandModel as CommandModel

class Library(ABC):
    
    @abstractmethod
    def GetCommands() -> list[CommandModel.Command]:
        pass

# class DerivedClass(AbstractClass):
    
#     def abstract_method(self):
#         print("Implementation of abstract_method in DerivedClass")

# # Creating an instance of the derived class
# obj = DerivedClass()

# # Calling the abstract method
# obj.abstract_method()