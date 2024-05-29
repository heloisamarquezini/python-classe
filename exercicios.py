class exercicio:
    def __init__(self):
        print('')

    def ex1(self):
        nomeFuncionario = "Ester"
        idade= 34
        salario = 2000.00
        cargo = "Gerente"
        turno = "Matutino"
        setor = "Administrativo"
        print("nomeFuncionario", nomeFuncionario, "idade", idade,"salario",salario, "cargo", cargo, "turno", turno, "setor", setor)

    def ex2(self):
        print("EX2")
        nomeEscola = "Colégio Estadual Cívico Militar Cruzeiro do Oeste"
        estado = "Paraná"
        numeroProfessores = 66
        cidade = "Cruzeiro do Oeste"
        numeroMilitares = 5
        logradouro = "Avenida Santos Dumont"
        numeroEndereco = 317
        numeroAlunos = 560
        colegioMilitar = True 
        disciplinas = ["Matemática", "Ciências", "História", "Geografia"]

        print("nomeEscola",nomeEscola,"estado",estado, "numeroProfessores", numeroProfessores, "cidade", cidade, "numeroMilitares", numeroMilitares, "logradouro", logradouro, "numeroEndereco", numeroEndereco, "numeroAlunos", numeroAlunos, "colegioMilitar", colegioMilitar, "discipinas", disciplinas)


    def ex3(self):
        print("EX3")
        valor1 = 10
        valor2 = 5
        valor3 = 2
        valor4 = 8
        valor5 = -5

        resultado1 = valor1 + valor2
        print("resultado1=", resultado1)

        resultado2 = valor1 + valor2 + valor4
        print("resultado2", resultado2)

        resultado3 = valor1 + valor2 - valor5
        print("resultado3", resultado3)

        resultado4 = valor1 + int(valor3)
        print("resultado4", resultado4)

        resultado5 = valor1 + valor2
        print("resultado5", resultado5)

        resultado6 = (valor4*valor2)/2
        print("resultado6", resultado6)

        resultado7 = (valor1+valor2+valor4+valor5)/4
        print("resultado7", resultado7)


ex = exercicio()
ex.ex1()
ex.ex2()
ex.ex3()
