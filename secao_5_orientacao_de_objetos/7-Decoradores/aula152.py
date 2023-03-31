# Funçao decoradora e decoradore de classes

def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'Este é o repr{class_name} ({class_dict})'
        return class_repr

def my_str(self):
        class_dict = self.__dict__
        class_repr = f'Esta é a string{class_dict})'
        return class_repr


def my_planet(method):
     def inter(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        if 'Earth' in result:
            print('Você está em casa')
        return result
     return inter



def add_repr(cls):
    cls.__repr__ = my_repr
    return cls


def add_str(cls):
    cls.__str__ = my_str
    return cls

@add_repr
@add_str
class Team:
    def __init__(self, name):
        self.name = name

@add_str
@add_repr
class Planet:
    def __init__(self, name):
        self.name = name
    
    @my_planet
    def tell_name(self):
        return f'O planeta é {self.name}'
    

brasil = Team('Brasil')
portugal = Team('Portugal')

print(brasil)
print(portugal)

earth = Planet('Earth')
mars = Planet('Mars')

print(earth)
print(mars)


# print(earth.tell_name())
# print(mars.tell_name())