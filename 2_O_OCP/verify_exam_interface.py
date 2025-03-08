from abc import ABC, abstractmethod

class ExamInterface(ABC):
  @abstractmethod
  def aprovar_solicitacao_exame(self) -> None:
    pass

  @abstractmethod
  def verifica_condicoes_do_exame(self, exame: str) -> bool:
    pass
