'''
OPEN CLOSED PRINCIPLE

Imagine que uma clínica veterinária tem seu sistema próprio para aprovação de exames. No primeiro momento, ela tem um método para
verificar exame de sangue. Em outro ela adiciona exame por raio-x. Notamos no código que, conforme a clínica adiciona exames,
deverão adicionar uma validação para o exame. O que aumentaria a complexidade do código e a manutenção do mesmo.

A solução deste caso pode ser feita com o princípio aberto-fechado (Open Closed Principle). 
Utilizando do conceito do OCP, crie uma interface e classes que implementam a mesma para que, caso a clínica necessite de um novo
tipo de exame, uma nova classe seja adicionada, implementando métodos de uma interface padrão para exames.

'''    
from verify_exam_interface import ExamInterface

class Exame:
    def __init__(self, tipo):
        self.tipo = tipo

class BloodTest(ExamInterface):
    def __init__(self, exame: Exame) -> None:
        self.exame = exame

    def aprovar_solicitacao_exame(self) -> None:

        if self.exame.tipo == "sangue":
            if b.verifica_condicoes_do_exame(self.exame):
                print("Exame sanguíneo aprovado!")
        else:
            print("Exame sanguíneo reprovado!")

    def verifica_condicoes_do_exame(self, exame: str) -> bool:
        tipo = exame.tipo
        if tipo == "sangue":
            return True
        
class XrayExamination(ExamInterface):
    def __init__(self, exame: Exame) -> None:
        self.exame = exame

    def aprovar_solicitacao_exame(self) -> None:
        if self.exame.tipo == "raio-x":
            if x.verifica_condicoes_do_exame(self.exame):
                print("Raio-X aprovado!")
        else:
            print("Raio-X reprovado!")

    def verifica_condicoes_do_exame(self, exame: str) -> bool:
        tipo = exame.tipo
        if tipo == "raio-x":
            return True

class Exame:
    def __init__(self, tipo):
        self.tipo = tipo

exame_sangue = Exame("sangue")
exame_raio_x = Exame("raio-x")

b = BloodTest(exame_sangue)
b.aprovar_solicitacao_exame()
print()
x = XrayExamination(exame_raio_x)
x.aprovar_solicitacao_exame()

