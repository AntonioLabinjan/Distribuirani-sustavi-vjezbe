pozivni_brojevi = [
    {"01": {"mjesto": "Grad Zagreb i Zagrebačka županija", "vrsta": "fiksna"}},
    {"020": {"mjesto": "Dubrovačko‑neretvanska županija", "vrsta": "fiksna"}},
    {"021": {"mjesto": "Splitsko‑dalmatinska županija", "vrsta": "fiksna"}},
    {"022": {"mjesto": "Šibensko‑kninska županija", "vrsta": "fiksna"}},
    {"023": {"mjesto": "Zadarska županija", "vrsta": "fiksna"}},
    {"031": {"mjesto": "Osječko‑baranjska županija", "vrsta": "fiksna"}},
    {"032": {"mjesto": "Vukovarsko‑srijemska županija", "vrsta": "fiksna"}},
    {"033": {"mjesto": "Virovitičko‑podravska županija", "vrsta": "fiksna"}},
    {"034": {"mjesto": "Požeško‑slavonska županija", "vrsta": "fiksna"}},
    {"035": {"mjesto": "Brodsko‑posavska županija", "vrsta": "fiksna"}},
    {"040": {"mjesto": "Međimurska županija", "vrsta": "fiksna"}},
    {"042": {"mjesto": "Varaždinska županija", "vrsta": "fiksna"}},
    {"043": {"mjesto": "Bjelovarsko‑bilogorska županija", "vrsta": "fiksna"}},
    {"044": {"mjesto": "Sisačko‑moslavačka županija", "vrsta": "fiksna"}},
    {"047": {"mjesto": "Karlovačka županija", "vrsta": "fiksna"}},
    {"048": {"mjesto": "Koprivničko‑križevačka županija", "vrsta": "fiksna"}},
    {"049": {"mjesto": "Krapinsko‑zagorska županija", "vrsta": "fiksna"}},
    {"051": {"mjesto": "Primorsko‑goranska županija", "vrsta": "fiksna"}},
    {"052": {"mjesto": "Istarska županija", "vrsta": "fiksna"}},
    {"053": {"mjesto": "Ličko‑senjska županija", "vrsta": "fiksna"}},
    {"091": {"mjesto": "A1 Hrvatska", "vrsta": "mobilna"}},
    {"092": {"mjesto": "Tomato", "vrsta": "mobilna"}},
    {"095": {"mjesto": "Telemach", "vrsta": "mobilna"}},
    {"097": {"mjesto": "bonbon", "vrsta": "mobilna"}},
    {"098": {"mjesto": "Hrvatski Telekom", "vrsta": "mobilna"}},
    {"099": {"mjesto": "Hrvatski Telekom", "vrsta": "mobilna"}},
    {"0800": {"mjesto": "Besplatni pozivi", "vrsta": "posebne usluge"}},
    {"060": {"mjesto": "Komercijalni pozivi", "vrsta": "posebne usluge"}},
    {"061": {"mjesto": "Glasanje telefonom", "vrsta": "posebne usluge"}},
    {"064": {"mjesto": "Usluge s neprimjerenim sadržajem", "vrsta": "posebne usluge"}},
    {"065": {"mjesto": "Nagradne igre", "vrsta": "posebne usluge"}},
    {"069": {"mjesto": "Usluge namjenjene djeci", "vrsta": "posebne usluge"}},
    {"072": {"mjesto": "Jedinstveni pristupni broj za cijelu državu za posebne usluge", "vrsta": "posebne usluge"}}
]

def vrati_original_broj_sanity_check(broj):
  return broj

def ocisti_broj(broj):
    for znak in [' ', '-', '(', ')']:
        broj = broj.replace(znak, '')
    # vrajno slabo
    if broj.startswith('+385'):
        broj = '0' + broj[4:]
    elif broj.startswith('00385'):
        broj = '0' + broj[5:]
    elif broj.startswith('(385)'):
        broj = '0' + broj[5:]
    return broj

def pronadi_pozivni(broj):
    for duzina in range(4, 1, -1):
        prefix = broj[:duzina]
        for item in pozivni_brojevi:
            if prefix in item:
                return prefix, item[prefix]
    return None, None

def validiraj_broj_telefona(broj: str):
    broj = ocisti_broj(broj)
    pozivni, info_o_poz = pronadi_pozivni(broj)
    if not pozivni:
        return {"pozivni_broj": None, "broj_ostatak": None, "vrsta": None, "mjesto": None, "operater": None, "validan": False}
    
    broj_ostatak = broj[len(pozivni):]
    vrsta = info_o_poz["vrsta"]
    
    validan = False
    if vrsta == "fiksna" and len(broj_ostatak) in [6,7]:
        validan = True
    elif vrsta == "mobilna" and len(broj_ostatak) in [6,7]:
        validan = True
    elif vrsta == "posebne usluge" and len(broj_ostatak) == 6:
        validan = True
    
    mjesto = info_o_poz["mjesto"] if vrsta == "fiksna" else (None if vrsta != "posebne usluge" else None)
    operater = info_o_poz["mjesto"] if vrsta == "mobilna" else (None if vrsta != "posebne usluge" else None)
    if vrsta == "fiksna":
        operater = None
    if vrsta == "posebne usluge":
        mjesto = None
        operater = None
    
    return {
        "pozivni_broj": pozivni,
        "broj_ostatak": broj_ostatak,
        "vrsta": vrsta,
        "mjesto": mjesto,
        "operater": operater,
        "validan": validan
    }

# Primjeri:
print(vrati_original_broj_sanity_check("+385 52 622 503"))
print(validiraj_broj_telefona("+385 52 622 503"))
print(vrati_original_broj_sanity_check("0919135146"))
print(validiraj_broj_telefona("0919135146"))
print(validiraj_broj_telefona("0800-123456"))
print(validiraj_broj_telefona("55"))
