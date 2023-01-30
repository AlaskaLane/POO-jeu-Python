from random import randint

class Magie:
    def __init__(self, nom, puissance, role):
        self.nom = nom
        self.puissance = puissance
        self.role = role

    def soigner(self, personnage, puissance):
        taux_de_reussite = TauxDeReussite(self.personnage).calculer()
        chance = randint(1, 100)
        if chance <= taux_de_reussite:
            personnage.add_vie(puissance)# L'action a réussi, vous pouvez mettre en place le comportement correspondant ici
            pass
        else:
            # L'action a échoué, vous pouvez mettre en place le comportement correspondant ici
            pass



class TauxDeReussite:
    def __init__(self, personnage, acte):
        self.personnage = personnage
        self.acte = acte

    def calculer(self, acte):
        taux =50
        
        # Ajuste le taux de réussite en fonction de l'état de l'intelligence du personnage
        if self.etat == "Stupide":
            success_rate -= 25
        elif self.etat == "Limitée":
            success_rate -= 10
        elif self.etat == "Supérieure":
            success_rate += 10
        elif self.etat == "Génie":
            success_rate += 25
        
        # Ajuste le taux de réussite en fonction de l'acte effectué
        if acte == "guérir":
            if not self.généreux:
                success_rate -= 10
        elif acte == "lancer un sort":
            success_rate += 10
        
        return success_rate