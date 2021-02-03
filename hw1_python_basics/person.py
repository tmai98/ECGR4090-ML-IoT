class person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def new_person(self):
        #print("{:} is {:} years old.".format(self.name, self.age))
        #print(self.name)
        return(self.name)

    def __repr__(self):
        print("{:} is {:} years old and {:} cm tall".format(self.name, self.age, self.height))
        return (self.name)


#new_person = person(self.name=='Joe', self.age==34, self.height==184)

x = person('Joe', 34, 184)
y = person('Bob', 17, 182)


#x.new_person()
#y.__repr__()
