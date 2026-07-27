from tokens import TOKENS

def tokenize(programma):

    risultato = []

    for riga in programma:

        token = TOKENS.get(riga["comando"])

        risultato.append({
            "linea": riga["linea"],
            "token": token,
            "comando": riga["comando"],
            "argomenti": riga["argomenti"]
        })

    return risultato