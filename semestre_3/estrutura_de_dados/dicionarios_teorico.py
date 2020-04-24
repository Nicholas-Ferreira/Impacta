'''
As próximas duas funções devem resolver
um mesmo problema de duas
formas diferentes: uma sem dicionarios,
e uma com

O problema é o seguinte: temos uma lista
e queremos saber se algum par de elementos
da lista soma 13.

Definiremos uma funcao casal_13 para isso

por exemplo

casal_13([1,2,3]) retorna False,
porque não existe nenhum par na lista
que somado dá 13.

casal_13([1,2,3,4,5,6,7,8,9,10])
retorna True, porque existe um par
de números da lista que soma 13
(o 3 e o 10, por exemplo, ou o 4 e o 9)

'''

'''
Primeiro, definiremos uma funcao
casal_13(lista)
que faz isso sem usar dicionarios.

Vou deixar ela pronta pra você.
A lógica é a seguinte:
    estou procurando o 13.
    se estou olhando para o 5, 
    basta descobrir se o 8 está na lista.
    Se não, devo tentar a mesma coisa
    para o próximo número
'''
def casal_13(lista):
    for n in lista:
        if 13-n in lista:
            return True
    return False


'''
Depois, definiremos uma funcao
casal_13_dic  
quando recebe uma lista [1,2,5,8]
monta um dicionário:
{1:True,2:True,5:True,8:True}

Ou seja, que monta um dicionário
onde as chaves são os números
da lista, e os valores sao todos True.

Com isso, podemos verificar rapidamente
se os números estavamna lista.
É só verificar que eles sao chaves
do dicionário.

Para ver se o 6 está
no dicionário, usamos "if 6 in dicionario"

Ou seja, como procurando o 13,
se estivermos olhando para
o número 3 (num for percorrendo a lista),
basta ver se "10 in dicionario"
'''



def casal_13_dic(lista):
    dic = {}
    for n in lista:
      dic[n] = True

    for n in lista:
      if 13-n in dic:
        return True

    return False


'''
Depois que você rodar o runTests e
se certificar que a sua
função casal_13_dic
está passando, façamos o seguinte

comparemos a funcao casal_13_dic
com a casal_13,
em termos de eficiência
rode o seguinte:
> escolhe_valor(1000) #(pega uma lista com 1000 elementos)
> testa_tempos() 
depois aumente o tamanho da lista para 2000, 4000 e 8000

Os tempos do dicionário devem estar sendo bem menores do que os da lista
Se nao ser certo, me chame
'''

'''
Agora, vamos realizar outra tarefa, que é bem mais rápida
com dicionários do que sem: Descobrir se duas palavras sao
anagramas. 

dizemos que uma palavra2 é um anagrama de uma palavra1 quando 
palava2 é um "embaralhamento" das letras de palavra1.
por exemplo 'banana' e 'nabana'.
outro exemplo 'abb' e 'bba'.
um exemplo que não  é anagrama: 'baa' e 'abb'
implementaremos 2 formas diferentes de detectar se 
uma string2 é um anagrama de string1.
'''

'''
A primeira coisa a fazer é usar um dicionário para contar as 
letras de uma palavra
'''

'''
Abaixo, temos um exemplo, onde o dicionario conta as letras da 
palavra banana
'''
dici_banana = {'b':1,'n':2,'a':3}

'''
Preencha os dicionarios a seguir com as contagens
de letras de "ataca" e "leve"
'''
dici_ataca = {'a': 3, 't': 1, 'c': 1}
dici_leve = {'l': 1, 'e': 2, 'v': 1}

'''
faça uma funcao que conta as letras de uma string
por exemplo, 'banana' tem 3 letras 'a'
 a funcao recebe uma string e devolve um dicionário
 por exemplo, conta_letras('banana') devolve {'b':1,'a':3,'n':2}
'''

