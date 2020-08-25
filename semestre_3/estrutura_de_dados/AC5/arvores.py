'''
Uma arvore é uma estrutura como


      10
     /  \
    5    20
   /\   /  \
  2  7 12  30 

Observe que 10 tem elementos a sua "esquerda" (5,2 e 7)
e a sua "direita" (20, 12 e 30)

Os elementos a esquerda são números menores que 10,
e os elementos a direita, maiores que 10.
(O mesmo vale para o 5: a esquerda, temos 2,
que é menor, e a direita, 7, que é maior)
'''

'''
Perceba que, para verificar se um número está nessa arvore,
precisamos usar apenas 3 consultas.

12 está na arvore?
Olho pro 10. Se 12 estiver, está na arvore direita 
(onde estão todos os números maiores que 10 da arvore)
Olho pro 20, se 12 estiver está na arvore esquerda
(onde estão todos os números menores que 20 da "subarvore")
Olho pro 12, e achei!
A resposta é True
A sequencia de números visitados foi [10,20,12]

      10
     /  \
    5    20
   /\   /  \
  2  7 12  30 

9 está na arvore?
Olho pro 10. Se 9 estiver, está na arvore esquerda
(onde estão todos os números menores que 10 da arvore)
Olho pro 5. Se 9 estiver está na arvore direita
(onde estão todos os números maiores que 5 da "subarvore")
Olho pro 7. Queria procurar "a direita" dele, mas não tem ninguém
A resposta é False
A sequencia de números visitados foi [10,5,7]

EXERCICIO: se eu quiser procurar 40 na árvore, que números visitarei?
'''
busca40=[10,20,30]
'''
E se eu quiser buscar o 15? E o 3? E o 5?
'''
busca15=[10, 20, 12]
busca3=[10, 5, 2]
busca5=[10, 5]

'''
Uma outra questão importante é a inserção.
        20
     /      \
    10      30
   /  \    /  \
  8   C   D    E
 / \
A  B

Se eu quiser inserir o número 40 nessa arvore, a posição correta para 
fazer isso é a posição E (40 é maior que 20, tem que estar a direita do
20. Também é maior que 30, então tem que estar a direita do 30)

Se eu quiser inserir o número 12, a posição correta é C (ele tem que estar
a esquerda do 20, mas à direita do 10)

Exercicio:
    Se eu te der uma lista de numeros, quero uma lista que diga
    onde eles devem ser inseridos.

    Por exemplo:
'''
numeros1 = [2,11,25]
letras1 = ['A','C','D']
'''
Faça o mesmo para as duas listas abaixo
'''
numeros2 = [19,21,33,7]
letras2 =  ['C', 'D', 'E', 'A']
numeros3 = [9,11,7,50]
letras3 =  ['B', 'C', 'A', 'E']

#para o que vem a seguir, é legal usar a função
#pprint, que imprime dicionarios de uma forma legivel
from pprint import pprint
'''
Para representar arvores em python, usamos dicionários.
Por exemplo, para representar uma árvore que apenas contém 30, fazemos
'''
arvore= {'raiz':30,'direita':{},'esquerda':{}}
#pprint(arvore)
'a cada passo você pode descomentar o pprint para ver como está a arvore'
'para adicionar o 20, fazemos o seguinte'
a20= {'raiz':20,'direita':{},'esquerda':{}}
arvore['esquerda']=a20
#pprint(arvore)
'para adicionar o 40, fazemos o seguinte'
a40= {'raiz':40,'direita':{},'esquerda':{}}
arvore['direita']=a40
#pprint(arvore)
'para adicionar o 35, fazemos o seguinte'
a35= {'raiz':35,'direita':{},'esquerda':{}}
aux = arvore['direita']
aux['esquerda']=a35
#pprint(arvore)
'para adicionar o 45, fazemos o seguinte'
a45= {'raiz':45,'direita':{},'esquerda':{}}
aux = arvore['direita']
aux['direita']=a45
#pprint(arvore)
'''
o pprint é legal para você ver as árvores, mas nao vai ser usado
dentro das funções pedidas. É só pra te ajudar a ver o que está
acontecendo.
'''
 
