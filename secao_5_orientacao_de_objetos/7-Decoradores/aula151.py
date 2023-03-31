# Funçao decoradora e decoradore de classes

def add_repr(cls):
    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name} ({class_dict})'
        return class_repr
    cls.__repr__ = my_repr
    return cls


# class MyReprMixin:            # erança menos recomendada
#     def __repr__(self):
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name} ({class_dict})'
#         return class_repr

@add_repr
class Team:
    def __init__(self, name):
        self.name = name

    
@add_repr
class Planet:
    def __init__(self, name):
        self.name = name
    


# Team = add_repr(Team)  == @add_repr
brasil = Team('Brasil')
portugal = Team('Portugal')

print(brasil)
print(portugal)

# Planet = add_repr(Planet)
earth = Planet('Earth')
mars = Planet('Mars')

print(earth)
print(mars)