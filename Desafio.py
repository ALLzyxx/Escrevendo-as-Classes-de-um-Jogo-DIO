class HEROI:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
    def ataque(self):
        if self.tipo.lower() == "mago":
            ataque = "magia"
        elif self.tipo.lower() == "guerreiro":
            ataque = "espada"
        elif self.tipo.lower() == "monge":
            ataque = "artes marciais"
        elif self.tipo.lower() == "ninja":
            ataque = "shuriken"
        else:
            ataque = "ataque desconhecido"
        print(f"O {self.tipo} atacou usando {ataque}.")

Heroi = HEROI(input("Digite o Nome:\n"), input("Digite a Idade:\n"), input("Digite a Classe:\n"))
Heroi.ataque()
