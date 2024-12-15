import re


class Car:
    def __init__(self,model,year,plate,color):
        self.model=model
        self.year=year
        self.plate=plate
        self.color=color
    def __str__(self):
        return str(self.__dict__)
    @property
    def model(self):
        return self._model
    @model.setter
    def model(self,value):
        if re.match(r"\w[a_zA_Z]\d{10}"):
            self._model=value
        else:
            raise ValueError("Invalid Model")
    @property
    def year(self):
        return self._year
    @year.setter
    def year(self,value):
        if value>=2005:
            self._year=value
        else:
            raise ValueError("Invalid Year")
    @property
    def plate(self):
        return self._plate
    @plate.setter
    def plate(self,value):
        if re.match(r"\d{2}\w\d{3}"):
            self._plate=value
        else:
            raise ValueError("Invalid Plate")
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,value):
        if value=="white" or value=="blue" or value=="green" or value=="yellow" or value=="red":
            self._color=value
        else:
            raise ValueError("Invalid Color")


