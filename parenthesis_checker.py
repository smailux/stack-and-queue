from stack import Pile

def verifierParenthesage(programme):
    pile = Pile()
    dico = {'(' : ')', '[' : ']', '{' : '}'}
    for element in programme :
        if element in ('(', '[', '{'):
            pile.push(element)
        elif not pile.estVide() and element == dico[pile.sommet()]:
            pile.pop()
    return pile.estVide()
