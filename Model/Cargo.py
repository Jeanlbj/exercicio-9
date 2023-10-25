class Cargo:

    def __init__(self):
        self.__salarioBruto = 0
        self.__funcionario = []

    def setSalarioBruto(self, salarioBruto):
        self.__salarioBruto = salarioBruto

    def getSalarioBruto(self):
        return self.__salarioBruto

    def addFuncionario(self, funcionario):
        self.__funcionario.append(funcionario)

    def removerFuncionario(self, funcionario):
        self.__funcionario.remove(funcionario)

    def listarFuncionario(self):
        return self.__funcionario
