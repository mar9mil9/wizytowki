""" Moduł 7
    Zadanie: wizytówki


"""

from faker import Faker
faker = Faker()


class Wizytowka:
    def __init__(self, imie, nazwisko, adres_email, nr_tel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres_email = adres_email
        self.nr_tel = nr_tel

    def kontakt(self):
        return f"Wybieram numer {self.imie} {self.nazwisko}"

    def dlugosc_nazwy(self):
        suma_ilości_liter = len(self.imie) + len(self.nazwisko)
        return f"Imię i nazwisko ma długość {suma_ilości_liter}"

    def __str__(self):
        return f'{self.imie}, {self.nazwisko}, {self.adres_email}'


class WizytowkaBiznesowa(Wizytowka):
    def __init__(self, nazwa_firmy, stanowisko, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nazwa_firmy = nazwa_firmy
        self.stanowisko = stanowisko

    def __str__(self):
        return f'{self.imie}, {self.nazwisko}, {self.nazwa_firmy} ,{self.adres_email}'


def create_contacts(jakie_wizytowki, ile_wizytowek):
    wizytownik = []
    if jakie_wizytowki == 'biznesowe':
        for nr in range(1, ile_wizytowek + 1):
            wizytowka_nr = WizytowkaBiznesowa(imie=faker.first_name(), nazwisko=faker.last_name(), nazwa_firmy=faker.company, stanowisko=faker.ocupation, adres_email=faker.company_email(), nr_tel=faker.phone_number())
            wizytownik.append(wizytowka_nr)
    elif jakie_wizytowki == 'prywatne':
        for nr in range(1, ile_wizytowek + 1):
            wizytowka_nr = Wizytowka(imie=faker.first_name(), nazwisko=faker.last_name(), adres_email=faker.email(), nr_tel=faker.phone_number())
            wizytownik.append(wizytowka_nr)
    else:
        pass

    print(str(wizytownik)) # nie drukuje prawidłowo




print()
