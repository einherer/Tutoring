from abc import ABC, abstractmethod

# Parent Class
class Animal(ABC): # ABC to be able to use abstract methods
    def __init__(self, name, age, legs):
        self.name = name

        # raising errors for 1-linethings like checking datatypes
        assert type(age)==int , "wrong datatype"
        self.age = age

        if type(legs)==float:
            # raising and catching errors for multiple lines or functions called
            try:
                #put here what could cause an error
                raise ValueError("WHAT? Can you have half legs")
            except ValueError as err:
                # catch the error here and do what you like with it
                print(err, "but luckily we catched it")
        
        self.legs = legs


    @abstractmethod # this way we need to implement the folloing function in childclasses
    def communicate(self):
        pass    #just a placeholder for the childs.


# child classes
    
class Cat(Animal):
    def __init__(self, name, age, legs, color):
        super().__init__(name, age, legs)

        self.color = color

    def communicate(self):
        return "Moew  - I can see the bottom of my foodbowl"
    

cat_instance = Cat("Minka", 4, 4.5, "grey - tiger")

print(cat_instance.communicate())
print(cat_instance.__dict__)