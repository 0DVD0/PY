# Aceasta este sarcina pentru lecția 7 legată de comentarii, continuarea liniilor și instrucțiuni condiționale.

# Creați o variabilă numită number și atribuiți-i o valoare întreagă.

# CODUL TĂU VINE MAI JOS:
number = 1
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este pozitiv și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number > 0:
    print("Nr. pozitiv")
else:
    print("Nr. negativ")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este par și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if (number % 2) == 0:
    print("Nr.par")
else:
    print("Nr. nu este par")

# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este impar și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if (number % 2) != 0:
    print("Nr.impar")
else:
    print("Nr. nu este impar")

# CODUL TĂU VINE MAI SUS:

# Creați o variabilă text și atribuiți-i un șir de caractere.

# CODUL TĂU VINE MAI JOS:
text = 'Hello Wolrd in Python'
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
py = "Python"
ja = "Java"
if py in text:
    print("Cuvantul Python este")
else:
    print('Cuvantul python nu este')
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Java" și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if ja in text:
    print("Cuvantul Java este")
else:
    print("Cuvantul Java nu este")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.
# în cazul în care nu conține, verificați dacă conține cuvântul "Java" și afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if py in text:
    print("Cuvantul Python este")
elif ja in text:
    print("Cuvantul Java este")
else:
    print("Nici unul din cuvintele mentionate nu sunt")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și cuvântul "Java" și afișați un mesaj corespunzător.
# În cazul în care conține doar unul dintre ele, afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if (py in text) and (ja in text):
    print("Cuvantul Python si Java este")
elif (py in text) or (ja in text):
    print("Unul din cuvintele mantionate se afla in fraza")
else:
    print("Nici unul din cuvintele mentionate nu sunt")
# CODUL TĂU VINE MAI SUS:

# Extrageți de la tastatură utilizând funcția input un număr de la 1 la 5 și atribuiți-l variabilei number.
# Folosiți o instrucțiune condițională pentru a printa un mesaj corespunzător în funcție de numărul introdus.
# pentru 1 - printați "Unu"
# pentru 2 - printați "Doi"
# pentru 3 - printați "Trei"
# pentru 4 - printați "Patru"
# pentru 5 - printați "Cinci"

# CODUL TĂU VINE MAI JOS:
i = 0
numere = ["unu", "doi", "trei", "patru", "cinci"]
number = int(input("dati un numar de la 1-5: "))
while i != 5:
    if number == i + 1:
        print(numere[i])
        break
    else:
        i += 1
# CODUL TĂU VINE MAI SUS:
