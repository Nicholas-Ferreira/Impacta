import requests as req

def logradouro(cep):
  retorno = req.get(f"http://viacep.com.br/ws/{str(cep)}/json").json()
  if('logradouro' in retorno):
    logradouro = retorno['logradouro']
    cidade = retorno['localidade']
    estado = retorno['uf']
    print(f"{logradouro} - {cidade} - {estado}")
  else:
    print("Error")

logradouro("00000000")