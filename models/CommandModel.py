from abc import ABC, abstractmethod

class Command(ABC):
    
    @abstractmethod
    def RunThisCommand(command : dict) -> str:
        pass

# class DerivedClass(Command):
    
#     def abstract_method(self):
#         print("Implementation of abstract_method in DerivedClass")

# # Creating an instance of the derived class
# obj = DerivedClass()

# # Calling the abstract method
# obj.abstract_method()
