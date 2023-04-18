class Categoria:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id


class Produto:
    def __init__(self, nome, id, categoria: Categoria):
        self.nome = nome
        self.id = id
        self.categoria = categoria


class Estoque:
    produtos = {}

    @classmethod
    def add_produto(cls, produto: Produto):
        cls.produtos[produto.nome] = produto.categoria.nome

    @classmethod
    def mostra_produtos(cls):
        return cls.produtos

    @classmethod
    def remover_produto(cls, value):
        del (cls.produtos[value])


class Pessoa:
    def __init__(self, nome, cpf, idade, compras):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.compras = compras


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, idade, id, vendas):
        self.id = id
        super().__init__(nome, cpf, idade)
        self.vendas = vendas

    vendas = 0


class Cliente(Pessoa):
    def __init__(self, nome, cpf, idade):
        super().__init__(nome, cpf, idade)


class Fornecedor():
    def __init__(self, nome, cnpj, id):
        self.nome = nome
        self.cnpj = cnpj
        self.id = id


class Caixa:
    vendas = {}

    @classmethod
    def venda(cls, produto: Produto):
        pass
