from Model.Funcionario import Funcionario
from Model.Cargo import Cargo
from Model.Dependente import Dependente
from Model.Ocorrencia import Ocorrencia
from datetime import datetime

if __name__ == "__main__":

    # Criando Funcionario

    funcionario1 = Funcionario()
    funcionario1.setNome("Jean")

    # Criando Cargo

    cargo1 = Cargo()
    cargo1.setSalarioBruto(2000)

    # Criando Dependente

    dependente1 = Dependente()
    dependente1.setNome("Lucas")
    dependente1.setDataNascimento("25/4/2020")

    # Criando Ocorrencia

    ocorrencia1 = Ocorrencia()
    ocorrencia1.setDataOcorencia("25/10/23")
    ocorrencia1.setValorAcrescimo(1000)
    ocorrencia1.setDataOcorencia(500)
    ocorrencia1.addHistoricoOcorrencia("Aumento né pai")

    # Criando amarrações entre Funcionario/Cargo

    funcionario1.addCargo(cargo1)

    cargo1.addFuncionario(funcionario1)

    # Criando amarração entre Funcionario/Dependente

    funcionario1.addDependente(dependente1)

    dependente1.addFuncionario(funcionario1)

    # Criando amarração entre Funcionario/Ocorrencia

    funcionario1.addOcorencia(ocorrencia1)

    ocorrencia1.addFuncionario(funcionario1)