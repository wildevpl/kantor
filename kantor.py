def convert():
# Wprowadź kurs skupu/Zalicz bez danych i przejdź dalej/Zamien , na .

    try:
        userusd = float(input("Wpisz kurs kupna USD: ").replace(",","."))
    except:
        pass
    try:
        userusd1 = float(input("Wpisz kurs sprzedaży USD: ").replace(",","."))
    except:
        pass
    try:
        usereuro = float(input("Wpisz kurs kupna EURO: ").replace(",","."))
    except:
        pass
    try:
        usereuro1 = float(input("Wpisz kurs sprzedaży EURO: ").replace(",","."))
    except:
        pass
    try:
        usergbp = float(input("Wpisz kurs kupna GBP: ").replace(",","."))
    except:
        pass
    try:
        usergbp1 = float(input("Wpisz kurs sprzedaży GBP: ").replace(",","."))
    except:
        pass
    try:
        userchf = float(input("Wpisz kurs kupna CHF: ").replace(",","."))
    except:
        pass
    try:
        userchf1 = float(input("Wpisz kurs sprzedaży CHF: ").replace(",","."))
    except:
        pass

# Kwota do wymiany

    try:
        kwota = float(input("Podaj kwotę do wymiany:"))
    except:
        print("Podaj wartość")


# Wybierz kierunek wymiany
    try:
        choice = input("Wybierz kierunek wymiany waluty: \n1) PLN>USD \n2) USD>PLN \n3) PLN>EURO \n4) EURO>PLN \n5) PLN>GBP \n6) GBP>PLN \n7) PLN>CHF \n8) CHF>PLN \nPodaj numer:")
    except:
        pass


# Funkcje obliczjące wymiane
    try:
        if  choice == "1":
                wynik = kwota/userusd
                print("\nKwota:","%.2f" % wynik,"USD")
        elif choice == "2":
                wynik = userusd1 * kwota
                print("%.2f" % wynik, "PLN")
        elif choice == "3":
                wynik = kwota/usereuro
                print ("%.2f" % wynik ,"EURO")
        elif choice == "4":
                wynik = usereuro1 * kwota
                print("%.2f" % wynik, "PLN")
        elif choice == "5":
                wynik = kwota / usergbp
                print("%.2f" % wynik, "GBP")
        elif choice == "6":
                wynik = kwota * usergbp1
                print("%.2f" % wynik, "PLN")
        elif choice == "7":
                wynik = kwota / userchf
                print("%.2f" % wynik, "CHF")
        elif choice == "8":
                wynik = kwota * userchf1
                print("%.2f" % wynik, "PLN")
    except:
        pass
convert()
input('\nPress ENTER to exit')