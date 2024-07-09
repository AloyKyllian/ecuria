import sys
import os
import unittest

# Ajouter src3 au chemin des modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src3')))

# Importer les modules à tester
from models.cellule_model import Cheval, Cavalier, CelluleModel
from models.heure_model import HeureModel

class TestCheval(unittest.TestCase):

    def test_initial_values(self):
        cheval = Cheval()
        self.assertEqual(cheval.name, "")
        self.assertEqual(cheval.poids, 0)
        self.assertEqual(cheval.posexcel, 0)
        self.assertEqual(cheval.poslistbox, 0)

    def test_setters(self):
        cheval = Cheval()
        cheval.set_name("Spirit")
        cheval.set_poids(500)
        cheval.set_posexcel(10)
        cheval.set_poslistbox(5)
        
        self.assertEqual(cheval.name, "Spirit")
        self.assertEqual(cheval.poids, 500)
        self.assertEqual(cheval.posexcel, 10)
        self.assertEqual(cheval.poslistbox, 5)

    def test_getters(self):
        cheval = Cheval()
        cheval.set_name("Spirit")
        cheval.set_poids(500)
        cheval.set_posexcel(10)
        cheval.set_poslistbox(5)
        
        self.assertEqual(cheval.get_name(), "Spirit")
        self.assertEqual(cheval.get_poids(), 500)
        self.assertEqual(cheval.get_posexcel(), 10)
        self.assertEqual(cheval.get_poslistbox(), 5)
    
    def test_set_cheval(self):
        cheval1 = Cheval()
        cheval1.set_name("Spirit")
        cheval1.set_poids(500)
        cheval1.set_posexcel(10)
        cheval1.set_poslistbox(5)
        
        cheval2 = Cheval()
        cheval2.set_cheval(cheval1)
        
        self.assertEqual(cheval2.get_name(), "Spirit")
        self.assertEqual(cheval2.get_poids(), 500)
        self.assertEqual(cheval2.get_posexcel(), 10)
        self.assertEqual(cheval2.get_poslistbox(), 5)

class TestCavalier(unittest.TestCase):

    def test_initial_values(self):
        cavalier = Cavalier()
        self.assertEqual(cavalier.name, "")
        self.assertEqual(cavalier.poids, 0)
        self.assertEqual(cavalier.grade, 0)

    def test_setters(self):
        cavalier = Cavalier()
        cavalier.set_name("Arthur")
        cavalier.set_poids(75)
        cavalier.set_grade(3)
        
        self.assertEqual(cavalier.name, "Arthur")
        self.assertEqual(cavalier.poids, 75)
        self.assertEqual(cavalier.grade, 3)

    def test_getters(self):
        cavalier = Cavalier()
        cavalier.set_name("Arthur")
        cavalier.set_poids(75)
        cavalier.set_grade(3)
        
        self.assertEqual(cavalier.get_name(), "Arthur")
        self.assertEqual(cavalier.get_poids(), 75)
        self.assertEqual(cavalier.get_grade(), 3)
    
    def test_set_cavalier(self):
        cavalier1 = Cavalier()
        cavalier1.set_name("Arthur")
        cavalier1.set_poids(75)
        cavalier1.set_grade(3)
        
        cavalier2 = Cavalier()
        cavalier2.set_cavalier(cavalier1)
        
        self.assertEqual(cavalier2.get_name(), "Arthur")
        self.assertEqual(cavalier2.get_poids(), 75)
        self.assertEqual(cavalier2.get_grade(), 3)


class TestHeureModel(unittest.TestCase):

    def test_initial_values(self):
        heure_model = HeureModel()
        self.assertEqual(heure_model.get_heure(), "")

    def test_set_heure(self):
        heure_model = HeureModel()
        heure_model.set_heure("12:00")
        self.assertEqual(heure_model.get_heure(), "12:00")

    def test_get_heure(self):
        heure_model = HeureModel()
        heure_model.set_heure("12:00")
        self.assertEqual(heure_model.get_heure(), "12:00")

class TestCelluleModel(unittest.TestCase):

    def test_initial_values(self):
        cellule = CelluleModel()
        self.assertEqual(cellule.get_heure().get_heure(), "")
        self.assertEqual(cellule.get_cheval().get_name(), "")
        self.assertEqual(cellule.get_cavalier().get_name(), "")

    def test_setters(self):
        cellule = CelluleModel()
        heure = HeureModel()
        heure.set_heure("10:00")
        
        cheval = Cheval()
        cheval.set_name("Spirit")
        
        cavalier = Cavalier()
        cavalier.set_name("Arthur")
        
        cellule.set_heure(heure)
        cellule.set_cheval(cheval)
        cellule.set_cavalier(cavalier)
        
        self.assertEqual(cellule.get_heure().get_heure(), "10:00")
        self.assertEqual(cellule.get_cheval().get_name(), "Spirit")
        self.assertEqual(cellule.get_cavalier().get_name(), "Arthur")

    def test_get_cellule(self):
        cellule = CelluleModel()
        heure = HeureModel()
        heure.set_heure("10:00")
        
        cheval = Cheval()
        cheval.set_name("Spirit")
        
        cavalier = Cavalier()
        cavalier.set_name("Arthur")
        
        cellule.set_cellule(heure, cheval, cavalier)
        self.assertEqual(cellule.get_cellule(), ("10:00", "Spirit", "Arthur"))

if __name__ == '__main__':
    unittest.main()

