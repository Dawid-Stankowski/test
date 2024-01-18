#!/usr/bin/env python3

def dodaj(x, y):
    return x + y

def odejmij(x, y):
    return x - y

def pobierz_dane():
    x = float(input("Podaj pierwszą liczbę: "))
    y = float(input("Podaj drugą liczbę: "))
    return x, y

def main():
    print("Prosty Kalkulator")
    print("1. Dodawanie")
    print("2. Odejmowanie")

    wybor = input("Wybierz operację (1/2): ")

    if wybor == '1':
        x, y = pobierz_dane()
        wynik = dodaj(x, y)
        operacja = "Dodawanie"
    elif wybor == '2':
        x, y = pobierz_dane()
        wynik = odejmij(x, y)
        operacja = "Odejmowanie"
    else:
        print("Nieprawidłowy wybór.")
        return

    print(f"{operacja} wynosi: {wynik}")

if __name__ == "__main__":
    main()

