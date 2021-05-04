
while True:
    konec = input('Jestli chceš ukončit program napiš konec. V opačném případě stiskni enter.')
    if konec == 'konec':
        print("program byl ukončen")
        break
    
    novy_stav_uctu_nastaveni = input("Chcete nastavit nový stav účtu napište ANO:")
    if(novy_stav_uctu_nastaveni == 'ANO'):
    
        novy_stav_uctu = float(input('Zadej novy stav tvého účtu:'))
    
    
    
    
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

    print('\n STATUS','\n stav tvého účtu:' ,novy_stav_uctu, 'Kč', '\n Příjem tento měsíc:',mesicni_prijem, 'Kč', '\n Měsíčně po zaplacení poplatku zbyde', zbytek, 'Kč', '\n Měsíční útrata za jídlo:', utrata_jidlo_mesic, 'Kč', '\n Kompletní útrata za Jídlo, Nájem, Poplatky:', kompletni_utrata, 'Kč', '\n Peníze pro osobní potřebu:', konicky, 'Kč')


    stav_uctu = novy_stav_uctu



    if porovnani:
        {
        print("Špatný měsíc zbylo:", konicky)
        }
    else:
        {
        print("Dobrý měsíc zbylo:", konicky)
        }
    

print("Hezký den")
