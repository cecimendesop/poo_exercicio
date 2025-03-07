class Veiculo:
    def __init__(self, marca, modelo, ano, ligado=False):
        self.__marca = marca
        self.modelo = modelo
        self.ano = ano
        self._ligado = ligado

    def get_marca(self):
        return self.__marca
    def set_marca(self, marca):
        if not self.__marca:
            self.__marca = marca
            print(f"A marca da moto é: {self.__marca}")
        else:
            print(f"Insira o marca da moto: {self.__marca}")

    def get_ligado(self):
        return self._ligado

    def apresentar(self):
        print("\n")
        print("-" * 20)
        print(f"Marca: {self.__marca}, Modelo: {self.modelo}, Ano: {self.ano}")
        print("Ligado" if self._ligado else "Desligado")

    def set_ligar(self):
        if not self._ligado:
            self._ligado = True
            print(f"{self.modelo} foi ligado.")
        else:
            print(f"{self.modelo} já está ligado.")

    def set_desligar(self):
        if self._ligado:
            self._ligado = False
            print(f"{self.modelo} foi desligado.")
        else:
            print(f"{self.modelo} já está desligado.")


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas, ligado=False):
        super().__init__(marca, modelo, ano, ligado)
        self.cilindradas = cilindradas

    def empinar(self):
        if self._ligado:
            print(f"{self.modelo} está empinando!")
        else:
            print(f"{self.modelo} precisa estar ligado para empinar.")

    def apresentar(self):
        super().apresentar()
        print(f"Cilindradas: {self.cilindradas}")


veiculo1 = Veiculo("Toyota", "Corolla", 2022)
veiculo1.apresentar()
veiculo1.set_ligar()
veiculo1.apresentar()
veiculo1.set_desligar()

moto1 = Moto("Honda", "CBR 600RR", 2021, "600cc")
moto1.apresentar()
moto1.set_ligar()
moto1.empinar()
moto1.set_desligar()

