from enum import Enum


class Type(Enum):
    fiction = "fiction"
    documentaire = "documentaire"


class Categorie:
    nom: str
    type: Type

    def __init__(self, nom, type: Type):
        self.nom = nom
        self.type = type

    def __str__(self):  # transforme un objet en string
        return f"{self.type.value} - {self.nom}"  # .value en ref à l'enum
