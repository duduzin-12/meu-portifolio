#1- Filtro: Selecione apenas as peças que custam R$ 100,00 ou mais.

#2- Cálculo: Para essas peças, aplique um desconto de 20% (dica: multiplicar por 0.8 dá o valor já com desconto).

#3- Formatação: O valor final deve ser uma string com 2 casas decimais (use o que aprendeu sobre f-strings: f"{valor:.2f}").

#4- Saída (Output): Crie uma nova lista de dicionários contendo apenas as chaves peca e preco_black_friday. Não altere a lista original!

estoque = [
    {"peca": "Kit Embreagem Civic", "preco": 800.00, "estoque": 5},
    {"peca": "Cheirinho Carro Novo", "preco": 15.00, "estoque": 50},
    {"peca": "Amortecedor Dianteiro", "preco": 450.00, "estoque": 10},
    {"peca": "Lampada Farol", "preco": 25.00, "estoque": 100},
]

nova_lista = []

for itens in estoque:
  if itens["preco"] >= 100.00:
    desconto = itens["preco"] * 0.8

    blackfriday_itens = {
      "peca": itens["peca"],
      "preco": f"{desconto:.2f}"
    }

    nova_lista.append(blackfriday_itens)

print(nova_lista)