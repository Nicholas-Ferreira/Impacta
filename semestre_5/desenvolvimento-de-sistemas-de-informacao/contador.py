
def contador(string):
  dic = dict()
  for i in string.split(" "):
    if i in dic.keys():
      dic[i] += 1
    else:
      dic[i] = 1
  print(dic)


contador("esse exercicio é um exercicio facil ou dificil")