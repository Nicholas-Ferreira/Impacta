from pessoasModel import PessoasModel

pessoas = PessoasModel()
#pessoas.create('Nicholas', 'nicholas_sc@live.com')
#pessoas.update('Nicholas Ferreira', 'nicholas_sc@live.com')
#pessoas.delete(1)

print('========= Pegar Todas as Pessoas =========')

lista = pessoas.listar()
for pessoa in lista:
  print(f'id: {pessoa[0]}, ', end='')
  print(f'nome: {pessoa[1]}, ', end='')
  print(f'email: {pessoa[2]}')

print('========= Pegar uma Pessoas =========')

pessoa = pessoas.get(1)
if(pessoa):
  print(f'id: {pessoa[0]}, ', end='')
  print(f'nome: {pessoa[1]}, ', end='')
  print(f'email: {pessoa[2]}')
