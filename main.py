linguagens = ["python","java","c++","java script"]
linguagens[3] = "hust"
print(linguagens)
linguagens.append("java script")
print(linguagens)
linguagens.insert(0,"c#")
print(linguagens)
del linguagens[2]
print(linguagens)
linguagens.pop()
print(linguagens)
linguagens.remove("c++")
print(linguagens)
len(linguagens)
#listas são mutaveis
print("-:-"*30)
valores = list(range(4,11))
print(valores)
valores.sort()
print(valores)
valores.sort(reverse=True)
print(valores)
print("-:-"*30)
#dados = ["pedro",25,]
dados = list() 
dados.append("pedro")
dados.append("25")
print(dados[0])
print(dados[1])
pessoas = list()
pessoas.append(dados[:])
print(pessoas)
pessoas.append("maria")
pessoas.append(19)
print(pessoas)
pessoas.append("joão")
pessoas.append(32)
print(pessoas)
pessoas = [["pedro", 25],["maria",19],["joão", 32] ]
print(pessoas)
print(pessoas[0][0])
print(pessoas[1][0])
print(pessoas[2][0])
print(pessoas[1])
