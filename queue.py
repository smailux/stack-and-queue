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
