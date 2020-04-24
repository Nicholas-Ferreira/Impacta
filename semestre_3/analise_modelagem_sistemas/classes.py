class Ingresso:
  valor = 10

  def __str__(self):
    return str(self.getValor())

  def getValor(self):
    return self.valor

class IngressoVIP(Ingresso):
  valor_adicional = 5

  def getValor(self):
    return self.valor + self.valor_adicional

class ControllerIngresso:
  def __init__(self):
    i = Ingresso()
    iv = IngressoVIP()
    print(f'Valor do Ingresso Normal: {i}')
    print(f'Valor do Ingresso VIP: {iv}')

class ColetorDeIngresso():
  total = 0

  def __init__(self, ingressos):
    for i in ingressos:
      self.total += float(i.getValor())
    print(f'Valor total igual a: {self.total}')

ingressos = []
ingressos += [Ingresso() for _ in range(1)]
ingressos += [IngressoVIP() for _ in range(1)]

ControllerIngresso()
ColetorDeIngresso(ingressos)