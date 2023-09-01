from banco import obterConta, banco

def depositar(conta:int, valor:float) -> None:
    cliente=obterConta(conta)
    if cliente:
        cliente ['saldo']=cliente['saldo']+valor
        print('Deposito realizado com sucesso!')
        print(f'Novo valor na conta de {cliente["nome"]} é {cliente["saldo"]}')
    else:
        print('cliente não existe!')


if __name__ == "__main__":
    depositar(2,1900)
    print(banco)
