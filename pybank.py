'''
Sistema Bancário:

    Operações:
Depósito:
    O usuário deve informar o valor a ser depositado e será guardado em uma variável.

    Todos depósitos devem ser armazenados em uma variável para serem exibidos na operação extrato.

Saque:
    O sistema deve ter um limite diario de 3 saques.

    O valor máximo por saque deve ser de R$500,00.

    Caso o usuário não tenha o valor em conta, o sistema irá exibir uma mensagem dizendo que não será possivel sacar o dinheiro por falta de saldo.

    Todos os saques devem ser armazedados em uma variável para exibir na operação extrato.

Extrato:
    Aqui ficara registrado todas as operações realizadas pelo usuário.

    No fim da listagem deve ser exibido o saldo atual da conta

    Os valores devem ser exibidos no formato R$XXXX.XX

'''
saldo = 0
saque_desejado = 0 
deposito = 0
limite_valor = 500
numero_saque = 1
LIMITE_SAQUES = 3
saque2 = 0
total_saques = 0
extrato1 = 0
extrato2 = 0
extrato = ""


nome = input('Digite seu nome: ')
print(f'Olá {nome}. Escolha uma das opções abaixo: ')
operacoes = [
   'deposito = d',
   'saque = s',
   'extrato = e',
   'sair = x'
]
for op in operacoes:
    print(op)

while True:
    operacao = input('\nDigite a operação escolhida: ')
    if operacao == 'd':
        print('\nDeposito: ')
        deposito = int(input('Digite o valor a ser depositado: '))
        saldo += deposito

    elif operacao == 's':
        if numero_saque <= LIMITE_SAQUES:
            print('Saque: ')
            saque_desejado = int(input('Digite o valor a ser sacado: '))
            if saque_desejado <= limite_valor and saque_desejado <= saldo:
                print(f'Realizando saque no valor de: {saque_desejado:.2f}')
                saldo = saldo - saque_desejado
                limite_valor = limite_valor - saque_desejado
                extrato += f' - R${saque_desejado:.2f} '
                numero_saque += 1

                if numero_saque <= LIMITE_SAQUES:
                    novo_saque = input('Deseja fazer um novo saque? ')
                    if novo_saque == 's':
                        saque2 = int(input('Digite o valor: '))
                        total_saques = saque_desejado + saque2
                        if total_saques <= limite_valor and saque2 <= saldo:
                            print(f'Realizando saque de: R${saque2:.2f}')
                            saldo = saldo - saque2
                            extrato += f' - R${saque2:.2f}'
                            numero_saque += 1
                        else:
                            print('Limite de saque excedido!')
                    elif novo_saque == 'n':
                        print('')
                    else:
                        print('Opção Invalida!')


            else:
                print('\nValor para saque não disponivel! \nVerifique seu saldo e o limite de saque!')

            
                            
        else:
            print('Número de saques excedido!')
    elif operacao == 'e':
        
        print(f'''
            Extrato: 
              
            Dia DD/MM/AAAA

            Deposito Realizado: 
            R${deposito:.2f}''')

        print(f'''
            Saques Realizado:
            {extrato}''')


        print(f'''
            Saldo Atual:
            R${saldo:.2f}
              ''')

    else:
        if operacao == 'x':
            print('\nSaindo... \nObrigado por nos escolher!\n')
            
            