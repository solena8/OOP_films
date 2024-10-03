
class Client:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.liste_films = []


    def ajouter_film(self, film):
        self.liste_films.append(film)

    def afficher_liste(self, liste):
        ma_liste = [film.titre for film in liste]
        return f"Liste de films de {self.prenom} {self.nom} : {ma_liste}"

