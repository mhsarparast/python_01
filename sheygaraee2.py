class jihadi_group:
    def __init__(self, name,leader, ideology,slogan,place):
        self.name = name
        self.leader = leader
        self.ideology = ideology
        self.slogan = slogan
        self.place = place
    def save(self):
        print(self.slogan)
        print(self.name,"is victorios")

name=input("enter The name: ")
leader=input("enter The leader: ")
ideology=input("enter The ideology: ")
slogan=input("enter The slogan: ")
place=input("enter The place: ")
jihadi_group1=jihadi_group(name,leader,ideology,slogan,place)
jihadi_group1.save()
print(jihadi_group1.__dict__)

name=input("enter The name: ")
leader=input("enter The leader: ")
ideology=input("enter The ideology: ")
slogan=input("enter The slogan: ")
place=input("enter The place: ")
jihadi_group2=jihadi_group(name,leader,ideology,slogan,place)
jihadi_group2.save()
print(jihadi_group2.__dict__)

name=input("enter The name: ")
leader=input("enter The leader: ")
ideology=input("enter The ideology: ")
slogan=input("enter The slogan: ")
place=input("enter The place: ")
jihadi_group3=jihadi_group(name,leader,ideology,slogan,place)
jihadi_group3.save()
print(jihadi_group3.__dict__)

name=input("enter The name: ")
leader=input("enter The leader: ")
ideology=input("enter The ideology: ")
slogan=input("enter The slogan: ")
place=input("enter The place: ")
jihadi_group4=jihadi_group(name,leader,ideology,slogan,place)
jihadi_group4.save()
print(jihadi_group4.__dict__)

name=input("enter The name: ")
leader=input("enter The leader: ")
ideology=input("enter The ideology: ")
slogan=input("enter The slogan: ")
place=input("enter The place: ")
jihadi_group5=jihadi_group(name,leader,ideology,slogan,place)
jihadi_group5.save()
print(jihadi_group5.__dict__)

name=input("enter The name: ")
leader=input("enter The leader: ")
ideology=input("enter The ideology: ")
slogan=input("enter The slogan: ")
place=input("enter The place: ")
jihadi_group6=jihadi_group(name,leader,ideology,slogan,place)
jihadi_group6.save()
print(jihadi_group6.__dict__)