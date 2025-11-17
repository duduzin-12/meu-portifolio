#1- Crie uma classe chamada Carro.

#2- O método construtor deve receber o modelo (ex: "Civic") e o ano (ex: 2004).

#3- Todo carro novo deve nascer com um atributo velocidade valendo 0 (zero).

#4- Crie um método chamado acelerar que recebe um valor e soma à velocidade atual do carro.

#5- Crie um método chamado exibir_painel que retorna (ou printa) uma frase dizendo: "O [modelo] está a [velocidade] km/h".

class Carro:
  
  def __init__(self, modelo, ano):
    self.modelo = modelo
    self.ano = ano
    self.velocidade = 0

  def acelerar(self, num):
    self.velocidade_atual = self.velocidade + num
  
  def exibirPainel(self):
    return f"O {self.modelo} está a {self.velocidade_atual}km/h"
  
civic = Carro(modelo="Civic", ano="2005")
civic.acelerar(150)
print(civic.exibirPainel())