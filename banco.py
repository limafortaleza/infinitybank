# banco seria o modelo /entidade (contas bancárias)



banco = [
    {"conta": 1, "nome": "Mariana", "saldo": 150.00},
    {"conta": 2, "nome": "Jonas", "saldo": 205.50},
]

conta_atual = 2  # variável de controle.


def adicionarConta(nome: str, saldo: float) -> None:

    global conta_atual  # para permitir alterar a variavel global, se nao tiver a palavra reservada a variavel nao vai ser lida dentro da função.
    conta_atual += 1 #a conta atual vai sempre ser adicionada a 1 para criar a próxima
    cliente = {
        "conta": conta_atual,
        "nome": nome,
        "saldo": saldo
    }
    banco.append(cliente)
    print(f"Cliente cadastrado com sucesso!")


#funcao auxiliar : SABER SE A CONTA DO CLIENTE EXISTE. ELA SERÁ USADA POR TODAS AS OUTRAS JA QUE VOU PRECISAR SEMPRE PESQUISAR SE O CLIENTE EXISTE.
def obterConta(conta:int)-> dict or None: #retorna ou dicionarios ou none - especificar a função chama-se assinatura.
    for cliente in banco:
        if cliente['conta']==conta:
            return cliente
    return None


def deletarConta(conta:int) -> None:
    cliente=obterConta(conta) #chamando a função auxiliar
    if cliente: # ou if cliente !=None:
        banco.remove(cliente)
        print("Cliente deletado com sucesso!")
    else:
        print("Cliente nao existe!")


def editarNome(novoNome:str, conta:int) -> None:
    cliente = obterConta(conta)
    if cliente:
        cliente['nome']=novoNome
        print('Dados alterados com sucesso')
    else:
        print('Cliente nao existe!')


def consultarCliente(conta:int)->None:
    cliente=obterConta(conta)
    if cliente:
        print(f'Conta:{conta} \n'
              f'Cliente: {cliente["nome"]} \n'
              f'Saldo: {cliente["saldo"]}')
    else:
        print("Cliente não existe!")

def listarTodasContas()-> None:
    for cliente in banco:
        for k, v in cliente.items():
            print(k,v, )
        # consultarCliente(cliente['conta']) #essa função já lista sob demanda, mas tb pode listar todas.


        print('=' * 20)


if __name__== "__main__": #pra nao ter que ir na função principal e importar o modulo la. Sever pra testar o modulo no próprio módulo.
    listarTodasContas()
