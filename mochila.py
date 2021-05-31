#Arquivo da CLASSE mochila => Inventário da personagem principal.

# INICIAR O DICIONÁRIO NA MAIN << URGENTE!

class Mochila:
    def __init__(self):
        self.mochila = []

    
    def abrir(self):
        if len(self.mochila) == 0:
            print('{Ela enfia a mão no fundo da mochila mas não encontra nada. A mochila está vazia.')
        else:
            print("Ela tem os seguintes itens na mochila:")
            for _item in self.mochila:
                print(_item, end="   ")
                print()
    
    
    def adicionar(self, item):
        self.mochila.append(item)
        print(f'Ela adicionou {item} na mochila.')

    
    def retirar(self, item):
        self.mochila.remove(item)
