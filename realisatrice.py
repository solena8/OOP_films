from dateutil.relativedelta import relativedelta
from datetime import date


class Realisatrice:
    def __init__(self, nom, prenom, birthday_year, birthday_month, birthday_day):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date(birthday_year, birthday_month, birthday_day)
        self.age = relativedelta(date.today(), self.date_naissance).years
