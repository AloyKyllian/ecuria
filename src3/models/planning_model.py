


class planningModel():
    
    def __init__(self):
        self.planning = []
        self.name = ""
        
    def set_planning(self, planning):
        self.planning = planning
        
    def get_planning(self):
        return self.planning
    
    def ajout(self, cellule):
        for i in self.planning:
            if (cellule.heure, cellule.cheval) == (i[0], i[1]):
                return -2
        if cellule.heure == "heure" or cellule.cheval == "cheval" or cellule.eleve == "eleve":
            return -1
        elif len(self.cheval) != 0 and self.cheval[cellule.cheval][1] >= 4:
            return -3
        elif cellule.getCellule() in self.planning:
            return -5
        else:
            self.planning.append(cellule.getCellule())
            self.planning.sort()
            if cellule.cheval in self.cheval:
                self.cheval[cellule.cheval][1] += 1
            else:
                return -4
            
    def supprime(self, cellule):
        if cellule.getCellule() in self.planning:
            self.planning.remove(cellule.getCellule())
            if cellule.cheval in self.cheval:
                self.cheval[cellule.cheval][1] -= 1
            else:
                return -4
        else:
            return -1
        
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        