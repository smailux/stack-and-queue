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