'''
Agora voce monta uma arvore.
Insira o 100, depois o 30, depois o 40, depois o 110
Já vou iniciar pra voce
'''
arvore100={
  'raiz':100,
  'direita': {'raiz':110,'direita':{},'esquerda':{}},
  'esquerda': { 'raiz':30,'direita': {'raiz':40,'direita':{},'esquerda':{} },'esquerda':{} }
}

'Representar uma arvore vazia é bem fácil'
vazia= {}
'(se voce notar, já fizemos isso várias vezes!)'

'''
A primeira funcao que vamos fazer nesse arquivo
recebe uma arvore e retorna a sua raiz

Se a arvore for vazia, sua funcao deve retornar a string 'nao tem raiz'
'''

def raiz(arvore):
  if len(arvore) == 0:
    return 'nao tem raiz'
  return arvore['raiz']

'''
Uma árvore tem tipicamente 2 árvores "penduradas"
nela, a da direita e a da esquerda.

Faça uma função que, dada uma árvore, retorna a árvore da esquerda.

Não se preocupe com o caso de não haver árvore à esquerda.
'''

def arvore_esquerda(arvore):
    return arvore['esquerda']

'''
O proximo passo:
    Uma função que recebe uma árvore A,
    vai andando para a esquerda "até não poder mais" (até estar
    em uma árvore que não tem filho esquerdo) e
    devolve a raiz correspondente a essa árvore mais a esquerda.

'''
def tudo_a_esquerda(arvore):
  if 'esquerda' in arvore and len(arvore['esquerda']) != 0:
    return tudo_a_esquerda(arvore['esquerda'])
  return arvore['raiz']


'''
Agora, façamos uma funcao que recebe uma arvore e um numero, e faz uma busca
para ver se o número está ou nao na arvore. 

Ela retorna True se o numero está na arvore, false caso contrário
'''

def busca(arvore,procurado):
  if raiz(arvore) == 'nao tem raiz':
    return False
  if arvore['raiz'] == procurado:
    return True
  if arvore['raiz'] > procurado:
    return busca(arvore['esquerda'], procurado)
  if arvore['raiz'] < procurado:
    return busca(arvore['direita'], procurado)


'''
Agora, vamos fazer uma funcao para inserir um elemento em uma arvore.

Por exemplo, ao pegarmos a arvore

      10
     /  \
    5    20
   /\   /  \
  2  7 12  30 

e inserirmos o elemento 15, temos
      
      10
     /  \
    5    20
   /\   /  \
  2  7 12  30 
        \
        15

(Estamos mantendo as propriedades: o 15 tem que estar a direita do 10, a esquerda do 20
e a direita do 12)

(outra coisa: se inserirmos o 5, nada acontece, porque ele já está na arvore)
'''

def insere(arvore,elemento):
  ramo = { 'raiz': elemento, 'direita': {}, 'esquerda': {} }
  if raiz(arvore) == 'nao tem raiz':
    arvore['raiz'] = elemento 
    arvore['esquerda'] = {}
    arvore['direita'] = {} 
    return arvore
  elif busca(arvore, elemento):
    return
  elif elemento > arvore['raiz']:
    if raiz(arvore['direita']) == 'nao tem raiz':
      arvore['direita'] = ramo
    else:
      insere(arvore['direita'], elemento)
  else:
    if raiz(arvore['esquerda']) == 'nao tem raiz':
      arvore['esquerda'] = ramo
    else:
      insere(arvore['esquerda'], elemento)
'''
Agora, faça uma funcao que recebe uma arvore e diz quantos elementos ela tem
'''

def conta(arvore):
  if raiz(arvore) == 'nao tem raiz':
    return 0
  return 1 + conta(arvore['esquerda']) + conta(arvore['direita'])

'''
Agora, vamos fazer uma funcao para calcular a soma de todos os numeros presentes
em uma arvore. Acho que recursao pode ser util aqui
'''

def soma(arvore):
  if raiz(arvore) == 'nao tem raiz':
    return 0
  return soma(arvore['esquerda']) + soma(arvore['direita']) + arvore['raiz']

'''
Agora, façamos uma função que retorna o maior numero presente
na arvore. Voce nao precisa usar recursão (e se usar
seu algoritmo vai funcionar, mas talvez fique lento)
'''
def maior(arvore):
  while arvore['direita'] != {}:
    arvore = arvore['direita']
  return arvore['raiz']


