from banco import obterConta, banco

def transferir(contaOrigem:int, contaDestino: int, valor:float) -> None:
    contaOrigem=obterConta(contaOrigem)
    contaDestino=obterConta(contaDestino)
    if contaOrigem and contaDestino:
        if contaOrigem['saldo']>=valor:
            contaOrigem['saldo']-=valor
            contaDestino['saldo']+=valor
            print('Transferência realizada com sucesso')
            print(f'Novo saldo da conta: {contaOrigem["saldo"]}')
        else:
            print('Saldo insuficiente')
    else:
        print('Uma ou mais contas não existem')


if __name__ == "__main__":
    transferir(1,2,59)
    print(banco)