from lexer import analizza


def parse_file(nomefile):

    with open(nomefile, "r") as f:
        righe = f.readlines()

    programma = []

    for riga in righe:

        riga = riga.strip()

        if not riga:
            continue

        parti = riga.split(maxsplit=2)

        numero = int(parti[0])
        comando = parti[1]

        testo_argomenti = ""

        if len(parti) == 3:
            testo_argomenti = parti[2]

        programma.append({
            "linea": numero,
            "comando": comando,
            "argomenti": analizza(testo_argomenti)
        })

    return programma