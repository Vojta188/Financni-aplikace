
while True:
    konec = input('Jestli chceš ukončit program napiš konec. V opačném případě stiskni enter.')
    if konec == 'konec':
        print("program byl ukončen")
        break

    stav_uctu = float(input('Zadej stav tvého účtu:'))
    mesicni_prijem = float(input('Zadej příjem za tento měsíc:'))
    mesicni_najem = float(input('Zadej měsíční nájem:'))
    mesicne_poplatky = float(input('Zadej ostatní poplatky za měsíc:'))
    dluhy = float(input('Zadej součet dlužných částek:'))
    utrata_jidlo = float(input('Denní útrata na jídlo:'))

    zbytek = mesicni_prijem - mesicni_najem - mesicne_poplatky - dluhy
    utrata_jidlo_mesic = 30 * utrata_jidlo
    kompletni_utrata = mesicni_najem + mesicne_poplatky + utrata_jidlo_mesic + dluhy
    konicky = mesicni_prijem - kompletni_utrata
    porovnani = konicky <= 0

    print('stav tvého účtu:',stav_uctu)
    print('Příjem tento měsíc:',mesicni_prijem)
    print('Měsíčně po zaplacení poplatku zbyde', zbytek)
    print('Měsíční útrata za jídlo:', utrata_jidlo_mesic)
    print('Kompletní útrata za Jídlo, Nájem, Poplatky:', kompletni_utrata)
    print('Peníze pro osobní potřebu:', konicky)


    if porovnani:
        {
        print("Špatný měsíc")
        }
    else:
        {
        print("Dobrý měsíc")
        }


print("Hezký den")
