from parser import parse_file
from tokenizer import tokenize
from compiler import compila
from writer import scrivi_prg

print("=" * 40)
print("FM BASIC Builder 0.1")
print("=" * 40)
print()

# Parser
programma = parse_file("source/agenda.bas")

# Tokenizer
programma_tokenizzato = tokenize(programma)

# Compiler
programma_compilato = compila(programma_tokenizzato)

# Writer
scrivi_prg(programma_compilato, "output/agenda.prg")

print()
print("Compilazione completata.")
print()

for riga in programma_compilato:

    print("------------------------------")
    print("Linea :", riga["linea"])
    print("Token :", hex(riga["token"]))

    print("Argomenti:")

    for elemento in riga["argomenti"]:
        print("   ", elemento)