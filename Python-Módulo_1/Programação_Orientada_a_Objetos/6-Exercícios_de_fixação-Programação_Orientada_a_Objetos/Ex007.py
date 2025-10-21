# Adicione um método sacar(valor) à classe ContaBancaria que diminua o saldo, se houver saldo suficiente.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar_valor(self):
        valor = float(input('Digite o valor para depositar: R$'))
        if valor > 0:
            self.saldo += valor
            print(f'Valor depositado com sucesso, seu novo saldo é de R${self.saldo}')
        else:
            print('Por favor, digite valores válidos para o programa.')

    def sacar_valor(self):
        valor = float(input('Digite o valor para sacar: R$'))
        if valor <= self.saldo and valor >= 0:
            self.saldo = self.saldo - valor
            print(f'Você sacou R${valor}\nSaldo restante: R${self.saldo}')
        elif valor > self.saldo:
            print(f'Saldo: R${self.saldo}\nSaldo insuficiente para sacar o valor pedido de R${valor}!')
        else:
            print('Por favor, digite valores válidos para o programa.')

conta1 = ContaBancaria('Matheus', 0)
print(f'Titular: {conta1.titular}\nSaldo: R${conta1.saldo}')
conta1.depositar_valor()
conta1.sacar_valor()