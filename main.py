# NOTE: superclasse, classe-pai ou classe base veículo
class Veiculo:
    # atributos
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # método
    def mostrar_detalhes(self):
        print(f'Marca: {self.marca}.')
        print(f'Modelo: {self.modelo}.')


# NOTE: subclasse, classe-filha ou classe derivada carro
class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

# NOTE: subclasse moto
class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

# NOTE: função polimórfica
def mostrar_informacoes_veiculo(veiculo):
    veiculo.mostrar_detalhes()

# NOTE: programa principal
if __name__ == '__main__':
    carro = Carro('Ford', 'Fusion', 4)
    moto = Moto('Honda', 'CBR', 650)

    mostrar_informacoes_veiculo(carro)
    mostrar_informacoes_veiculo(moto)