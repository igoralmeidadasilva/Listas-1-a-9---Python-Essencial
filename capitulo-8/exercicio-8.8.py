class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome 
        self.idade = idade 
        
    def mostrar_dados(self, ) -> None:
        print(f"{self.nome} tem {self.idade} de idade. \n")
        
class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula) -> None:
        super().__init__(nome, idade)
        self.matricula = matricula
        
    def mostrar_dados(self, ) -> None:
        print(f"{self.nome} tem {self.idade} de idade e tem a matrícula {self.matricula}. \n")

if __name__ == "__main__":
    aluno = Aluno("Igor",26,"20201si027")
    aluno.mostrar_dados()
    
    
    
        