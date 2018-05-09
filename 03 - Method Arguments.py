

class SomeClassName:
    longName = False
    name = "dhadoo"
    def __init__ (self, name, longName = False, **kwargs):
        # kwargs = keywords argument    
        self.longName = longName
        self.name = name
        
        for key, value in kwargs.items():
            setattr(self, key, value)

    def BetterName(self, userThoughts):
        if (self.longName): 
            return False
        return True



stackObject = SomeClassName('Zeus', True)

# kwargs is kinda optional arguments
anotherStackObject = SomeClassName('John Wayne', True, ugly = True, fugly = "Hell Yeah, Ugly AF", dreadful = False)

print(f" The name passed is {stackObject.name}")
print(f"Guy named {anotherStackObject.name} is {anotherStackObject.fugly}")
# to be continued, the use of kwargs