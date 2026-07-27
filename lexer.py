def analizza(testo):

    elementi = []

    corrente = ""
    dentro_stringa = False

    for carattere in testo:

        if carattere == '"':

            corrente += carattere

            if dentro_stringa:
                elementi.append(("STRINGA", corrente))
                corrente = ""
                dentro_stringa = False
            else:
                dentro_stringa = True

            continue

        if dentro_stringa:
            corrente += carattere
            continue

        if carattere.isspace():

            if corrente:

                elementi.append(classifica(corrente))
                corrente = ""

            continue

        if carattere == "=":

            if corrente:
                elementi.append(classifica(corrente))
                corrente = ""

            elementi.append(("UGUALE", "="))
            continue

        corrente += carattere

    if corrente:
        elementi.append(classifica(corrente))

    return elementi


def classifica(testo):

    if testo.isdigit():
        return ("NUMERO", int(testo))

    if testo.isidentifier():
        return ("IDENTIFICATORE", testo)

    return ("TESTO", testo)