'''
dica:  use os exemplos para lembrar como manipular dicionarios
        >>> d1={} #cria dicionario vazio
        >>> d1['a']=2 #associa chave 'a' a valor 2 
        >>> d1
        {'a': 2}
        >>> d1['b']=5 #associa chave 'b' a valor 5
        >>> d1
        {'a': 2, 'b': 5}
        >>> d1['b']
        5
        >>> pegar = d1['a'] #consulta o valor da chave 'a'
        >>> pegar
        2
        >>> d1['a'] = d1['a']+1 #aumentei o valor da chave 'a' em 1
        >>> d1
        {'a': 3, 'b': 5}
        >>> 'a' in d1 #verifica se 'a' é uma chave
        True
        >>> 'c' in d1 #verifica se 'b' é uma chave
        False
        >>> d1['c'] #dá pau se voce acessa uma chave inexistente
        Traceback (most recent call last):
          File "<pyshell#2>", line 1, in <module>
            d1['c']
        KeyError: 'c' 
'''
def conta_letras(string):
    dicti = {}
    for s in string:
      if s in dicti:
        dicti[s] += 1
      else:
        dicti[s] = 1
    return dicti


'''
Crie uma função iguais que recebe dois dicionarios,
e retorna True se eles forem iguais (têm as mesmas chaves,
o valor associado a uma mesma chave é igual nos dois)
'''
def iguais(d1,d2):
  return d1 == d2


'''
crie uma função conta e compara que recebe string1 e string2 
e retorna True se elas sao anagramas uma  da outra, False caso contrário

 por exemplo, conta e compara('aab','abb') deve retornar False
 por exemplo, conta e compara('aab','aba') deve retornar True

Faça isso da seguinte maneira: crie um dicionário d1 e um dicionario d2. 
Para cada caractere c, d1[c] deverá conter o número de ocorrencias 
do caractere c na string 1.

 Por exemplo, se string1='banana', então d1['a'] == 3, d1['b'] == 1

 Se as duas strings tiverem as mesmas letras, 
 e cada letra ocorrendo o mesmo número de vezes, 
 são anagramas uma  da outra. Caso contrário, não são.
 
'''
def conta_e_compara(string1,string2):
    d1 = conta_letras(string1)
    d2 = conta_letras(string2)
    return iguais(d1, d2)

'''
Agora vamos nos preparar para a segunda solução de "anagramas".

Primeiro, escreva uma função que recebe uma string e devolve uma 
lista das letras da string, em ordem

Os seguintes exemplos podem ser uteis
>>> palavra  = 'antigo'
>>> for c in palavra:
	print(c)
a
n
t
i
g
o
>>> lista = []
>>> lista.append('a')
>>> lista.append('n')
>>> lista
['a', 'n']
'''

def vira_lista(string):
  a = []
  for s in string:
    a.append(s)
  return a


'''
Agora, façamos uma função posicoes 
que chama a funcao "fotografa" para 
cada letra de uma string e sua posicao.

Por exemplo, para a string 'gato', serão
feitas as seguintes chamadas:
    fotografa((0,'g'))
    fotografa((1,'a'))
    fotografa((2,'t'))
    fotografa((2,'o'))

Repare o parênteses dobrado! É assim mesmo!
Estou passando uma tupla com 2 elementos para a
função fotografa

O código abaixo talvez ajude
>>> string = 'bruce'
>>> for i in range(len(string)):
	print(i)
0
1
2
3
4
>>> string[2]
'u'

Nao use funcoes magicas do python, como "index" e "remove"
'''
def posicoes(string):
  for i, s in enumerate(string):
    fotografa((i, s))


'''
Agora, faça uma funcao perde_a que recebe uma string e devolve uma
lista.

Essa lista tem todas as letras da string, menos o **primeiro a**
Esse primeiro a é trocado pela string ' '

por exemplo perde_a('banana') = ['b', ' ', 'n', 'a', 'n', 'a']
por exemplo perde_a('abana') = [' ', 'b', 'a', 'n', 'a']

Se a palavra não tiver nenhuma letra 'a', sua função deve retornar False
em vez da lista

Nao use funcoes mágicas do python, como "index" e "remove"
'''
def perde_a(string):
  if 'a' not in string:
    return False

  lis = []
  a = True
  for s in string:
    if a and s == 'a':
      a = False
      s = ' '
    lis.append(s)
  return lis

'''
vamos criar uma função vai_apagando que recebe string1 e string2 
e retorna True se elas sao anagramas uma da outra.
 Ela deve fazer isso da seguinte maneira:
 1. Crie uma lista2 com cada um dos caracteres 
 de string2 (se houver repetidos, eles devem aparecer 
             na lista repetidos)
 1a. A lista2 deve estar na mesma ordem da string2
 2. Para cada caractere na string1, procure na lista2. 
    Se ele estiver lá, troque a primeira ocorrência por ' '
 3. Se você conseguir achar os caracteres da string1, 
    e não sobrou nenhum caractere na lista2, 
    string1 e string2 eram anagramas.
 4. Devolva: True ou False (se sao ou nao anagramas)
'''

