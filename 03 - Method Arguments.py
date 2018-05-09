

class SomeClassName:
    longName = False
    name = "dhadoo"
    def __init__ (self, name, longName = False, **kwargs):
        # kwargs = keywords argument    
        self.longName = longName
        self.name = name

    def BetterName(self, userThoughts):
        if (self.longName): 
            return False
        return True



stackObject = SomeClassName('Zeus', True)
print(f" The name passed is {stackObject.name}")