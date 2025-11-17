#1- Crie uma classe chamada Personagem.

#2- O método construtor (__init__) deve receber nome e classe (ex: "Guerreiro", "Mago") como parâmetros.

#3- Todo personagem novo deve nascer com o atributo vida valendo 100 (não receba isso como parâmetro, defina fixo lá dentro).

#4- Crie um método tomar_dano que recebe um valor numérico e subtrai esse valor da vida do personagem.

#5- Crie um método ver_status que retorna uma frase: "O [nome] está com [vida] de HP".

class Personagem:

  def __init__(self, nome, classe):
    self.nome = nome
    self.classe = classe
    self.vida = 100

  def dano(self, valor):
    self.vida = self.vida - valor
    return self.vida
  
  def status(self):
    return f"O {self.nome} está com a {self.vida} de HP"
  
sven = Personagem(nome="Sven Sparrow", classe="Guerreiro")
sven.dano(38)
sven.dano(38)
sven.dano(8)
print(sven.status())