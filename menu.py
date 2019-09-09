import sys

from bloco_notas import BlocoDeNotas, Nota

class Menu:

    def __init__(self):
        self.bloco_notas = BlocoDeNotas()
        self.escolhas = {"1": self.mostrar_notas,
                        "2": self.buscar_notas,
                        "3": self.adicionar_nota,
                        "4": self.modificar_nota,
                        "5": self.sair}

    def mostrar_menu(self):
        print("""Menu

                1. Mostrar notas
                2. Buscar notas
                3. Adicionar nota
                4. Modificar nota
                5. Sair
            """)

    def rodar(self):
        '''Mostra o menu e responde as escolhas'''
        while True:
            self.mostrar_menu()
            escolha = input('Escolha uma opcao: ')
            executar = self.escolhas.get(str(escolha))
            if executar:
                executar()
            else:
                print("{0} invalido".format(escolha))

    def mostrar_notas(self, notas=None):
        if not notas:
            for i in self.bloco_notas.notas:
                print("{0}: {1}\n{2}".format(i.id, i.texto, i.tags))
        else:
            for i in notas:
                print("{0}: {1}\n{2}".format(i.id, i.texto, i.tags))

    def buscar_notas(self):
        filtro = input("Buscar por: ")
        n = self.bloco_notas.buscar(filtro)
        self.mostrar_notas(n)

    def adicionar_nota(self):
        texto = input("Digite o texto: ")
        tags = input("Digite as tags: ")
        self.bloco_notas.nova_nota(texto, tags)
        print("nota adicionada")

    def modificar_nota(self):
        idn = input("ID de uma nota: ")
        texto = input("Novo texto: ")
        tags = input("Novas tags: ")
        self.bloco_notas.modificar_texto(idn, texto)
        self.bloco_notas.modificar_tags(idn, tags)
        print("Nota modificada com sucesso.")

    def sair(self):
        print("Saindo...")
        sys.exit(0)

if __name__ == "__main__":
    Menu().rodar()