'''
Mas antes de fazermos isso, vamos simular um pouco 
o que deve ocorrer

se a gente chamar vai_apagando('xkcd','dckx')
a lista2 vai ser, em sequencia
['c', 'd', 'k', 'x']
['c', 'd', 'k', ' ']
['c', 'd', ' ', ' ']
[' ', 'd', ' ', ' ']
[' ', ' ', ' ', ' ']
E o retorno será True

Se a gente chamar vai_apagando('dinossaur','nosdina'),
lista2 vai ser, em sequencia
['n', 'o', 's', 'd', 'i', 'n', 'a']
['n', 'o', 's', ' ', 'i', 'n', 'a']
['n', 'o', 's', ' ', ' ', 'n', 'a']
[' ', 'o', 's', ' ', ' ', 'n', 'a']
[' ', ' ', 's', ' ', ' ', 'n', 'a']
[' ', ' ', ' ', ' ', ' ', 'n', 'a']

E o retorno será False (não achei o segundo s)

Se a gente chamar vai_apagando('ala','sala')
lista2 vai ser, em sequencia
['s', 'a', 'l', 'a']
['s', ' ', 'l', 'a']
['s', ' ', ' ', 'a']
['s', ' ', ' ', ' ']
E o retorno será False (sobrou gente na lista2)

Se a gente chamar vai_apagando('gata','ataga'),
quais serao as primeiras lista2, em ordem?
'''
primeira_lista2 = ['a','t','a','g','a']
segunda_lista2 =  ['a','t','a',' ','a']
terceira_lista2 = [' ','t','a',' ','a']

'''
Agora estamos prontos para fazer a funcao!
'''
def perde_letra(string, letra):
  lis = []
  i = True
  for s in string:
    if i and s == letra:
      i = False
      s = ' '
    lis.append(s)
  return lis

def vai_apagando(string1,string2):
  if string1 == string2:
    return True
  if string2 == '':
    return False

  string2 = vira_lista(string2)
  for s in string1:
    fotografa(string2)
    string2 = perde_letra(string2, s)
  for s in string2:
    if s != ' ':
      return False
  return True
  
'''
Depois que você rodar o runTests e
se certificar que a sua
função conta_e_compara
está passando, façamos o seguinte

comparemos a funcao conta_e_compara
com a vai_apagando,
em termos de eficiência
rode o seguinte:
> escolhe_valor(1000) #(monta duas strings iguais, com 1000 elementos)
> testa_tempos_anagrama() 
depois aumente o tamanho da string para 2000, 4000 e 8000

Os tempos do dicionário devem estar sendo bem menores do que os da lista
Se nao ser certo, me chame

'''



# DESAFIO crie uma função gera_e_compara que recebe string1 e string2 e retorna True se elas sao anagramas uma da outra.
# ISSO É UM DESAFIO, não vai ser fácil :)
# a função deve fazer o seguinte:
#1. Gerar todos os anagramas possiveis de string1 e colocá-los numa lista_de_anagramas
#2. Retornar True se string2 está na lista_de_anagramas, e False caso contrário
#3. Retornar também a lista de anagramas
# Por exemplo, gera_e_compara('abc','bca') retorna (True,['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
# Não se preocupe com a ordem da lista de anagramas, e pode repetir ou  não, como quiser.

import itertools
def gera_e_compara(string1,string2):
  anagramas = []
  for anagrama in itertools.permutations(string1):
    anagramas.append(''.join(anagrama))
  return (conta_e_compara(string1, string2),anagramas)


'''
a partir daqui nao ha nada para voce implementar
'''

import random
import time
def gera_vetor(nmax):
    a = []
    i=0
    while(i<nmax):
       a.append(i*100)
       i += random.randint(1,2)
    return a

def escolhe_valor(valor_max_novo):
  global valor_max
  global vetor
  global string_as
  valor_max = valor_max_novo
  print ('a entrada agora tem '+str(valor_max)+' valores')
  vetor = gera_vetor(valor_max)
  string_as = 'a'*valor_max

