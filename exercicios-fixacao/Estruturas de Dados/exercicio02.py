#1- Identifique os funcionários com nota maior que 8.0.

#2- Para esses funcionários, calcule o novo salário adicionando 10% ao valor original (multiplique por 1.1).

#3-O Grande Desafio (Output): Ao invés de uma lista de strings, eu quero que você retorne uma nova lista de dicionários, contendo apenas o nome e o novo salário.

funcionarios = [
    {"nome": "Pedro", "salario": 2000.00, "nota": 7.0},
    {"nome": "Bianca", "salario": 3000.00, "nota": 9.5},
    {"nome": "Marcos", "salario": 1500.00, "nota": 5.0},
    {"nome": "Luana", "salario": 4000.00, "nota": 8.5},
]

promocao = []

for func in funcionarios:
  if func["nota"] > 8.0:
    salario = func["salario"] * 1.1

    novo_quadro = {
      "nome": func["nome"],
      "salario": f"{salario:.2f}"
    }

    promocao.append(novo_quadro)

print(promocao)