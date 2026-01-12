class Pile:
    def __init__(self):
        self.pile = []
    def estVide(self):
        return self.pile == []
    def push(self, valeur):
        return self.pile.append(valeur)
    def pop(self):
        assert not self.estVide()
        k = self.pile[-1]
        self.pile = self.pile[0:-1]
        return k
    def sommet(self):
        assert not self.estVide()
        k = self.pop()
        self.push(k)
        return k
    def hauteur(self):
        p_bis = Pile()
        cpt = 0
        while not self.estVide():
            p_bis.push(self.pop())
            cpt += 1
        while not p_bis.estVide():
            self.push(p_bis.pop())
        return cpt


def calculerNPI(calcul):
    pile = Pile()
    for element in calcul.split(" "):
        if pile.hauteur() >= 2 and element in ['+', '/', '*', '-'] :
            a,b = float(pile.pop()), float(pile.pop())
            if element == '+':
                pile.push(b + a)
            elif element == '*':
                pile.push(b*a)
            elif element == '-':
                pile.push(b-a)
            else :
                pile.push(b/a)
        else :
            pile.push(element)
    return pile.sommet()

def verifierParenthesage(programme):
    pile = Pile()
    dico = {'(' : ')', '[' : ']', '{' : '}'}
    for element in programme :
        if element in ('(', '[', '{'):
            pile.push(element)
        elif not pile.estVide() and element == dico[pile.sommet()]:
            pile.pop()
    return pile.estVide()


class File:
    def __init__(self):
        self.file = []
    def estVide(self):
        return self.file == []
    def enfiler(self, valeur):
        self.file = [valeur] + self.file
    def defiler(self):
        assert not self.estVide()
        k = self.file[-1]
        self.file = self.file[0:-1]
        return k
    def tete(self):
        assert not self.estVide()
        k = self.defiler()
        f_bis = File()
        f_bis.enfiler(k)
        while not self.estVide():
            f_bis.enfiler(self.defiler())
        while not f_bis.estVide():
            self.enfiler(f_bis.defiler())
        return k
    def longueur(self):
        f_bis = File()
        cpt = 0
        while not self.estVide():
            f_bis.enfiler(self.defiler())
            cpt += 1
        while not f_bis.estVide() :
            self.enfiler(f_bis.defiler())
        return cpt
    
    
def jouer(n):
    file = File()
    for i in range(1, n+1):
        file.enfiler(i)
    while file.longueur() > 1:
        k = file.defiler()
        file.enfiler(file.defiler())
        
    return file.tete()

