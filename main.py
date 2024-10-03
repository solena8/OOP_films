from film import Film
from realisatrice import Realisatrice
from categorie import Categorie
from categorie import Type
from client import Client

categorie_drame = Categorie("drame", Type.fiction)
categorie_drame2 = Categorie("comédie", Type.fiction)
realisatrice = Realisatrice("Triet", "Justine", 1978, birthday_month=7, birthday_day=17)
realisatrice2 = Realisatrice("Gerwig", "Greta", 1983, birthday_month=8, birthday_day=4)
film = Film("Anatomie d'une chute", 2023, realisatrice, categorie_drame)
film2 = Film("Barbie", 2023, realisatrice2, categorie_drame2)

print(film.afficher_film())

print(film2.afficher_film())


client = Client("Soléna", "Toussaint")
client.ajouter_film(film)
client.ajouter_film(film2)

print(client.afficher_liste(client.liste_films))


