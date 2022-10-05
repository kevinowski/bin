translate = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
             9: "dziewięć", 10: "dziesięć", 11: "jedenaście", 12: "dwanaście", 13: "trzynaście", 14: "czternascie",
             15: "piętnaście", 16: "szesnaście", 17: "siedemnaście", 18: "osiemnaście", 19: "dziewiętnaście",
             20: "dwadzieścia", 30: "trzydzieści", 40: "czterdzieści", 50: "pięćdziesiąt", 60: "sześćdziesiąt",
             70: "siedemdziesiąt", 80: "osiemdziesiąt", 90: "dziewięćdziesiąt", 100: "sto", 200: "dwieście",
             300: "trzysta", 400: "czterysta", 500: "pięćset", 600: "sześćset", 700: "siedemset", 800: "osiemset",
             900: "dziewięćset", 1000: "tysiąc", "thousand1": "tysiące", "thousand2": "tysięcy", }


def slownie(n=1337):
    """You can translate from 1 to 9999
    """

    result = []

    units = n % 10
    n = n - units
    dozens = n % 100

    if dozens == 10 and units < 10:
        teens = dozens + units
        result.append(translate[teens])
    else:
        result.append(translate[units])
        result.append(translate[dozens])

    n = n - dozens
    hundreds = n % 1000
    result.append(translate[hundreds])
    n = n - hundreds
    thousands = n % 10000

    if 2000 <= thousands <= 4000:
        result.append(f"{translate[thousands / 1000]} {translate['thousand1']}")

    elif thousands >= 5000:
        result.append(f"{translate[thousands / 1000]} {translate['thousand2']}")

    else:
        result.append(translate[thousands])

    if thousands >= 10000:
        result.append(f"{translate[thousands / 10000]} {translate['thousand2']}")
    result = [i for i in result if len(i) > 2]
    return " ".join(reversed(result))


print(slownie(6512))
