#1- Crie uma classe ContaBancaria.

#2- O __init__ recebe o titular (nome) e começa com saldo igual a 0 (zero).

#3- Crie um método depositar(valor): Adiciona dinheiro ao saldo.

#4- Crie um método sacar(valor): Só subtrai do saldo SE tiver dinheiro suficiente.

#5- Se tiver saldo: diminui e retorna True (ou printa "Saque OK").

#6- Se não tiver saldo: não faz nada e retorna False (ou printa "Saldo Insuficiente").

#7- Crie um método extrato(): Retorna "Saldo de R$ X".

class ContaBancaria:
  def __init__(self, titular):
    self.titular = titular
    self.saldo = 0

  def depositar(self, valor):
    self.saldo += valor
    return self.saldo
  
  def sacar(self, valor):
    if self.saldo >= valor:
      self.saldo -= valor
      print("Saque liberado.")
      return self.saldo
    else:
      print("Saldo insuficiente.")

  def extrato(self):
    return f"O saldo de {self.titular} é de R${self.saldo:.2f}"
  
eduardo = ContaBancaria(titular="Eduardo")
eduardo.depositar(10000)
eduardo.sacar(3450)
print(eduardo.extrato())
eduardo.sacar(10000)