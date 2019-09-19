# Atividade Contínua 03
# Aluno 01: Lucas Eduardo Ano RA:1900675
# Aluno 02: Nicholas Mota Ferreira RA:1900953


def incluir_novo_nome(agenda, nome, telefone):
    agenda[nome] = telefone
    '''
    Essa função acrescenta um novo nome na agenda,
    com um ou mais telefones. Ela deve receber como
    argumentos o dicionario, o nome e uma lista de telefones.
    '''


def excluir_nome(agenda, nome):
    if nome in agenda:
        del agenda[nome]
    '''
    Essa função exclui uma pessoa da agenda.
    Ela deve receber como parâmetros de entrada o dicionário
    e o nome a ser exclúído. Caso o nome não exista na agenda, nenhuma
    alteração deve ser feita
    '''


def consultar_telefone(agenda, nome):
    return agenda[nome]
    '''
    Essa função retorna os telefones de uma pessoa na agenda.
    Ela deve receber como parâmetros de entrada o dicionário
    e o nome da pessoa a ser consultado.
    '''


def incluir_telefone(agenda, nome, telefone):
    if nome in agenda:
        agenda[nome].append(telefone)
    '''
    Essa função acrescenta um telefone em um nome existente na agenda.
    A função recebe como argumentos o diciomário, o nome e um telefone.
    Caso o nome não exista na agenda, nenhuma alteração deve ser feita.
    '''


def excluir_telefone(agenda, nome, telefone):
    if nome in agenda:
        del(agenda[nome][agenda[nome].index(telefone)])
    '''
    Essa função exclui um telefone específico de uma pessoa
    que já está na agenda.
    A função recebe como argumentos o diciomário, o nome e um telefone.
    Se a pessoa tiver apenas um telefone, ela deve ser excluída da agenda.
    '''
