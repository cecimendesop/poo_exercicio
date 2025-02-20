class Moto:
    def __init__(self, marca, ano, tipo, valor, nova=True):
        self.marca = marca
        self.ano = ano
        self.tipo = tipo
        self.valor = 0
        self.nova = nova


    def acelerar(self):
        print("\n")
        print("-" * 20)
        print(self.marca, self.tipo, self.valor, self.ano)
        if self.:
            print(f"Estudando")
        else:
            print(f"Não está estudando")

    def abastecer(self):
        if self.estudando and self.trabalhando:
            print(f"Estudando e Trabalhando então recebeu um aumento de salário")
            self.salario += 1000
        elif self.estudando:
            print("Está estudando")
        else:
            print("Não está estudando")

    def revisar(self):
        if not self.trabalhando:
            self.trabalhando = True
            self.salario += 100
            print(f"{self.nome} Começar a trabalhar")
        else:
            print(f"{self.nome} Já está trabalhando")



class Bebe(Pessoa):
    def __init__(self, nome, data_nasc, codigo, estudando=False, trabalhando=False, fome=True, chorando=True,
                 dormindo=False):
        super().__init__(nome, data_nasc, codigo, estudando, trabalhando, fome, chorando, dormindo)
        self.fome = True
        self.chorando = True
        self.dormindo = False

    def mamar(self):
        if self.fome:
            print("O bebê está mamando")
            self.fome = False
            self.chorando = False
        else:
            print("O bebê está satisfeito")
            self.fome = False


    def chorar(self):
        if self.chorando:
            print("O bebê está chorando porque quer mamar")
            self.fome = True
            self.dormindo = False
        else:
            print("Ele não está chorando")
            self.chorando = False

    def dormir(self):
        if self.dormindo:
            print("Ele está com fome, por isso não está dormindo")
        else:
            if self.fome:
                print("O bebê ainda não comeu, então não pode dormir")
            else:
                print("Ele está dormindo")
                self.dormindo = True

    def acordar(self):
        if self.dormindo:
            self.fome = True
            self.chorando = True
            print("O bebê acordou e está chorando de fome")
        else:
            print("O bebê já está acordado")


p1 = Pessoa("Lucas",    "23/09/1990",   "jghfgjj")
p1.apresentar()
p2 = Pessoa("Lucas", "23/09/2000", "gjsdbfj")
p2.apresentar()
p3 = Pessoa("Lucas", "23/09/2005", "eshfier")
p3.apresentar()
p4 = Pessoa("Lucas", "23/09/2010", "udfsg")
p4.apresentar()


bebe1 = Bebe("Lucas", "23/09/1990", "jghfgjj")
bebe1.apresentar()
bebe1.acordar()
bebe1.chorar()
