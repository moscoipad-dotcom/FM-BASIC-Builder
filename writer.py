from compiler import compila_argomenti


def scrivi_prg(programma, nomefile):

    with open(nomefile, "wb") as f:

        # Indirizzo di caricamento BASIC ($0801)
        f.write(bytes([0x01, 0x08]))

        indirizzo = 0x0801

        for riga in programma:

            corpo = bytearray()

            # Token del comando
            corpo.append(riga["token"])

            # Argomenti compilati
            corpo.extend(compila_argomenti(riga["argomenti"]))

            # Fine linea BASIC
            corpo.append(0x00)

            # Calcolo indirizzo della riga successiva
            prossimo = indirizzo + len(corpo) + 4

            # Puntatore alla riga successiva
            f.write(prossimo.to_bytes(2, "little"))

            # Numero di linea
            f.write(riga["linea"].to_bytes(2, "little"))

            # Corpo della riga
            f.write(corpo)

            indirizzo = prossimo

        # Fine programma
        f.write(bytes([0x00, 0x00]))

    print("File creato:", nomefile)