#escolhe_valor(1000)


def simula1():
   print('testando casal_13 - versao O(n**2) (sem dicionario)')
   start=time.process_time()
   for i in range(1,10):
      casal_13(vetor)
   end = time.process_time()
   return end-start

def simula2():
   print('testando casal_13_dic - versao O(n) (dicionario)')
   start=time.process_time()
   for i in range(1,100):
      casal_13_dic(vetor)
   end = time.process_time()
   return end-start

def simula_anagrama_1():
   print('testando vai_apagando - anagramas versao O(n**2) (sem dicionario)')
   start=time.process_time()
   for i in range(1,10):
      vai_apagando(string_as,string_as)
   end = time.process_time()
   return end-start

def simula_anagrama_2():
   print('testando conta_e_compara - anagramas versao O(n) (com dicionario)')
   start=time.process_time()
   for i in range(1,10):
      conta_e_compara(string_as,string_as)
   end = time.process_time()
   return end-start



    
    
#para testar velocidades, use escolhe_valor, testa1 e testa2

def testa_tempos():
    try:
       r2 = simula2()
    except NameError:
        print('voce rodou a funcao escolhe_valor(1000)?')
        return  
    print('{0:.20f}'.format(r2))
    r1 = simula1()
    print('{0:.20f}'.format(r1))
    
def testa_tempos_anagrama():
    try:
       r2 = simula_anagrama_2()
    except NameError:
        print('voce rodou a funcao escolhe_valor(1000)?')
        return  
    print('{0:.20f}'.format(r2))
    r1 = simula_anagrama_1()
    print('{0:.20f}'.format(r1))

import unittest
import hashlib

