import textwrap

class Venda:
    """
    A classe Venda representa uma venda de um produto, contendo informações como ID do produto, 
    nome do produto, quantidade vendida e preço unitário. A classe fornece métodos para calcular 
    o valor total da venda e exibir as informações de forma formatada.
    """

    def __init__(self, id_produto: int, produto: str, quantidade: int, preco_unitario: float) -> None:
        """
        Inicializa uma nova instância da classe Venda.

        Parâmetros:
        - id_produto (int): O identificador único do produto.
        - produto (str): O nome ou descrição do produto.
        - quantidade (int): A quantidade de itens vendidos.
        - preco_unitario (float): O preço unitário do produto.

        Exemplo:
        >>> venda = Venda(101, "Notebook", 2, 2500.00)
        """
        self.id_produto = id_produto
        self.produto = produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def calcular_total(self) -> float:
        """
        Calcula o valor total da venda com base na quantidade e no preço unitário.

        Retorna:
        - float: O valor total da venda.

        Exemplo:
        >>> venda = Venda(101, "Notebook", 2, 2500.00)
        >>> venda.calcular_total()
        5000.00
        """
        return self.quantidade * self.preco_unitario
    
    def exibir_info(self) -> None:
        """
        Exibe as informações da venda de forma formatada, incluindo ID do produto, nome do produto, 
        quantidade, preço unitário e valor total da venda. A formatação do texto é ajustada para remover 
        indentação desnecessária.

        O texto é impresso diretamente no console.

        Exemplo:
        >>> venda = Venda(101, "Notebook", 2, 2500.00)
        >>> venda.exibir_info()
        ID: 101, 
        Produto: Notebook, 
        Quantidade vendida: 2, 
        Preço unitário: R$ 2500.00,
        Preço total: R$ 5000.00
        """
        total = self.calcular_total()

        texto = f"""
        ID: {self.id_produto}, 
        Produto: {self.produto}, 
        Quantidade vendida: {self.quantidade}, 
        Preço unitário: R$ {self.preco_unitario:.2f},
        Preço total: R$ {total:.2f}
        """

        # Remove a indentação do texto
        texto_sem_indentacao = textwrap.dedent(texto)

        # Apresenta o texto
        print(texto_sem_indentacao)


class Cliente:
    """
    Classe que representa o comportamento do cliente, trazendo informações como seu nome,
    e-mail. Os métodos possibilitam o registro do valor de compra do cliente e o cálculo
    total de seu histórico de compra.
    """

    def __init__(self, nome: str, email: str) -> None:
        """
        Inicializa uma instância da classe Cliente.

        Args:
            nome (str): Nome do cliente.
            email (str): E-mail do cliente.
            compras (List): Lista que armazenará os histórico de compras do cliente.
        """
        self.nome = nome
        self.email = email
        self.compras = []

    def adicionar_comprar(self, valor: float) -> None:
        """
        Acrescenta o valor da compra do cliente no histórico de compras dele.

        Args:
            valor (float): Valor da compra realizada pelo cliente.
        """
        self.compras.append(valor)
        
    def total_gasto(self) -> int | float:
        """
        Calcula o valor total do histórico de compras do cliente.
        """
        total = 0
        for compra in self.compras:
            total += compra
        return total


from datetime import datetime
import pytz
from random import randint

class ContaBancaria:

    # Usa-se _ para inidicar que aquele atributo ou método não deveria ser acessado pelo usuário
    # Usa-se __ para bloquear que aquele atributo ou método para usuário

    # Esse é um exemplo de atributo de classe
    # Atributo estático
    # Variável global
    percentual_cheque_especial = 0.1

    # Exemplo de um método estático
    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        agora = datetime.now(fuso_br)
        agora = agora.strftime('%d/%m/%Y %H:%M:%S')
        return agora

    def __init__(self, nome: str, cpf: str, data_nascimento: str, num_conta: str) -> None:
        self._nome = nome
        self.__cpf = cpf
        self.data_nascimento = data_nascimento
        self.num_conta = num_conta
        self.saldo = 0
        self.historico = []
        self.cartoes = []

    def consultar_saldo(self):
        print(f'Seu saldo atual é R$ {self.saldo:.2f}')

    def consultar_historico(self):
        for historico in self.historico:
            print('Entrada/saída: R$', historico[0])
            print('Saldo final: R$', historico[1])
            print('Data e horário da transação: ', historico[2], '\n')

    def depositar_dinheiro(self, valor: float):
        self.saldo += valor
        self.historico.append((valor, self.saldo, ContaBancaria._data_hora()))

    def sacar_dinheiro(self, valor: float):
        if valor <= self.saldo + (self.saldo * self.percentual_cheque_especial):
            self.saldo -= valor
            self.historico.append((-valor, self.saldo, ContaBancaria._data_hora()))

        else:
            print(f'Você não pode sacar R$ {valor:.2f}')
            self.consultar_saldo()
            print(f'Você só pode sacar {(self.saldo * self.percentual_cheque_especial):.2f}')

    def transferir_dinheiro(self, valor, outra_conta):
        self.saldo -= valor
        self.historico.append((valor, self.saldo, ContaBancaria._data_hora()))
        outra_conta.saldo += valor
        outra_conta.historico.append((valor, outra_conta.saldo, ContaBancaria._data_hora()))


class CartaoCredito:
        
    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        agora = datetime.now(fuso_br)
        return agora

    def __init__(self, titular, conta_corrente) -> None:
        self.numero = randint(1000_0000_0000_0000, 9999_9999_9999_9999)
        self.titular = titular
        self.validade = f'{CartaoCredito._data_hora().month}/{CartaoCredito._data_hora().year + 4}'
        self.codigo_seguranca = f'{randint(0,9)}{randint(0,9)}{randint(0,9)}'
        self.limite = 1000
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)


class Pessoa:

    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    # Getter para nome
    @property
    def nome(self):
        return self._nome

    # Setter para nome
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str) and nome:
            self._nome = nome
        else:
            raise ValueError("O nome deve ser uma string não vazia.")

    # Getter para idade
    @property
    def idade(self):
        return self._idade

    # Setter para idade
    @idade.setter
    def idade(self, idade):
        if isinstance(idade, int) and idade > 0:
            self._idade = idade
        else:
            raise ValueError("A idade deve ser um número inteiro positivo.")


class Agencia:

    valor_limite_caixa = 1_000_000

    def __init__(self, telefone, cnpj, numero) -> None:
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.caixa = 0
        self.clientes = []
        self.emprestimos = []
        
    def verificar_caixa(self):

        if self.caixa > Agencia.valor_limite_caixa:
            print(f"O valor do caixa está adequado -> R$ {self.caixa}")

        else:
            print(f"O valor do caixa está abaixo do recomendado -> R$ {self.caixa}")

    def emprestar_dinheiro(self, valor, cpf, juros):

        if self.caixa > Agencia.valor_limite_caixa:
            self.emprestimos.append((valor, cpf, juros))

        else:
            print("Não há dinheiro no caixa para realizar empréstimos.")

    def cadastrar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


class AgenciaVirtual(Agencia):
    pass


class AgenciaComum(Agencia):
    pass


class AgenciaPremium(Agencia):
    pass










