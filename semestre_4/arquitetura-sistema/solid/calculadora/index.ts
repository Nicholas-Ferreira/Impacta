class Calculadora implements ISomar, ISubtrair, IMultiplicar, IDividir {
  private numero_1: number
  private numero_2: number

  constructor(numero_1: number, numero_2: number) {
    this.numero_1 = numero_1
    this.numero_2 = numero_2
  }

  somar(): number {
    return this.numero_1 + this.numero_2
  }
  subtrair(): number {
    return this.numero_1 - this.numero_2
  }
  multiplicar(): number {
    return this.numero_1 * this.numero_2
  }
  dividir(): number {
    return this.numero_1 / this.numero_2
  }
}

/* 
https://docs.google.com/document/d/1fYD06SgoBFsH4998yXgSRQwPxpoFhQi1sdCPI7KL0Wo/edit
*/