#Requisitos:

#-1 Filtrar transações com valor maior que R$ 100,00 E com status "aprovado".

#-2 Retornar uma lista de strings com os nomes em maiúsculo.

transacoes = [
    {"id": 1, "cliente": "joao silva", "valor": 150.50, "status": "aprovado"},
    {"id": 2, "cliente": "maria souza", "valor": 50.00, "status": "aprovado"},
    {"id": 3, "cliente": "carlos lima", "valor": 500.00, "status": "pendente"},
    {"id": 4, "cliente": "ana pereira", "valor": 200.00, "status": "aprovado"},
]

clientes = []

for transacao in transacoes:
  if transacao["valor"] > 100.00 and transacao["status"] == "aprovado":
    clientes.append(transacao["cliente"].upper())

print(clientes)

# Usando o método List Comprehension
#clientes = [t["cliente"].upper() for t in transacoes if t["valor"] > 100 and t["status"] == "aprovado"]

cliente = [transacao["cliente"].upper() for transacao in transacoes if transacao["valor"] > 100 and transacao["status"] == "aprovado"]
print(clientes)