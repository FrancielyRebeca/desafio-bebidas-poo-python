from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class BebidaQuente(ABC):
    def preparar(self):
       conteudo = self.fever_agua()
       conteudo += '\n' + self.misturar()
       conteudo += '\n' + self.servir()
       caixa = Panel(conteudo, expand=True, title=' [green]INICIANDO O PREPARO[/] ', width=70)    
       return caixa

    def fever_agua(self):
        conteudo = '1. Fervendo água a 100 graus Celsius.'
        return conteudo 

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):
    def misturar(self):
        conteudo = '2. Passando água pressurizada pelo pó de café moído.'
        return conteudo   

    def servir(self):
        conteudo = '3. Servindo em xícara pequena.'
        return conteudo 
    
class Cha(BebidaQuente):
    def misturar(self):
        conteudo = '2. Mergulhando o sachê de ervas na água.'
        return conteudo  

    def servir(self):
        conteudo = '3. Servindo na caneca de porcelana com limão.'
        return conteudo  

class Leite(BebidaQuente):
    def misturar(self):
        conteudo = '2. Passando vapor pressurizado pelo bico do leite.'
        return conteudo   

    def servir(self):
        conteudo = '3. Servindo na caneca grande, já com café.'
        return conteudo  


# DESAFIO 24
bebida1 = Cafe()
bebida2 = Cha()
bebida3 = Leite()

print(bebida1.preparar())
print(bebida2.preparar())
print(bebida3.preparar())
