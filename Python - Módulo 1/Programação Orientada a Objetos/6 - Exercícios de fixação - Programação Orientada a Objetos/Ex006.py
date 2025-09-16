# Adicione um método depositar(valor) à classe ContaBancaria que aumente o saldo.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar_valor(self):
        valor = float(input('Digite o valor para depositar: R$'))
        self.saldo += valor
        print(f'Seu novo saldo é de R${self.saldo}')

conta1 = ContaBancaria('Matheus', 0)
print(f'Titular: {conta1.titular}\nSaldo: R${conta1.saldo}')
conta1.depositar_valor()