class TestStringMethods(unittest.TestCase):
    def test_01_casal_13(self):
        self.assertTrue(casal_13([1,2,3,12]))
        self.assertFalse(casal_13([1,2,3,9,7]))
        self.assertTrue(casal_13([4,2,3,1,9]))
        self.assertTrue(casal_13([20,30,0,13]))
        self.assertFalse(casal_13([10,2,1]))
        self.assertTrue(casal_13([11,2]))
        self.assertTrue(casal_13([-7,2,3,4,20,2]))

    def test_01_casal_13_dic(self):
        self.assertTrue(casal_13_dic([1,2,3,12]))
        self.assertFalse(casal_13_dic([1,2,3,9,7]))
        self.assertTrue(casal_13_dic([4,2,3,1,9]))
        self.assertTrue(casal_13_dic([20,30,0,13]))
        self.assertFalse(casal_13_dic([10,2,1]))
        self.assertTrue(casal_13_dic([11,2]))
        self.assertTrue(casal_13_dic([-7,2,3,4,20,2]))
    
    def test_10_dicionarios(self):
        c11='ac588cb9f8db52ffeb736ec620e40b801bf43db84e06102731fcc29a'
        c12='f3ae5edbcbc592d6a22c3fa7f34eee0fc6cc3f290e946d6ce8c87c6e'
        c21='24f372ec57c9311b9f67dfe6254f61eb9e6af53d2facb4c7a8f18c5f'
        c22='309bfe1cf5b6c79488a78668eddaa24faa358365b963b993435a0613'
        if type(dici_ataca) != type({1:2}):
            self.fail('dici_ataca nao é dicionario')
        if type(dici_leve) != type({1:2}):
            self.fail('dici_leve nao é dicionario')
        self.verifica_dicionario(dici_ataca,c11,c12)
        self.verifica_dicionario(dici_leve,c21,c22)


    def test_11_conta_letras(self):
        testes = [('banana',{'b':1,'a':3,'n':2}),
                  ('nabana',{'b':1,'a':3,'n':2}),
                  ('abb',{'b':2,'a':1}),
                  ('baa',{'b':1,'a':2}),
                  ('',{})
                  ]
        for teste in testes:
             self.assertEqual(conta_letras(teste[0]),
                                   teste[1])
    

    def verifica_anagrama(self,func):
        self.assertEqual(func('banana','nabana'),True)
        self.assertEqual(func('banaaa','nabana'),False)
        self.assertEqual(func('banana','nabann'),False)
        self.assertEqual(func('',''),True)
        self.assertEqual(func('','a'),False)
        self.assertEqual(func('a',''),False)

    def test_12_dicionarios_iguais(self):
        self.assertTrue(iguais({},{}))
        self.assertTrue(iguais({'a':2,'b':5},{'a':2, 'b':5}))
        self.assertTrue(iguais({'a':2,'b':5, 'c':1},{'a':2, 'b':5, 'c':1}))
        self.assertFalse(iguais({'a':2,'b':5, 'c':10},{'a':2, 'b':5, 'c':1}))
        self.assertTrue(iguais({'a':2,'b':5, 'c':10},{'a':2, 'b':5, 'c':10}))
        self.assertFalse(iguais({'a':2,'b':5},{'a':2, 'b':5, 'c':10}))
        self.assertFalse(iguais({},{'a':2, 'b':5, 'c':10}))
        self.assertFalse(iguais({},{'c':10}))

    def test_13_conta_e_compara(self):
        self.assertEqual(conta_e_compara('banana','nabana'),True)
        self.assertEqual(conta_e_compara('banaaa','nabana'),False)
        self.assertEqual(conta_e_compara('banana','nabann'),False)
        self.assertEqual(conta_e_compara('',''),True)
        self.assertEqual(conta_e_compara('','a'),False)
        self.assertEqual(conta_e_compara('a',''),False)

    def test_20_vira_lista(self):
        self.assertEqual(vira_lista('banana'),['b','a', 'n', 'a', 'n', 'a'])
        self.assertEqual(vira_lista('ban'),['b','a', 'n'])
        self.assertEqual(vira_lista('ana'),['a', 'n', 'a'])
        self.assertEqual(vira_lista(''),[])

    def test_21_posicoes(self):
        reseta_fotos()
        posicoes('ban')
        resposta = [(0, 'b'), (1, 'a'), (2, 'n')]
        fotos_aluno = fotografias
        if not fotos_aluno == resposta:
            explica_erro(fotos_aluno,resposta)
            self.fail('fotos incorretas')
        reseta_fotos()
        posicoes('fria')
        resposta = [(0, 'f'), (1, 'r'), (2, 'i'), (3, 'a')]
        fotos_aluno = fotografias
        if not fotos_aluno == resposta:
            explica_erro(fotos_aluno,resposta)
            self.fail('fotos incorretas')


    def test_22_perde_a(self):
        self.assertEqual(perde_a('banana'),['b',' ', 'n', 'a', 'n', 'a'])
        self.assertEqual(perde_a('ban'),['b',' ', 'n'])
        self.assertEqual(perde_a('ana'),[' ', 'n', 'a'])
        self.assertEqual(perde_a('sopa'),['s', 'o', 'p', ' '])
    
    def test_22a_perde_a_da_false(self):
        self.assertEqual(perde_a('todo'),False)
        self.assertEqual(perde_a('gomes'),False)
        self.assertEqual(perde_a('outro'),False)

    def test_23_listas2_ataga(self):
        cod_primeira_correto = '88185bb9f6e445cc3f9e726e1d0c0db4d97365e3de6924ea90f4921b'
        cod_segunda_correto = '0f47670ea3e44c6fd2ee7a3b50e36de5ef218d3bf89f212eeeaa4b1e'
        cod_terceira_correto = '219ad298a4e8e1a849e5491f8bdf2542a15d1f14d7c4088ce1522a02'
        self.verifica_lista(primeira_lista2,cod_primeira_correto)
        self.verifica_lista(segunda_lista2,cod_segunda_correto)
        self.verifica_lista(terceira_lista2,cod_terceira_correto)

        
    def test_24_vai_apagando_fotografias(self):
        reseta_fotos()
        vai_apagando('banana','nabana')
        resposta = [['n', 'a', 'b', 'a', 'n', 'a'],
                    ['n', 'a', ' ', 'a', 'n', 'a'],
                    ['n', ' ', ' ', 'a', 'n', 'a'],
                    [' ', ' ', ' ', 'a', 'n', 'a'],
                    [' ', ' ', ' ', ' ', 'n', 'a'],
                    [' ', ' ', ' ', ' ', ' ', 'a'],
                    [' ', ' ', ' ', ' ', ' ', ' '],
                    ]
        fotos_aluno = fotografias
        if not (fotos_aluno == resposta or fotos_aluno == resposta[:-1]):
            explica_erro(fotos_aluno,resposta)
            self.fail('fotos incorretas')
    
    def test_25_vai_apagando_teste2(self):
        self.assertEqual(vai_apagando('banana','nabana'),True)
        self.assertEqual(vai_apagando('banaaa','nabana'),False)
        self.assertEqual(vai_apagando('banana','nabann'),False)
        self.assertEqual(vai_apagando('',''),True)
        self.assertEqual(vai_apagando('','a'),False)
        self.assertEqual(vai_apagando('a',''),False)

    def test_30_gera_e_compara(self):
        def versao_true_false(string1,string2):
            return gera_e_compara(string1,string2)[0]
        self.verifica_anagrama(versao_true_false)
        a = gera_e_compara('abc','cba')
        self.assertEqual(a[0],True)
        self.assertEqual(set(a[1]),set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        a = gera_e_compara('abcd','cbaa')
        self.assertEqual(a[0],False)
        self.assertEqual(set(a[1]),set(['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']))
        a = gera_e_compara('abca','cbaa')
        self.assertEqual(a[0],True)
        self.assertEqual(set(a[1]),set(['abca', 'abac', 'acba', 'acab', 'aabc', 'aacb', 'baca', 'baac', 'bcaa', 'bcaa', 'baac', 'baca', 'caba', 'caab', 'cbaa', 'cbaa', 'caab', 'caba', 'aabc', 'aacb', 'abac', 'abca', 'acab', 'acba']))

    def verifica_dicionario(self,d1,codigo1_correto,codigo2_correto):
        chaves = sorted([str(x) for x in d1.keys()])
        codigo1_aluno = hashlib.sha224(str(chaves).encode('utf-8')).hexdigest()
        valores = sorted([str(x) for x in d1.values()])
        codigo2_aluno = hashlib.sha224(str(valores).encode('utf-8')).hexdigest()
        self.assertEqual(codigo1_aluno,codigo1_correto)
        self.assertEqual(codigo2_aluno,codigo2_correto)


    def verifica_lista(self,lista,codigo_correto):
        codigo_aluno = hashlib.sha224(str(lista).encode('utf-8')).hexdigest()
        self.assertEqual(codigo_aluno,codigo_correto)
    


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


fotografias = []
def reseta_fotos():
    global fotografias
    fotografias = []

def fotografa(elemento):
    try:
        copia = elemento.copy()
    except:
        copia = elemento
    fotografias.append(copia)

def explica_erro(f_aluno,f_resposta):

    print('')

    if len(f_aluno) == 0 and len(f_resposta) > 0:
        print('Você não tirou nenhuma fotografia')
        print('Primeira fotografia esperada:')
        print(f_resposta[0])
        return


    tam_do_menor = min(len(f_aluno),len(f_resposta))
    diferentes = [i for i in range(tam_do_menor) if f_aluno[i] != f_resposta[i]]
    if len(diferentes) > 0:
        menor_diferente = min(diferentes)
        print('Suas primeiras ' + str(menor_diferente) + ' fotografias estao certas')
        print('Suas fotografias corretas:')
        for j in range(menor_diferente):
            print(f_aluno[j])
        print('Sua primeira fotografia errada:')
        print(f_aluno[menor_diferente])
        print('Era esperado:')
        print(f_resposta[menor_diferente])
        return

    if len(f_aluno) < len(f_resposta):
        print('Você tirou fotografias a menos')
        print('Voce tirou '+str(len(f_aluno))+ ' fotografias, mas era pra tirar ' + str(len(f_resposta)))
        menor_diferente = len(f_aluno)
        print('Suas primeiras ' + str(menor_diferente) + ' fotografias estao certas')
        print('Suas fotografias corretas:')
        for j in range(menor_diferente):
            print(f_aluno[j])
        print('A primeira fotografia que faltou:')
        print(f_resposta[menor_diferente])

    if len(f_aluno) > len(f_resposta):
        print('Você tirou fotografias a mais')
        print('Voce tirou '+str(len(f_aluno))+ ' fotografias, mas era pra tirar ' + str(len(f_resposta)))
        menor_diferente = len(f_resposta)
        print('Suas primeiras ' + str(menor_diferente) + ' fotografias estao certas')
        print('Suas fotografias corretas:')
        for j in range(menor_diferente):
            print(f_aluno[j])
        print('A primeira fotografia que sobrou:')
        print(f_aluno[menor_diferente])

runTests()