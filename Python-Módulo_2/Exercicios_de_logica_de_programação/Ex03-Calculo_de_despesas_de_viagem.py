'''
Solicite ao usuário o custo diário de uma viagem (hospedagem,
alimentação, transporte, etc.) e o número de dias que ele pretende
viajar. Calcule o valor total da viagem.
'''

hospedagem = float(input('Digite o custo da hospedagem: '))
alimentacao = float(input('Digite o custo da alimentação: '))
transporte = float(input('Digite o custo do transporte: '))
dias_de_viagem = int(input('Digite a quantidade de dias de viagem: '))
total_viagem = (hospedagem + alimentacao + transporte) * dias_de_viagem
total_diário = hospedagem + alimentacao + transporte

print(
    f'O custo total diário é de {total_diário}\nO custo total da viagem inteira é de {total_viagem}')
