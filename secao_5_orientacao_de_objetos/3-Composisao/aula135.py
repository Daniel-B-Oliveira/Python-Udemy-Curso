# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).

class Carinho:
    def __init__(self):
        self._produtos = []


    def total(self):
        return sum([p.preco for p in self._produtos])
    

    def listar_produto(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()


    def inserir_produtos(self, *produtos):
        self._produtos.extend(produtos)

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carinho()
p1, p2 = Produto('Canheta', 1.20), Produto('Camiseta', 20)
carrinho.inserir_produtos(p1,p2)
carrinho.listar_produto()
print(carrinho.total())