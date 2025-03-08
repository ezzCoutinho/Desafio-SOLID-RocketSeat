'''
SINGLE RESPONSABILITY PRINCIPLE

Note que nessa classe, temos várias ações e responsabilidades. O que torna a manutenção, usabilidade e até a performance ruins.

Seguindo o conceito do Princípio da Responsabilidade única, organize essa classe e, se necessário, crie outras 
classes com suas devidas responsabilidades.

'''

class TaskHandler:
    def create_task(self) -> None:
        print("Tarefa criada com sucesso!")

    def update_task(self) -> None:
        print("Tarefa atualizada com sucesso!")

    def remove_task(self) -> None:
        print("Tarefa removida com sucesso!")

class ConnectionAPI:
    def conect_api(self) -> None:
        print("API conectada com sucesso!")

class Notification:
    def send_notification(self) -> None:
        print("Notificação enviada com sucesso!")

class Report:
    def generate_report(self) -> None:
        print("Gerando relatório...")

    def send_report(self) -> None:
        print("Relatório enviado com sucesso!")

t = TaskHandler()
t.create_task()
t.update_task()
t.remove_task()
print()
c = ConnectionAPI()
c.conect_api()
print()
r = Report()
r.generate_report()
r.send_report()
