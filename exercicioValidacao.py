class Cadastro:
    Nome = None
    def __init__(self) -> None:
        pass
       
    def InserirNome (self, nome):
        nomePreenchido = self.ValidaNome (nome)
        if nomePreenchido == True:
            self.nome = nome
            print("cadastrado com sucesso")
            
    def ValidaNome(self,nome):
        if len(nome) == 0:
            print("nome não pode estar vazio")
            return False
        else:
            return True

    def InserirIdade(self, idade):
        idadeCorreta = self.ValidaIdade (idade)
        if idadeCorreta == True:
            self.idade = idade
            print("idade precisa ser maio que 18")

    def ValidaIdade(self, idade):
        if idade > 18:
            print("Valor cadastrado com suceso")
            return False
        else:
            return True 
    
    def InserirSaldo(self, saldo):
        saldoCorreto = self.ValidaSaldo (saldo)
        if saldoCorreto == True:
            self.saldo = saldo
            print("Valor cadastrado não pode ser negativo")

    def ValidaSaldo (self, saldo):
        if saldo >0:
            print("Saldo positivo")
            return False
        else:
            return True 
        
    


cad = Cadastro ()
cad.InserirIdade(17)
cad.InserirSaldo(200)
cad.InserirNome("Heloísa")
