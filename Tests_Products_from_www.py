# python (lokation)/Tests_Products_from_www.py

from Products_from_www import extract

def test_extract_should_strip_texts():
    html = '<b> should be stripped </b>'
    got = extract(html, '//b')
    expected = ['should be stripped']
    assert got == expected


def test_extract_converts_newlines_to_spaces():
    html = '<b>should be stripped\na new line</b>'
    got = extract(html, '//b')
    expected = ['should be stripped a new line']
    assert got == expected


# for testing you need to have downloaded HTML-file.html
def test_scrapper_reallife_webpage():
    with open('data/HTML-file.html',encoding='utf-8-sig') as stream:
        html = stream.read()
    got = extract(html, "//*[@id='categoryMainContent']/div/section/div/div/section/section/h3")
    # example of the expected data:
    expected = [ 
        "Zlewozmywak granitowy Burnell 1-komorowy z półociekaczem czarny",
        "Zlewozmywak granitowy Laveo Celebes 1-komorowy z baterią czarny",
        "Zlewozmywak granitowy Romesco 1-komorowy z ociekaczem i akcesoriami czarny",
        "Zlewozmywak stalowy Romesco 1-komorowy z ociekaczem i akcesoriami",
        "Zlewozmywak granitowy Romesco 1,5-komorowy bez ociekacza z akcesoriami czarny",
        "Zlewozmywak granitowy Romesco 1-komorowy bez ociekacza z akcesoriami czarny",
        "Zlewozmywak stalowy Romesco 1-komorowy bez ociekacza z akcesoriami",
        "Zlewozmywak stalowy Romesco 1,5-komorowy bez ociekacza z akcesoriami",
        "Zlewozmywak kompozytowy Ising 1-komorowy z ociekaczem czarny",
        "Zlewozmywak stalowy Petrina 1-komorowy bez ociekacza",
        "Zlewozmywak ceramiczny Cooke&Lewis Burbank 1-komorowy z ociekaczem biały",
        "Zlewozmywak granitowy Hirase 1-komorowy bez ociekacza czarny",
        "Zlewozmywak stalowy Turing 1-komorowy z ociekaczem satyna",
        "Zlewozmywak stalowy Sagan 1-komorowy z ociekaczem polerowany",
        "Zlewozmywak granitowy Cooke&Lewis Galvani 1-komorowy z ociekaczem czarny",
        "Zlewozmywak Tectonite Franke Orion OID 611-78 1-komorowy z ociekaczem onyx",
        "Zlewozmywak stalowy Franke Basil 2-komorowy bez ociekacza z syfonem",
        "Zlewozmywak stalowy nakładany Mayr 1-komorowy z ociekaczem gładki",
        "Zlewozmywak tectonite Franke Sirius S2D 611-78 1-komorowy z ociekaczem onyx",
        "Zlewozmywak ceramiczny Cooke&Lewis Burbank 1,5-komorowy z ociekaczem biały",
        "Zlewozmywak granitowy Hahn 1-komorowy bez ociekacza czarny",
        "Zlewozmywak granitowy Cooke&Lewis Lavoisier 1-komorowy z ociekaczem czarny",
        "Zlewozmywak kompozytowy Ising 1-komorowy z ociekaczem biały",
        "Zlewozmywak stalowy Bohm 2-komorowy bez ociekacza len",
        "Zlewozmywak kompozytowy Ising 1-komorowy z ociekaczem szary",
        "Zlewozmywak stalowy gospodarczy 1-komorowy bez ociekacza polerowany",
        "Zlewozmywak stalowy Gamow 1-komorowy bez ociekacza satyna",
        "Zlewozmywak granitowy Cooke&Lewis Hawking 1-komorowy z ociekaczem czarny",
        "Zlewozmywak stalowy Cooke&Lewis Liebig 1-komorowy z ociekaczem satyna",
        "Zlewozmywak granitowy Cooke&Lewis Arber 1,5-komorowy z ociekaczem czarny",
        "Zlewozmywak granitowy Cooke&Lewis Arber 1-komorowy z ociekaczem czarny",
        "Zlewozmywak stalowy Apollonia 1-komorowy z ociekaczem",
        "Zlewozmywak stalowy gospodarczy Kuchinox Chios 1-komorowy",
        "Zlewozmywak Tectonite Franke Orion OID 651 1,5-komorowy z ociekaczem onyx",
        "Zlewozmywak stalowy Nakaya 1-komorowy z ociekaczem polerowany",
        "Klipsy Kuchinox do montażu zlewu z taśmą",
        "Sitko uniwersalne do zlewozmywaka Cooke&Lewis",
        "Korek uniwersalny do zlewozmywaka Cooke&Lewis",
        "Zwijana mata GoodHome Datil gr. 8 mm",
        "Durszlak nakładany GoodHome Datil 16,5 x 54,5 cm",
        "Mata do zlewozmywaków GoodHome Datil 30 x 27 cm szara",
        "Dozownik kuchenny GoodHome Datil 23 x 13 cm chrom",
        "Dozownik kuchenny GoodHome Datil 19 x 13 cm szczotkowany",
        "Dozownik kuchenny płynu do naczyń Laveo czarny",
        "Organizer na zlewozmywak GoodHome Datil 22 x 9 cm",
        "Koszyk do zlewu GoodHome Datil",
        "Zlewozmywak stalowy Turing 1-komorowy z ociekaczem len",
    ]
    assert got == expected