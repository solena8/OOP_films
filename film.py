class Film:

    def __init__(self, titre, date_sortie, realisatrice, categorie):
        self.titre = titre
        self.date_sortie = date_sortie
        self.realisatrice = realisatrice
        self.categorie = categorie

    def afficher_film(self):
        return (f"Le film : {self.titre}, de la catégorie : {self.categorie}, sorti en {self.date_sortie}, "
                f"a été réalisé par {self.realisatrice.prenom} {self.realisatrice.nom}, qui a {self.realisatrice.age} ans.")
