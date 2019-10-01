# Atividade Contínua 05
# Aluno 1: Nicholas Ferreira RA 1900953
# Aluno 2: Fernando Franco RA 1900519


class Piloto:
    __nome = None
    __habilidade = None

    def __init__(self, nome, habilidade):
        self.__nome = nome
        self.__habilidade = habilidade

    def get_nome(self):
        return self.__nome

    def get_habilidade(self):
        return self.__habilidade


class CarroCorrida:
    __numero_identificacao = None
    __piloto = None
    __velocidade_atual = 0.0
    __velocidade_maxima = 150.0

    def __init__(self, numero_identificacao, piloto):
        self.__numero_identificacao = numero_identificacao
        self.__piloto = piloto

    def get_numero_identificacao(self):
        return self.__numero_identificacao

    def get_piloto(self):
        return self.__piloto

    def get_velocidade_atual(self):
        return self.__velocidade_atual

    def get_velocidade_maxima(self):
        return self.__velocidade_maxima

    def __set_velocidade_atual(self, velocidade):
        self.__velocidade_atual += velocidade

    def ligar(self):
        print("VRUUUMmmmmmmmmm")

    def desligar(self):
        print("MMMmmmm......")

    def acelerar(self):
        self.__set_velocidade_atual(10 + self.get_piloto().habilidade * 0.1)
        if self.get_velocidade_atual() > self.get_velocidade_maxima():
            self.__set_velocidade_atual(self.get_velocidade_maxima())
        print("Carro ", self.get_numero_identificacao(), " acelerou")
        print("Velocidade atual: ", self.get_velocidade_atual())

    def frear(self, intensidade_freada):
        if intensidade_freada > 100:
            intensidade_freada = 100
        elif intensidade_freada < 0:
            intensidade_freada = 0

        self.__set_velocidade_atual(-(intensidade_freada * 0.25))
        if self.get_velocidade_atual() < 0:
            self.__set_velocidade_atual(0.0)

        print("Carro ", self.get_numero_identificacao(), " freou")
        print("Velocidade atual: ", self.get_velocidade_atual())


# Criacao dos pilotos de cada equipe
piloto_equipe_velocidade = Piloto("Felipe Lazanha", 75)
piloto_equipe_trapaceiros = Piloto("Rubens Branquelo", 65)

# Define atributos do piloto da equipe Velocidade
piloto_equipe_velocidade.nome = "Felipe Lazanha"
piloto_equipe_velocidade.habilidade = 75

# Define atributos do piloto da equipe Trapaceiros
piloto_equipe_trapaceiros.nome = "Rubens Branquelo"
piloto_equipe_trapaceiros.habilidade = 65

# Criacao dos carros que irao correr
carro_equipe_velocidade = CarroCorrida(1, piloto_equipe_velocidade)
carro_equipe_trapaceiros = CarroCorrida(2, piloto_equipe_trapaceiros)

# Define atributos dos carros de corrida
carro_equipe_velocidade.numero_identificacao = 1
carro_equipe_trapaceiros.numero_identificacao = 2

# Os pilotos sao vinculados aos seus carros
carro_equipe_velocidade.piloto = piloto_equipe_velocidade
carro_equipe_trapaceiros.piloto = piloto_equipe_trapaceiros

# Carros são ligados
carro_equipe_velocidade.ligar()
carro_equipe_trapaceiros.ligar()

# Inicia a corrida
carro_equipe_velocidade.acelerar()
carro_equipe_trapaceiros.acelerar()
carro_equipe_velocidade.acelerar()
carro_equipe_trapaceiros.acelerar()
carro_equipe_velocidade.acelerar()
carro_equipe_velocidade.acelerar()
carro_equipe_velocidade.acelerar()
carro_equipe_trapaceiros.velocidade_atual = 200.0   # Uma trapaça
print(carro_equipe_trapaceiros.velocidade_atual)
carro_equipe_trapaceiros.frear(50)
