class Personnage:

    def __init__(self, name, genre, role, nbr_de_vie_ini):
        """Initialise les persos."""
        self.name = name
        self.genre = genre
        self.role = role
        self.nbr_de_vie = nbr_de_vie_ini
        self.alive = True
        self.inventaire = []
    
    def get_name(self):
        return self.name
    
    def get_article_ind(self):
        if self.genre == "femme":
           return "une"
        elif self.genre == "homme":
           return "un"
        else :
            return "um"

    def get_article(self, article):
        if self.genre == "femme":
           return"la"
        elif self.genre == "homme":
           return "le"
        else :
            return "lo"
    
    def get_role(self):
        if self.genre == "femme" and self.role == "Guerrier":
           return "guerrière"
        elif self.genre == "homme" and self.role == "Guerrier":
           return "guerrier"
        elif self.genre == "autre" and self.role == "Guerrier":
            return "guerri.ère.er"
            
        if self.genre == "femme" and self.role == "Sorcier":
            return "sorcière"
        elif self.genre == "homme" and self.role == "Sorcier":
            return "sorcier"
        elif self.genre == "autre" and self.role == "Sorcier":
            return "sorci.ère.er"
        
        if self.genre == "femme" and self.role == "Guérisseur":
           return "guérisseuse"
        elif self.genre == "homme" and self.role == "Guérisseur":
           return "guérisseur"
        elif self.genre == "autre" and self.role == "Guérisseur":
            return "guérisseu.se.r"

        if self.role == "Efle":
           return "elfe"

        if self.role == "Sage":
            return "sage"

        if self.genre == "femme" and self.role == "Nain":
           return "naine"
        elif self.genre == "homme" and self.role == "Nain":
           return "nain"
        else :
           return "nain.e"

    def add_objet(self, objet):
        self.inventaire.append(objet)

    def set_intelligence(self):
        if self.role == "Nain":
            self.intelligence = 20
        elif self.role == "Guérisseur":
            self.intelligence = 50
        elif self.role == "Elfe":
            self.intelligence = 50
        elif self.role == "Sorcier":
            self.intelligence = 60
        elif self.role == "Sage":
            self.intelligence = 85
        else:
            self.intelligence = 45
    
    def check_intelligence(self):
        self.set_intelligence()
        if self.intelligence < 0:
            self.intelligence = 0
        elif self.intelligence > 100:
            self.intelligence = 100
        if self.intelligence >= 0 and self.intelligence <= 25:
            self.etat = "stupide"
        elif self.intelligence > 25 and self.intelligence <= 45:
            self.etat = "limitée"
        elif self.intelligence > 45 and self.intelligence <= 60:
            self.etat = "normale"
        elif self.intelligence > 60 and self.intelligence <= 75:
            self.etat = "légèrement supérieure"
        elif self.intelligence > 75 and self.intelligence <= 85:
            self.etat = "supérieure"
        elif self.intelligence > 85 and self.intelligence <= 100:
            self.etat = "incroyable"
        return self.etat

    def add_intelligence(self, valeur):
        self.intelligence += valeur
        self.check_intelligence()
    
    def remove_intelligence(self, valeur):
        self.intelligence -= valeur
        self.check_intelligence()

    def check_nbr_de_vie(self):
        if self.nbr_de_vie >= 0:
            self.alive = True
        else:
            self.alive = False

    def add_vie(self, gain):
        if self.nbr_de_vie < self.nbr_de_vie_ini:
            self.nbr_de_vie += gain
        if self.nbr_de_vie > self.nbr_de_vie_ini:
            self.nbr_de_vie = self.nbr_de_vie_ini

        self.check_nbr_de_vie()

    def remove_vie(self, loose):
        if (self.nbr_de_vie > self.nbr_de_vie_ini):
            self.nbr_de_vie -= loose
        if (self.nbr_de_vie < self.nbr_de_vie_ini):
            self.nbr_de_vie = self.nbr_de_vie_ini

        self.check_nbr_de_vie()

    def choix_trait(self, trait):
        if trait == "généreux" and not self.généreux and not self.égoïste:
            self.généreux = True
        elif trait == "égoïste"and not self.égoïste and not self.généreux:
            self.égoïste = True 
        elif trait == "courageux"and not self.courageux and not self.lâche:
            self.courageux = True
        elif trait == "lâche"and not self.lâche and not self.courageux:
            self.lâche = True
        elif trait == "loyal"and not self.loyal and not self.traître:
            self.loyal = True
        elif trait == "traître"and not self.traître and not self.loyal:
            self.traître = True
        elif trait == "téméraire"and not self.téméraire and not self.prudent:
            self.téméraire = True
        elif trait == "prudent"and not self.téméraire and not self.prudent:
            self.prudent = True
        elif trait == "froid" and not self.amical and not self.froid:
            self.froid = True 
        elif trait == "amical"and not self.amical and not self.froid:
            self.amical = True 
        elif trait not in ["généreux", "lâche", "courageux", "loyal", "traître", "téméraire", "prudent", "froid", "amical"]:
            print(f"Le trait de caractère '{trait}' n'est pas valide.")
        else:
            pass
        
class Guerrier(Personnage):
    def __init__(self, name, nbr_de_vie_ini):
        super().__init__(name, nbr_de_vie_ini)
        self.role = "Guerrier"  # Définit le rôle du personnage
        self.defense = 6  # Définit la défense du guerrier
        self.attack = 8  # Définit l'attaque du guerrier
        self.magic = False  # Indique si le guerrier a la capacité de lancer des sorts ou non
        self.courageux = True
        self.temeraire = True  
        self.amical = False
        self.set_intelligence(self)

class Elfe(Personnage):
    def __init__(self, name, role, nbr_de_vie_ini):
        super().__init__(name, role, nbr_de_vie_ini)
        self.role = "Elfe"
        self.defense = 8
        self.attack = 6
        self.magic = True
        self.loyal =True
        self.courageux = True
        self.romantique = True
        self.set_intelligence(self)

class Nain(Personnage):
    def __init__(self, name, nbr_de_vie_ini):
        super().__init__(name, nbr_de_vie_ini)
        self.role = "Nain"
        self.defense = 8
        self.attack = 7
        self.magic = False
        self.loyal = True
        self.courageux = True
        self.amical = True
        self.set_intelligence(self)

class Guérisseur(Personnage):
    def __init__(self, name, nbr_de_vie_ini):
        super().__init__(name, nbr_de_vie_ini)
        self.role = "Guérisseur"
        self.defense = 5
        self.attack = 5
        self.magic = True
        self.loyal = True
        self.courageux = False
        self.généreux = True
        self.set_intelligence(self)

class Sorcier(Personnage):
    def __init__(self, name, nbr_de_vie_ini):
        super().__init__(name, nbr_de_vie_ini)
        self.role = "Sorcier"
        self.defense = 5
        self.attack = 7
        self.magic = True
        self.loyal = False
        self.courageux = False
        self.téméraire = True
        self.set_intelligence(self)

class Sage(Personnage):
    def __init__(self, name, nbr_de_vie_ini):
        super().__init__(name, nbr_de_vie_ini)
        self.role = "Sage"
        self.defense = 5
        self.attack = 5
        self.magic = True
        self.loyal = True
        self.courageux = False
        self.généreux = True
        self.set_intelligence(self)
