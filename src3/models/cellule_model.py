from .heure_model import HeureModel

class Cheval():
    def __init__(self):
        self.name = ""
        self.poids = 0
        self.posexcel = 0
        self.poslistbox = 0
        
    def set_cheval(self, cheval):
        self.name = cheval.name
        self.poids = cheval.poids
        self.posexcel = cheval.posexcel
        self.poslistbox = cheval.poslistbox
    
    def get_cheval(self):
        return self
    
    def get_name(self):
        return self.name
    
    def get_poids(self):
        return self.poids
    
    def get_posexcel(self):
        return self.posexcel
    
    def get_poslistbox(self):
        return self.poslistbox
    
    def set_name(self, name):
        self.name = name
        
    def set_poids(self, poids):
        self.poids = poids
        
    def set_posexcel(self, posexcel):
        self.posexcel = posexcel

    def set_poslistbox(self, poslistbox):
        self.poslistbox = poslistbox
        
    

class Cavalier():
    def __init__(self):
        self.name = ""
        self.poids = 0
        self.grade = 0
    
    def set_cavalier(self, cavalier):
        self.name = cavalier.name
        self.poids = cavalier.poids
        self.grade = cavalier.grade
    
    def get_cavalier(self):
        return self

    def get_name(self):
        return self.name
    
    def get_poids(self):
        return self.poids
    
    def get_grade(self):
        return self.grade
    
    def set_name(self, name):
        self.name = name
        
    def set_poids(self, poids):
        self.poids = poids
        
    def set_grade(self, grade):
        self.grade = grade
    
    

class CelluleModel():
    
    def __init__(self):
        self.heure = HeureModel()
        self.cheval = Cheval()
        self.cavalier = Cavalier()
    
    def get_cellule(self):
        return (self.heure.get_heure(), self.cheval.get_name(), self.cavalier.get_name())
    
    def set_cellule(self, heure, cheval, cavalier):
        self.heure = heure
        self.cheval = cheval
        self.cavalier = cavalier
    
    def set_heure(self, heure):
        self.heure = heure
    
    def set_cheval(self, cheval):
        self.cheval = cheval
    
    def set_cavalier(self, cavalier):
        self.cavalier = cavalier
    
    def get_heure(self):
        return self.heure
    
    def get_cheval(self):
        return self.cheval
    
    def get_cavalier(self):
        return self.cavalier
    


