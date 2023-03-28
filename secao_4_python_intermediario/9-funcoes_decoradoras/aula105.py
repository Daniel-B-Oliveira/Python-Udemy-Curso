
def decorator_factory(a=None, b=None, c=None):  
    def function_factory(func):
        print('Decorator')
        def nested(*args, **kwargs):
            print('Decorator parameters:', a, b, c)
            print('nested')
            res = func(*args, **kwargs)
            return res
        return nested
    return function_factory


@decorator_factory(1, 2, 3)
def sum_func(x,y):
    return x + y


ten_plus_five = sum_func(1, y=2)
print(ten_plus_five)