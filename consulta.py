from banco import obterConta, banco

def consultarSaldo(conta:int) -> None:
    cliente=obterConta(conta)
    if cliente:
        print(f'Saldo de {cliente["nome"]} é: {cliente["saldo"]}')
    else:
        print('Conta não existe!')

if __name__ == "__main__":
    consultarSaldo(2)
    print(banco)