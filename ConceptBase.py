# -*- coding: utf-8 -*-
## author : Rochez Justin

#héritage
class humain:
    
    def __init__(self,nom):
        self.nom = nom

class homme(humain):
    
    def __init__(self,nom):
        humain.__init__(self,nom)
        self.sexe = "Mâle"
        self.Poilu = True

class femme(humain):
    def __init__(self,nom):
        humain.__init__(self,nom)
        self.sexe = "Femele"
        self.jolie = True



if __name__ == "__main__":
    adam = homme("adam")
    eve = femme("eve")

    print(isinstance(adam,humain))
    print(isinstance(eve,humain))
    print("======================")
    print(isinstance(adam,femme))
    print(isinstance(eve,homme))