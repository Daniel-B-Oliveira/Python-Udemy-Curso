
def decorator_factory(name):  
    def function_factory(func):
        print('Decorator', name)

        def nested(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {name}'
            return final
        return nested
    return function_factory


@decorator_factory(name= '5')
@decorator_factory(name= '4')
@decorator_factory(name= '3')
@decorator_factory(name= '2')
@decorator_factory(name= '1')
def sum_func(x,y):
    return x + y


ten_plus_five = sum_func(1, y=2)
print(ten_plus_five)