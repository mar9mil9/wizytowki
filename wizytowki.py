# ćwiczenie 1
'''
class Wizytowka:
    def __init__(self, imie, nazwisko, nazwa_firmy, stanowisko, adres_email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nazwa_firmy = nazwa_firmy
        self.stanowisko = stanowisko
        self.adres_email = adres_email

    def kontakt(self):
        return f"Kontaktuję się z {self.imie} {self.nazwisko}"

    # ________to nie działa__________VVV
    @property
    def dlugosc_imienia_i_nazwiska(self):
        return len(self.imie) + len(self.nazwisko) + 1

    @dlugosc_imienia_i_nazwiska.setter
    def imie_nazwisko(self, ktos):
        self.imie = ktos.split()[0]
        self.nazwisko = ktos.split()[1]

'''

from faker import Faker
faker = Faker()
'''
print(f'name: {faker.name()}')
print(f'address: {faker.address()}')
print(f'text: {faker.text()}')

print(f'Name: {faker.name()}')
print(f'First name: {faker.first_name()}')
print(f'Last name: {faker.last_name()}')
phone = faker.phone_number()
print(f'Company email: {faker.company_email()}')
'''


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

    print(str(wizytownik))


'''
wizytowka_nr1 = WizytowkaBiznesowa(imie="Ksenia", nazwisko="Adamczyk", nazwa_firmy="Destiny Realty", stanowisko="technik",
                          adres_email="KseniaAdamczyk@armyspy.com", nr_tel="+48 658 325 951")
wizytowka_nr2 = WizytowkaBiznesowa(imie="Eligia", nazwisko="Kucharska", nazwa_firmy="Tapicerstwo EK", stanowisko="tapicer",
                          adres_email="EligiaKucharska@rhyta.com", nr_tel="+48 357 954 824")
wizytowka_nr3 = WizytowkaBiznesowa(imie="Asia", nazwisko="Lasińska", nazwa_firmy="S&W Cafeteria", stanowisko="Web designer",
                          adres_email="AsiaJasinska@teleworm.us", nr_tel="+48 831 319 458")
wizytowka_nr4 = WizytowkaBiznesowa(imie="Kunegunda", nazwisko="Górska", nazwa_firmy="Keeney's", stanowisko="kontroler",
                          adres_email="KunegundaGorska@jourrapide.com", nr_tel="+48 215 995 466")
wizytowka_nr5 = WizytowkaBiznesowa(imie="Bazyli", nazwisko="Pawlak", nazwa_firmy="Anthony's", stanowisko="kierowca",
                          adres_email="BazyliPawlak@dayrep.com", nr_tel="+48 883 115 654")

wizytownik = [wizytowka_nr1, wizytowka_nr2, wizytowka_nr3, wizytowka_nr4, wizytowka_nr5]
'''
'''
for nr_wizytowki in wizytownik:
    print(f"imię: {nr_wizytowki.imie}, nazwisko: {nr_wizytowki.nazwisko}, firma: {nr_wizytowki.nazwa_firmy}, e-mail: {nr_wizytowki.adres_email}")

po_imieniu = sorted(wizytownik, key=lambda Wizytowka: Wizytowka.imie)
po_nazwisku = sorted(wizytownik, key=lambda Wizytowka: Wizytowka.nazwisko)
po_emailu = sorted(wizytownik, key=lambda Wizytowka: Wizytowka.adres_email)

print("____________________________________________________________________________________________________________________")
for nr_wizytowki in po_imieniu:
    print(f"imię: {nr_wizytowki.imie}, nazwisko: {nr_wizytowki.nazwisko}, firma: {nr_wizytowki.nazwa_firmy}, e-mail: {nr_wizytowki.adres_email}")
print("____________________________________________________________________________________________________________________")
for nr_wizytowki in po_nazwisku:
    print(f"imię: {nr_wizytowki.imie}, nazwisko: {nr_wizytowki.nazwisko}, firma: {nr_wizytowki.nazwa_firmy}, e-mail: {nr_wizytowki.adres_email}")
print("____________________________________________________________________________________________________________________")
for nr_wizytowki in po_emailu:
    print(f"imię: {nr_wizytowki.imie}, nazwisko: {nr_wizytowki.nazwisko}, firma: {nr_wizytowki.nazwa_firmy}, e-mail: {nr_wizytowki.adres_email}")

'''

print()
