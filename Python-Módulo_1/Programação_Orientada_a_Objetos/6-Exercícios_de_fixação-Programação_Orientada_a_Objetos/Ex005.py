# Crie uma classe ContaBancaria com atributos titular e saldo. Inicialize o saldo com zero.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

conta1 = ContaBancaria('Matheus', 0)
print(f'Titular: {conta1.titular}\nSaldo: R${conta1.saldo}')