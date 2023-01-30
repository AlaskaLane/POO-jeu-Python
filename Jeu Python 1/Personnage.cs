using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Personnage : MonoBehaviour
{
    // Propriétés
    public string name { get; set; }
    public string genre { get; set; }
    public int nbr_de_vie { get; set; }
    public bool alive { get; set; }
    public List<string> inventaire { get; set; }
    public string etat { get; set; }

    // Constructeur
    public Personnage(string name, string genre, string role, int nbr_de_vie_ini)
    {
        this.name = name;
        this.genre = genre;
        this.role = role;
        this.nbr_de_vie = nbr_de_vie_ini;
        this.alive = true;
        this.inventaire = new List<string>();
        this.etat = "";
    }

    // Méthodes
    public string get_article_ind()
    {
        if (this.genre == "femme")
        {
            return "une";
        }
        else if (this.genre == "homme")
        {
           return "un";
        }
        else
        {
            return "um";
        }
    }

    public string get_article()
    {
        if (this.genre == "femme")
        {
            return "la";
        }
        else if (this.genre == "homme")
        {
           return "le";
        }
        else
        {
            return "lo";
        }
    }
    public string get_role()
{
    if (this.genre == "femme" && this.role == "Guerrier")
    {
        return "guerrière";
    }
    else if (this.genre == "homme" && this.role == "Guerrier")
    {
        return "guerrier";
    }
    else if (this.genre == "autre" && this.role == "Guerrier")
    {
        return "guerri.ère.er";
    }
    else if (this.genre == "femme" && this.role == "Sorcier")
    {
        return "sorcière";
    }
    else if (this.genre == "homme" && this.role == "Sorcier")
    {
        return "sorcier";
    }
    else if (this.genre == "autre" && this.role == "Sorcier")
    {
        return "sorci.ère.er";
    }
    else if (this.genre == "femme" && this.role == "Guérisseur")
    {
        return "guérisseuse";
    }
    else if (this.genre == "homme" && this.role == "Guérisseur")
    {
        return "guérisseur";
    }
    else if (this.genre == "autre" && this.role == "Guérisseur")
    {
        return "guérisseu.se.r";
    }
    else if (this.role == "Elfe")
    {
        return "elfe";
    }
    else if (this.role == "Sage")
    {
        return "sage";
    }
}

public void add_objet(string objet)
{
    this.inventaire.Add(objet);
}

public void remove_objet(string objet)
{
    this.inventaire.Remove(objet);
}

public void set_intelligence()
{
    if (this.role == "Nain")
    {
        this.intelligence = 20;
    }
    else if (this.role == "Guérisseur")
    {
        this.intelligence = 50;
    }
    else if (this.role == "Elfe")
    {
        this.intelligence = 50;
    }
    else if (this.role == "Sorcier")
    {
        this.intelligence = 60;
    }
    else if (this.role == "Sage")
    {
        this.intelligence = 80;
    }
    else
    {
        this.intelligence = 45;
    }
}

public void check_intelligence()
{
    this.set_intelligence();
    if (this.intelligence < 0)
    {
        this.intelligence = 0;
    }
    else if (this.intelligence > 100)
    {
        this.intelligence = 100;
    }
    if (this.intelligence >= 0 && this.intelligence <= 25)
    {
        this.etat = "stupide";
    }
    else if (this.intelligence > 25 && this.intelligence <= 45)
    {
        this.etat = "limitée";
    }
    else if (this.intelligence > 45 && this.intelligence <= 60)
    {
        this.etat = "normale";
    }
    else if (this.intelligence > 60 && this.intelligence <= 75)
    {
        this.etat = "légèrement supérieure";
    }
    else if (this.intelligence > 75 && this.intelligence <= 85)
    {
        this.etat = "supérieure";
    }
    else if (this.intelligence > 85 && this.intelligence <= 100)
    {
        this.etat = "incroyable";
    }
}

public string get_intelligence()
{
    return this.etat;
}

public int get_intelligence_pnt()
{
    return this.intelligence;
}

public void add_intelligence(int valeur)
{
    this.intelligence += valeur;
    this.check_intelligence();
}

public void remove_intelligence(int valeur)
{
    this.intelligence -= valeur;
    this.check_intelligence();
}

public void check_nbr_de_vie()
{
    if (this.nbr_de_vie <= 0)
        {
            this.alive = false;
        }
}
public void add_vie(gain)
{
    if (this.nbr_de_vie < this.nbr_de_vie_ini)
    {
        this.nbr_de_vie += gain;
    }
    if (this.nbr_de_vie >= this.nbr_de_vie_ini)
    {
        this.nbr_de_vie = this.nbr_de_vie_ini;
    }
    this.check_nbr_de_vie();
}public void remove_vie(int loose)
{
    if (this.nbr_de_vie > this.nbr_de_vie_ini)
    {
        this.nbr_de_vie -= loose;
    }
    if (this.nbr_de_vie < this.nbr_de_vie_ini)
    {
        this.nbr_de_vie = this.nbr_de_vie_ini;
    }

    this.check_nbr_de_vie();
}

public void choix_trait(string trait)
{
    if (trait == "généreux" && !this.généreux && !this.égoïste)
    {
        this.généreux = true;
    }
    else if (trait == "égoïste" && !this.égoïste && !this.généreux)
    {
        this.égoïste = true;
    }
    else if (trait == "courageux" && !this.courageux && !this.lâche)
    {
        this.courageux = true;
    }
    else if (trait == "lâche" && !this.lâche && !this.courageux)
    {
        this.lâche = true;
    }
    else if (trait == "loyal" && !this.loyal && !this.traître)
    {
        this.loyal = true;
    }
    else if (trait == "traître" && !this.traître && !this.loyal)
    {
        this.traître = true;
    }
    else if (trait == "téméraire" && !this.téméraire && !this.prudent)
    {
        this.téméraire = true;
    }
    else if (trait == "prudent" && !this.téméraire && !this.prudent)
    {
        this.prudent = true;
    }
    else if (trait == "froid" && !this.amical && !this.froid)
    {
        this.froid = true;
    }
    else if (trait == "amical" && !this.amical && !this.froid)
    {
        this.amical = true;
    }
    else if (!new List<string> { "généreux", "lâche", "courageux", "loyal", "traître", "téméraire", "prudent", "froid", "amical" }.Contains(trait))
    {
        Console.WriteLine($"Le trait de caractère '{trait}' n'est pas valide.");
    }
    else
    {
    // ne rien faire
    }

class Guerrier : Personnage
{
    public Guerrier(string name, int nbr_de_vie_ini) : base(name, nbr_de_vie_ini)
    {
        // Création d'une instance de la sous-classe Guerrier:
        //Guerrier monGuerrier = new Guerrier("Robert", 100);
        this.role = "Guerrier";
        this.defense = 6;
        this.attack = 8;
        this.magic = false;
        this.courageux = true;
        this.temeraire = true;
        this.amical = false;
        this.set_intelligence(this);
    }
}

class Elfe : Personnage
{
    public Elfe(string name, int nbr_de_vie_ini) : base(name, nbr_de_vie_ini)
    {
        this.role = "Elfe";
        this.defense = 8;
        this.attack = 6;
        this.magic = true;
        this.loyal = true;
        this.courageux = true;
        this.romantique = true;
        this.set_intelligence(this);
    }
}
class Nain : Personnage
{
    public Nain(string name, int nbr_de_vie_ini) : base(name, nbr_de_vie_ini)
    {
        this.role = "Nain";
        this.defense = 8;
        this.attack = 7;
        this.magic = false;
        this.loyal = true;
        this.courageux = true;
        this.amical = true;
        this.set_intelligence();
    }
}
class Guérisseur : Personnage
{
    public Guérisseur(string name, int nbr_de_vie_ini) : base(name, nbr_de_vie_ini)
    {
        this.role = "Guérisseur";
        this.defense = 5;
        this.attack = 5;
        this.magic = true;
        this.loyal = true;
        this.courageux = false;
        this.généreux = true;
        this.set_intelligence();
    }
}
class Sorcier : Personnage
{
    public Sorcier(string name, int nbr_de_vie_ini) : base(name, nbr_de_vie_ini)
    {
        this.role = "Sorcier";
        this.defense = 5;
        this.attack = 7;
        this.magic = true;
        this.loyal = false;
        this.courageux = false;
        this.téméraire = true;
        this.set_intelligence();
    }
}
class Sage : Personnage
{
    public Sage(string name, int nbr_de_vie_ini) : base(name, nbr_de_vie_ini)
    {
        this.role = "Sage";
        this.defense = 5;
        this.attack = 5;
        this.magic = true;
        this.loyal = true;
        this.courageux = false;
        this.généreux = true;
        this.set_intelligence();
    }
}
