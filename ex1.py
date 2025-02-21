class Veiculo:
    def __init__(self, marca, modelo, ano, ligado=False):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = ligado

    def apresentar(self):
        print("\n")
        print("-" * 20)
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")
        print("Ligado" if self.ligado else "Desligado")

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"{self.modelo} foi ligado.")
        else:
            print(f"{self.modelo} já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"{self.modelo} foi desligado.")
        else:
            print(f"{self.modelo} já está desligado.")


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas, ligado=False):
        super().__init__(marca, modelo, ano, ligado)
        self.cilindradas = cilindradas

    def empinar(self):
        if self.ligado:
            print(f"{self.modelo} está empinando!")
        else:
            print(f"{self.modelo} precisa estar ligado para empinar.")

    def apresentar(self):
        super().apresentar()
        print(f"Cilindradas: {self.cilindradas}")


veiculo1 = Veiculo("Toyota", "Corolla", 2022)
veiculo1.apresentar()
veiculo1.ligar()
veiculo1.apresentar()
veiculo1.desligar()

moto1 = Moto("Honda", "CBR 600RR", 2021, "600cc")
moto1.apresentar()
moto1.ligar()
moto1.empinar()
moto1.desligar()

