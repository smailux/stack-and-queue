from queue import File

def play(n):
    file = File()
    for i in range(1, n+1):
        file.enfiler(i)
    while file.longueur() > 1:
        k = file.defiler()
        file.enfiler(file.defiler())
        
    return file.tete()
