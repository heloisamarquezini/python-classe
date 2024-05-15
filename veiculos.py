class Veículo:
    def ___init___(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo 
        self.ano = ano 

    def imprimir(self):
        print("marca:", self.marca) 
        print("modelo:", self.modelo)
        print("ano:", self.ano)  
        
    def ligar(self):
        print("Veículo ligado") 

    def desligar(self):
        print("Veículo desligado")

    
class Carro(Veículo):
    def __init__(self, marca, modelo, ano, numeroDePortas):
        super() .__init__(marca, modelo, ano)
        self.numeroDePortas = numeroDePortas

    def NumeroDePortas(self):
        print("O Carro possui:", self.numeroDePortas)

class Moto(Veículo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super() .__init__(marca, modelo, ano)
        self.cilindradas = cilindradas
    def Cilindradas(self):
        print("A Moto possui:",self.cilindradas)

renault = Veículo("renault", "duster", 2000)

chevrolet = Carro("chevrolet", "tracker", 2020, 4)

honda = Moto("honda","twister", 2024, 293,5 )


renault.imprimir()
chevrolet.imprimir()
honda.imprimir()
renault.ligar()
renault.desligar()