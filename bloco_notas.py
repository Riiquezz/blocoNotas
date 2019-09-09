
import datetime

ultimo_id = 0

class Nota:
    '''Representa uma nota em um bloco de notas'''

    def __init__(self, texto, tags=''):
        '''Inicializa uma nota com texto e tags.
        Seta um ID unico automaticamente'''
        self.texto = texto
        self.tags = tags
        self.data_criacao = datetime.date.today()
        self.id = nextId()

    def igual(self, filtro):
        '''Determina se esta nota contem o texto filtrado'''
        return filtro in self.texto or filtro in self.tags

def nextId():
    global ultimo_id
    ultimo_id += 1
    return ultimo_id

class BlocoDeNotas:

    def __init__(self):
        '''Inicializa um bloco de notas com uma lista vazia'''
        self.notas = []

    def nova_nota(self, texto, tags=''):
        '''Cria uma nova nota e adiciona na lista'''
        n = Nota(texto, tags)
        self.notas.append(n)

    def _encontrar_nota(self, id_nota):
        '''Localiza a nota por id'''
        for n in self.notas:
            if n.id == id_nota:
                return n
        return None

    def modificar_texto(self, id_nota, texto):
        '''Encontra uma nota e modifica o texto'''
        n = self._encontrar_nota(id_nota)
        n.texto = texto

    def modificar_tags(self, id_nota, tags):
        '''Encontra uma nota e modifica as tags'''
        n = self._encontrar_nota(id_nota)
        n.tags = tags

    def buscar(self, filtro):
        '''Encontrar todas as notas que batem com o filtro'''
        return [n for n in self.notas if n.igual(filtro)]
