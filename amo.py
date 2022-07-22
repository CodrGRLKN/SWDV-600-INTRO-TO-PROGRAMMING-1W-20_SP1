
class Weapon:
    def _str_(self):
        return self.name


class Sword(Weapon):
    def _init_(self):
        self.name = "Sword"
        self.defeat = 100
        
    

class MagicLasso(Weapon):
    def _init_(self):
        self.name = "Magic Lasso"
        self.defeat = 60

class Bat(Weapon):
    def _init_(self):
        self.name = "Bat"
        self.defeat = 20
        