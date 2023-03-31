# Médodo especial __call__
# Callabre é alg que pode ser executado com parenteses
# EM classes normais, __call__ faz a instancia de uma
# classe 'callable'.

class CallMe:
    def __init__(self,phone):
        self.phone = phone

    def __call__(self, *args, **kwds):
        print(*args, 'está chamando', self.phone)

call = CallMe('123212131231')

call('Daniel Barreto')