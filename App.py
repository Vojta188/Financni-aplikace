stav_uctu = float(input('Zadej stav tvého účtu:'))
mesicni_prijem = float(input('Zadej příjem za tento měsíc:'))
mesicni_najem = float(input('Zadej měsíční nájem:'))
mesicne_poplatky = float(input('Zadej ostatní poplatky za měsíc:'))
dluhy = float(input('Zadej součet dlužných částek:'))
utrata_jidlo = float(input('Denní útrata na jídlo:'))

zbytek = mesicni_prijem - mesicni_najem - mesicne_poplatky - dluhy
utrata_jidlo_mesic = 30 * utrata_jidlo

print('stav tvého účtu:',stav_uctu)
print('Příjem tento měsíc:',mesicni_prijem)
print('Měsíčně po zaplacení poplatku zbyde', zbytek)
print('Měsíční útrata za jídlo:', utrata_jidlo_mesic)



