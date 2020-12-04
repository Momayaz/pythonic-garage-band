
from abc import ABC, abstractmethod
class Band:
    all = []
    def __init__(self,name,members):
        self.name=name
        self.members=members
        self.all.append(self)

    def play_solos(self,name):
        pass

    def __str__(self):
        return """string with the "name" of the obj instance"""


    def __repr__(self):
        return f"'name':{self.name},'members' :{self.members}"

    @classmethod
    def to_list(cls):
        """Returns all Band instances that were created"""
        return cls.all

###########################################

class Musician():

    def __init__(self, name):
        self.name = name
  
    # It's better to have __str__ for every sub class
    def __str__(self):
        return self.name

    def __repr__(self):
        # This method will be called if we call the class instance from the command line
        return f"you look at '{self.name}' "

    # def get_instrument(self):
    #     return self.instrument
    
    # def play_solo(self):
    #     pass

###########################################

class Guitarist(Musician):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"my name is '{self.name}', i'm a Musician"

    def __repr__(self):
        return f"Guitariest:{self.name} "

    def get_instrument(self):
        return f"Guitar"

    def play_solo(self):
        return f"some guitar sound"

###########################################

class Bassist(Musician): 
    def __init__(self, name):
        self.name = name 

    def __str__(self):
        return f"my name is '{self.name}', i'm a Musician"

    def __repr__(self):
        return f"Bassist:{self.name} "

    def get_instrument(self):
        return f"Bassist"

    def play_solo(self):
        return f"some Bassist sound"

###########################################

class Drummer(Musician):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"my name is '{self.name}', i'm a Musician"

    def __repr__(self):
        return f"Drummer:{self.name} "

    def get_instrument(self):
        return f"Drums"

    def play_solo(self):
        return f"some Drums sound"

###########################################

if __name__ == "__main__":
    shela =Guitarist("ahmad SH")
    print(shela.name)
    print(shela.play_solo())
    print(shela.get_instrument())
    emadooov = Bassist("emad Z3")
    print(emadooov.name)
    print(emadooov.play_solo())
    print(emadooov.get_instrument())
    jhon = Drummer("jhon")
    print(jhon.name)
    print(jhon.play_solo())
    print(jhon.get_instrument())
    band1 = (Band("funny band", [jhon, shela, emadooov]))
    for member in band1.members:
        print("Name: ", member.name)
        print("Member: ", member)
    print(band1.all)