'''
A partir daqui nao há nada para você implementar
'''

def cria_simples(lista):
    arvore = {}
    for e in lista:
        insere(arvore,e)
    return arvore

ex1= {'direita': {'direita': {'direita': {}, 'esquerda': {}, 'raiz': 20}, 'esquerda': {'direita': {}, 'esquerda': {}, 'raiz': 12}, 'raiz': 15}, 'esquerda': {'direita': {'direita': {}, 'esquerda': {}, 'raiz': 7}, 'esquerda': {'direita': {}, 'esquerda': {}, 'raiz': 2}, 'raiz': 5}, 'raiz': 10}

ex2= {'direita': {}, 'esquerda': {'direita': {}, 'esquerda': {'direita': {}, 'esquerda': {}, 'raiz': 2}, 'raiz': 3}, 'raiz': 10} 

ex3 = {'direita': {'direita': {}, 'esquerda': {'direita': {}, 'esquerda': {}, 'raiz': 110}, 'raiz': 120}, 'esquerda': {'direita': {'direita': {}, 'esquerda': {}, 'raiz': 10}, 'esquerda': {}, 'raiz': 5}, 'raiz': 90}
arvore2= {'raiz':2,'direita':{},'esquerda':{}}
arvore7= {'raiz':7,'direita':{},'esquerda':{}}
arvore5 = {'raiz':5, 'esquerda':arvore2, 'direita': arvore7}
arvore12= {'raiz':12,'direita':{},'esquerda':{}}
arvore30= {'raiz':30,'direita':{},'esquerda':{}}
arvore20 = {'raiz':20, 'esquerda':arvore12, 'direita': arvore30}
arvore10={'raiz':10,'direita':arvore20,'esquerda':arvore5}
arv_torta={'direita': {},
 'esquerda': {'direita': {},
              'esquerda': {'direita': {},
                           'esquerda': {'direita': {},
                                        'esquerda': {},
                                        'raiz': 9},
                           'raiz': 10},
              'raiz': 11},
 'raiz': 12}
import unittest
# import pprint
import hashlib

