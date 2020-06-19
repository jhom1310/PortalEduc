class Materia():
    nome = 'text'

class Xixi():
    def __init__(self, nome):
        self.nome = nome
        self.list = []

    def set_list(self, x):
        if(x == Materia):
            self.list.append(x)
        else:
            self.list.append('meu ovo')

tete = Materia

print(tete.nome)
kaka = Xixi('kkkkkkkkkkk')
kaka.set_list("salve")
print(kaka.nome)


print(kaka.list)
