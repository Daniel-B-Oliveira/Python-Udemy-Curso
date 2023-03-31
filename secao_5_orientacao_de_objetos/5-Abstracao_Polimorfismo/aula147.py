# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__

# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames

# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str


class Ponto:
    def __init__(self, x, y, z='string'):
        self.x = x
        self.y = y
        self.z = z

    # def __str__(self):
    #     return f'{self.x}, {self.y}'


    def __repr__(self):     # Para desenvolvedores
        # class_name = type(self).__name__
        class_name = self.__class__.__name__
        # return f'{class_name}(x={self.x}, y={self.y}, z={self.z})' 
        # return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})' 
        return f'{class_name}(x={self.x!r}, y={self.y!r})' 
    

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y

        return Ponto(new_x, new_y)


    def __gt__(self, other):
        result_self = (self.x ** 2 + self.y ** 2)**1/2
        result_other = (other.x ** 2 + other.y ** 2)**1/2
        return result_self > result_other


if __name__ == '__main__':
    p1 = Ponto(4, 2)
    p2 = Ponto(6, 4)
    p3 = p1 + p2
    print(p3)

    print('P1 é maior que p2', p1 > p2)
    print('P2 é maior que p1', p2 > p1)

