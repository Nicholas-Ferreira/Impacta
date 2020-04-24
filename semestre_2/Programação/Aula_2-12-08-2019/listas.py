list = [1,2,3,4,5]
x = 0 #elemento
L = [6, 7] 
i = 0 #index

list.append(x)
#Adiciona um item ao fim da lista; equivale a a[len(a):] = [x].

list.extend(L)
#Prolonga a lista, adicionando no fim todos os elementos da lista L passada como argumento; equivalente a a[len(a):] = L.

list.insert(i, x)
#Insere um item em uma posição especificada. O primeiro argumento é o índice do elemento antes do qual será feita a inserção, assim a.insert(0, x) insere no início da lista, e a.insert(len(a), x) equivale a a.append(x).

list.remove(x)
#Remove o primeiro item encontrado na lista cujo valor é igual a x. Se não existir valor igual, uma exceção ValueError é levantada.

list.pop(i)
#Remove o item na posição dada e o devolve. Se nenhum índice for especificado, a.pop() remove e devolve o último item na lista. (Os colchetes ao redor do i indicam que o parâmetro é opcional, não que você deva digitá-los daquela maneira. Você verá essa notação com frequência na Referência da Biblioteca Python.)

list.index(x)
#Devolve o índice do primeiro item cujo valor é igual a x, gerando ValueError se este valor não existe

list.count(x)
#Devolve o número de vezes que o valor x aparece na lista.

list.sort()
#Ordena os itens na própria lista in place.

list.reverse()
#Inverte a ordem dos elementos na lista in place (sem gerar uma nova lista).

len(list) # Tamanho
max(list) # Maior valor
min(list) # Menor valor

list = [item for item in list if item % 2 == 0]
print(list)