# python allows you to inherit from multiple super/base classes 
import random

class Character:
    
    name = "none"
    weirdChar = True
    weirdName = "Syatama Katomatko"
    def __init__ (self, name, kwargs):
        self.name = name
        for key, value in kwargs.items():
            setattr(self, key, value)


class Name(Character):
    
    longName = True

    def __init__ (self, name, longName = True, **kwargs):
        self.name = name
        for key, value in kwargs.items():
            setattr(self, key, value)

    def IslongName(self):
        return self.longName and bool(random.randint(0, 1))

    def PrintStuff(self):
        print(f"Character inherited is {self.weirdChar} and his name is long({self.weirdName}).")


stackObject = Name("Bean", False)
stackObject.PrintStuff()