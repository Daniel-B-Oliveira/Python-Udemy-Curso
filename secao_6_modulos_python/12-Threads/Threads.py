from time import sleep

from threading import Thread
from threading import Lock

# # print('HELLO')

# # for i in range(10):
# #     print(i)
# #     sleep(0.5)

# # print('WORLD!')

# class MeuThread(Thread):
#     def __init__(self, text, time):
#         self.text = text
#         self.time = time

#         super().__init__()

#     def run(self):
#         sleep(self.time)
#         print(self.text)


# t1 = MeuThread('Thread 1', 5)
# t1.start()

# t2 = MeuThread('Thread 2', 3)
# t2.start()

# t3 = MeuThread('Thread 3', 5)
# t3.start()

# t4 = MeuThread('Thread 4', 15)
# t4.start()

# for i in range(20):
#     print(i)
#     sleep(1)

# def vai_demorar(texto, tempo):
#     sleep(tempo)
#     print(texto)

# t1 = Thread(target=vai_demorar, args=('Olá, mundo1!', 5))
# t2 = Thread(target=vai_demorar, args=('Olá, mundo 2!', 10))
# t3 = Thread(target=vai_demorar, args=('Olá, mundo 3!', 15))
# t4 = Thread(target=vai_demorar, args=('Olá, mundo 4!', 2))

# t_total = t1, t2, t3, t4

# for t in t_total:
#     t.start()

# for i in range(10):
#     print(i)
#     sleep(1)

# def vai_demorar(texto, tempo):
#     sleep(tempo)
#     print(texto)


# tempo_t1 = 10
# t1 = Thread(target=vai_demorar, args=('Olá, mundo1!', tempo_t1))
# t1.start()
# # t1.join()  # Bloqueia a thread
# t = 1

# while t1.is_alive():
#     print(f'esperando a thread {t}%')
#     t += 1
#     sleep(tempo_t1/100)

# print(f'Thread acabou, {t}%')

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes')
            self.lock.release()
            return
        
        sleep(1)

        self.estoque -= quantidade

        print(f'Você comprou {quantidade} ingresso(s).'\
              f' Ainda temos {self.estoque} em estoque')

        self.lock.release()

if __name__ == '__main__':
    ingressos = Ingressos(10)
    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()
    
    print(ingressos.estoque)