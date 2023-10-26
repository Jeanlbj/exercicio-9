from Model.Funcionario import Funcionario
from Model.Cargo import Cargo
from Model.Dependente import Dependente
from Model.Ocorrencia import Ocorrencia

if __name__ == "__main__":

    # Criando Funcionario

    funcionario1 = Funcionario()
    funcionario1.setNome("Jean")

    funcionario2 = Funcionario()
    funcionario2.setNome("João Victor")

    funcionario3 = Funcionario()
    funcionario3.setNome("Murilo")

    # Criando Cargo

    cargo1 = Cargo()
    cargo1.setSalarioBruto(2000)

    cargo2 = Cargo()
    cargo2.setSalarioBruto(8000)

    cargo3 = Cargo()
    cargo3.setSalarioBruto(3500)

    # Criando Dependente

    dependente1 = Dependente()
    dependente1.setNome("Lucas")
    dependente1.setDataNascimento("25/04/2015")

    dependente2 = Dependente()
    dependente2.setNome("Vinicius")
    dependente2.setDataNascimento("13/09/2022")

    dependente3 = Dependente()
    dependente3.setNome("Gustavo")
    dependente3.setDataNascimento("21/07/1998")

    dependente4 = Dependente()
    dependente4.setNome("Giacopo")
    dependente4.setDataNascimento("12/9/1992")

    # Criando Ocorrencia

    ocorrencia1 = Ocorrencia()
    ocorrencia1.setDataOcorencia("25/10/2023")
    ocorrencia1.setValorAcrescimo(1000)
    ocorrencia1.setValorDesconto(500)
    ocorrencia1.addHistoricoOcorrencia("Promoção de cargo")

    ocorrencia2 = Ocorrencia()
    ocorrencia2.setDataOcorencia("13/4/2023")
    ocorrencia2.setValorAcrescimo(5000)
    ocorrencia2.setValorDesconto(2700)
    ocorrencia2.addHistoricoOcorrencia("Promoção de cargo")

    ocorrencia3 = Ocorrencia()
    ocorrencia3.setDataOcorencia("28/3/2023")
    ocorrencia3.setValorAcrescimo(500)
    ocorrencia3.setValorDesconto(50)
    ocorrencia3.addHistoricoOcorrencia("Promoção de cargo")

    # Criando amarrações entre Funcionario/Cargo

    funcionario1.addCargo(cargo1)
    funcionario2.addCargo(cargo2)
    funcionario3.addCargo(cargo3)

    cargo1.addFuncionario(funcionario1)
    cargo2.addFuncionario(funcionario2)
    cargo3.addFuncionario(funcionario3)

    # Criando amarração entre Funcionario/Dependente

    funcionario1.addDependente(dependente1)
    funcionario1.addDependente(dependente2)
    funcionario2.addDependente(dependente3)
    funcionario3.addDependente(dependente4)

    dependente1.addFuncionario(funcionario1)
    dependente2.addFuncionario(funcionario1)
    dependente3.addFuncionario(funcionario2)
    dependente4.addFuncionario(funcionario3)

    # Criando amarração entre Funcionario/Ocorrencia

    funcionario1.addOcorencia(ocorrencia1)
    funcionario2.addOcorencia(ocorrencia2)
    funcionario3.addOcorencia(ocorrencia3)

    ocorrencia1.addFuncionario(funcionario1)
    ocorrencia2.addFuncionario(funcionario2)
    ocorrencia3.addFuncionario(funcionario3)

    # Printando funcionários e dependentes

    funcionario1.toStr(10, 2023)
    funcionario2.toStr(4, 2023)
    funcionario3.toStr(3, 2023)

    print("Programa finalizado.")
