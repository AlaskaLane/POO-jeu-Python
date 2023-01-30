import Personnages
import Actions 

Poppy = Personnages.Personnage("Poppy", "homme", "Sorcier", 10)
print(Poppy.get_article_ind().capitalize(), Poppy.get_role(),"nommé", Poppy.get_name(), "est d'intelligence", Poppy.get_intelligence(), "et il a", Poppy.check_nbr_de_vie(), "vie(s)" )
Poppy.remove_vie(3)
print("\n Il a maintenant", Poppy.nbr_de_vie())
