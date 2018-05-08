import random


class Name:
    lengthyName = True
    goodName = True

    def GoodGuy(self):
        if self.goodName:
            return bool(random.randint(0, 1))
        return False

stackObject = Name()

# Name.GoodGuy(stackObject) 
# stackObject.GoodGuy()