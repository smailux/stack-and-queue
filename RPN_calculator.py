from stack import Pile

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
