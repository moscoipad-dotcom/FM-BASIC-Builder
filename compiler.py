def compila_argomenti(argomenti):
    risultato = bytearray()

    for tipo, valore in argomenti:

        if tipo == "STRINGA":

            testo = valore.strip('"')
            risultato.extend(testo.encode("ascii"))

        elif tipo == "NUMERO":

            numero = int(valore)
            risultato.extend(numero.to_bytes(2, "little"))

    return risultato


def compila(programma):

    compilato = []

    for riga in programma:

        compilato.append({
            "linea": riga["linea"],
            "token": riga["token"],
            "argomenti": riga["argomenti"]
        })

    return compilato