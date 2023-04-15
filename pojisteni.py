class Pojisteny:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}, {self.vek} let, tel. {self.telefon}"


class DatabazePojisteni:
    def __init__(self):
        self.seznam_pojisteni = []

    def vytvor_pojisteneho(self, jmeno, prijmeni, vek, telefon):
        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.seznam_pojisteni.append(pojisteny)

    def vypis_seznam_pojisteni(self):
        for pojisteny in self.seznam_pojisteni:
            print(pojisteny)

    def najdi_pojisteneho(self, jmeno, prijmeni):
        for pojisteny in self.seznam_pojisteni:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                return pojisteny
        return None



