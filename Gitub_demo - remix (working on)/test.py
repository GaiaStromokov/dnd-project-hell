vClass = "Fighter"
vSubclass = ""


class bClass():
    def __init__(self):
        self.Atr = {"STR": 0, "DEX": 0, "CON": 0}
        
        if vClass: cClass = globals()[vClass](self)
        if vClass: cClass = globals()[vClass](self)

    def __repr__(self):
        return str(self.__dict__)

class Fighter():
    def __init__(self, parent):
        parent.Atr["STR"] += 1
        
        
test = bClass()
print(test)