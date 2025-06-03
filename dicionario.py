# Dicionários e listas


print("-" * 40)


filmes = ["Star Wars", 
          "Atack On Titan", 
          "Koe no Katachi", 
          "Espetacular Homem-Aranha"]

for n in filmes:
    print(f"Meus filmes favoritos são: {n}")

print("-" * 40)

# Exemplo de dicionário

livro = {
    "titulo": "Diario de um Banana",
    "autor": "Jeff Kinney",
    "ano": 2007,
}
print("titulo:", livro["titulo"])
print("Autor:", livro["autor"])
print("Ano:", livro["ano"])

print("-" * 40)

compras = ["camisa", "calça", "tênis", "cueca", "meias", "casaco", "moletom"]
compras.append("boné")
compras.insert(0, "óculos")
compras.remove("cueca")
for i in compras:
    print(i)

print("-" * 40)

# Exemplo de dicionário
alunos = {
    "nome": "Maynard Diogo",
    "idade": 20,
    "curso": "Python",
}
alunos["idade"] = 21

chave = "matricula"
alunos[chave] = "26116428"

for chave, valor in alunos.items():
    print(f"{chave}: {valor}")

print("-" * 40)