from pojisteni import DatabazePojisteni

# Vytvoření instance třídy DatabazePojisteni
databaze = DatabazePojisteni()

# Pět pojištěnců vytvořených pomocí slovníků
pojistenci = [
    {"jmeno": "Jan", "prijmeni": "Novak", "vek": 30, "telefon": "+420 111 111 111"},
    {"jmeno": "Marie", "prijmeni": "Vesela", "vek": 25, "telefon": "+420 222 222 222"},
    {"jmeno": "Petr", "prijmeni": "Dvorak", "vek": 40, "telefon": "+420 333 333 333"},
    {"jmeno": "Eva", "prijmeni": "Hruskova", "vek": 35, "telefon": "+420 444 444 444"},
    {"jmeno": "Lukas", "prijmeni": "Prochazka", "vek": 45, "telefon": "+420 555 555 555"}
]

# Přidání pojištěnců do databáze pomocí cyklu for
for pojistenec in pojistenci:
    databaze.vytvor_pojisteneho(pojistenec["jmeno"], pojistenec["prijmeni"], pojistenec["vek"], pojistenec["telefon"])

while True:
    print("\n")
    print("1. Vytvořit pojištěného")
    print("2. Seznam pojištěných")
    print("3. Vyhledat pojištěného")
    print("4. Konec")

    volba = input("\nVyberte možnost: ")

    if volba == "1":
        jmeno = input("\nZadejte jméno: ")
        prijmeni = input("Zadejte příjmení: ")
        vek = int(input("Zadejte věk: "))
        telefon = input("Zadejte telefonní číslo: ")
        databaze.vytvor_pojisteneho(jmeno, prijmeni, vek, telefon)
        print("\nPojištěný byl úspěšně vytvořen.")

    elif volba == "2":
        databaze.vypis_seznam_pojisteni()

    elif volba == "3":
        jmeno = input("\nZadejte jméno pojištěného: ")
        prijmeni = input("Zadejte příjmení pojištěného: ")
        pojisteny = databaze.najdi_pojisteneho(jmeno, prijmeni)
        if pojisteny:
            print("\nPojištěný nalezen: ")
            print(pojisteny)
        else:
            print("\nPojištěný nebyl nalezen.")

    elif volba == "4":
        break



    else:
        print("\nNeplatná volba")