class TestStringMethods(unittest.TestCase):

    def test_001a_buscas(self):
        self.verifica_resposta(busca40,'feb9e440ff56772c4479f005489fe8b7b914bee97e9742b1fa01eb0c')
    def test_001b_buscas(self):
        self.verifica_resposta(busca15,'ab437c0e9544f634d919fff8592eef327db3ed8567cad06c8b1d9afc')
    def test_001c_buscas(self):
        self.verifica_resposta(busca3,'e8f50d09a2838980b07dc396e5f5767e85c90e0dd100700bb2f638b8')
    def test_001d_buscas(self):
        self.verifica_resposta(busca5,'37bc87547ee4ffb1b04a4927e097209938ffb3f7d1b7a49360e09d61')
    
    def test_002a_inserir(self):
        self.verifica_resposta(letras2,'cd144b3ba1fd2bc639eef7ae6f04c98a09ebecf7ec6f53d1874ec199')
    def test_002b_inserir(self):
        self.verifica_resposta(letras3,'80150a2e2007176ea15ba99718131cace42a660947208280340a5df4')

    #Relembrando teste 3: Insira o 100, depois o 30, depois o 40, depois o 110
    def test_003a_montar_arvore(self):
        self.assertEqual(arvore100['raiz'],100)
    def test_003b_montar_arvore(self):
        self.assertEqual(arvore100['esquerda']['raiz'],30)
        self.assertEqual(arvore100['esquerda']['esquerda'],{})
    def test_003c_montar_arvore(self):
        self.assertEqual(arvore100['esquerda']['direita']['raiz'],40)
        self.assertEqual(arvore100['esquerda']['direita']['esquerda'],{})
        self.assertEqual(arvore100['esquerda']['direita']['direita'],{})
    def test_003d_montar_arvore(self):
        self.assertEqual(arvore100['direita']['raiz'],110)
        self.assertEqual(arvore100['direita']['direita'],{})
        self.assertEqual(arvore100['direita']['esquerda'],{})
    
    def test_100_raiz(self):
        self.assertEqual(raiz(arvore5), 5)
        self.assertEqual(raiz(ex1), 10)
        self.assertEqual(raiz(ex2), 10)
        self.assertEqual(raiz(ex3), 90)
    def test_100a_raiz(self):
        self.assertEqual(raiz({}), 'nao tem raiz')

    def test_101_arvore_esquerda(self):
        self.assertEqual(arvore_esquerda(arvore5), arvore2)
        self.assertEqual(arvore_esquerda(arvore10), arvore5)
        self.assertEqual(arvore_esquerda(arvore20), arvore12)
        self.assertEqual(arvore_esquerda(arvore12), {})
    
    def test_102_tudo_a_esquerda(self):
        self.assertEqual(tudo_a_esquerda(arvore5), arvore2['raiz'])
        self.assertEqual(tudo_a_esquerda(arvore10), arvore2['raiz'])
        self.assertEqual(tudo_a_esquerda(arvore20), arvore12['raiz'])
        
    
    def test_103_busca(self):
        self.assertTrue(busca(arvore10,10))
        self.assertFalse(busca(arvore10,15))
        self.assertFalse(busca(ex3,91))
        self.assertTrue(busca(ex3,90))
        self.assertTrue(busca(arvore5,5))
        self.assertTrue(busca(arvore10,20))
        self.assertTrue(busca(arvore10,7))
        self.assertFalse(busca(arvore10,8))
        
    def test_103a_busca(self):
        self.assertTrue(busca(arvore10,12))
        self.assertTrue(busca(arv_torta,10))
        self.assertTrue(busca(arv_torta,9))
        self.assertFalse(busca(arv_torta,8))

    def test_103b_busca_arvore_vazia(self):
        self.assertFalse(busca({},12))
        self.assertFalse(busca({},10))
        self.assertFalse(busca({},9))
        self.assertFalse(busca({},8))
        
    def test_104a_insere(self):
        d5 = {'raiz':5,'esquerda':{},'direita':{}}
        insere(d5,2)
        insere(d5,7)

        self.assertEqual(d5, arvore5)
        d10 = {'raiz':10,'esquerda':{},'direita':{}}
        insere(d10,10)
        insere(d10,5)
        insere(d10,2)
        insere(d10,7)
        insere(d10,20)
        insere(d10,12)
        insere(d10,30)
        self.assertEqual(d10, arvore10)

    def test_104b_insere_comecando_vazio(self):
        d2={}
        insere(d2,2)
        self.assertEqual(d2, arvore2)
        d5 = {}
        insere(d5,5)
        insere(d5,2)
        insere(d5,7)
        self.assertEqual(d5, arvore5)
        d10 = {}
        insere(d10,10)
        insere(d10,5)
        insere(d10,2)
        insere(d10,7)
        insere(d10,20)
        insere(d10,12)
        insere(d10,30)
        self.assertEqual(d10, arvore10)

    def test_105_insere_repetida(self):
        d10 = {}
        insere(d10,10)
        insere(d10,5)
        insere(d10,2)
        insere(d10,7)
        insere(d10,20)
        insere(d10,12)
        insere(d10,30)
        insere(d10,10)
        insere(d10,5)
        insere(d10,20)
        insere(d10,30)
        self.assertEqual(d10, arvore10)

    def test_106_conta(self):
        self.assertEqual(conta(arvore10),7)
        self.assertEqual(conta(arvore5),3)
        self.assertEqual(conta(arvore2),1)
        self.assertEqual(conta({}),0)
        self.assertEqual(conta(ex3),5)


    def test_107_soma(self):
        self.assertEqual(soma(ex1),71)
        self.assertEqual(soma(ex2),15)
        self.assertEqual(soma(ex3),335)
        self.assertEqual(soma({}),0)

    def test_108_maior(self):
        self.assertEqual(maior(ex1),20)
        self.assertEqual(maior(ex2),10)
        self.assertEqual(maior(ex3),120)

    def verifica_resposta(self,resposta,codigo_correto):
        #print('verificando',resposta)
        codigo_resp_aluno = hashlib.sha224(str(resposta).encode('utf-8')).hexdigest()
        self.assertEqual(codigo_resp_aluno,codigo_correto)
        
        

    
    
def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

try:
    from gabarito  import *
except:
    pass

runTests();