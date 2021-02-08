interface IOperacao {
  resultado(n1: number, n2: number): number
}

class Somar implements IOperacao {
  public resultado(n1: number, n2: number): number {
    return n1 + n2
  }
}

class Subtrair implements IOperacao {
  public resultado(n1: number, n2: number): number {
    return n1 - n2
  }
}

class Calculadora {
  calcular(numero_1: number, numero_2: number, operador: IOperacao) {
    return operador.resultado(numero_1, numero_2)
  }
}

const calculadora = new Calculadora()
const soma = calculadora.calcular(1, 1, new Somar)