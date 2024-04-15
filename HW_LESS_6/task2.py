# Aceasta este a doua ta sarcină legată de seturi

# Creați un set gol numit `numbers_set`

# CODUL TĂU VINE MAI JOS:
numbers_set = set()
# CODUL TĂU VINE MAI SUS:

# Acum adăugați numerele de la 1 la 5 în setul `numbers_set`

# CODUL TĂU VINE MAI JOS:
for i in range(1, 6):
    numbers_set.add(i)
# CODUL TĂU VINE MAI SUS:

# Acum afișați setul `numbers_set`

# CODUL TĂU VINE MAI JOS:
print(numbers_set)
# CODUL TĂU VINE MAI SUS:

# Acum adăugați numărul 6 la setul `numbers_set`

# CODUL TĂU VINE MAI JOS:
numbers_set.add(6)
# CODUL TĂU VINE MAI SUS:

# Acum adaugă numerele de la 1 la 5 în setul `numbers_set` folosind metoda update()

# CODUL TĂU VINE MAI JOS:
for i in range(1, 5):
    numbers_set.update({i})
print(numbers_set)

# Extrageți numărul 3 din setul `numbers_set`

# CODUL TĂU VINE MAI JOS:
numbers_set.remove(3)
print(numbers_set)
# CODUL TĂU VINE MAI SUS:

# Ștergeți un număr inexistent din setul `numbers_set` fără a genera o eroare

# CODUL TĂU VINE MAI JOS:
numbers_set.discard(10)
print(numbers_set)
# CODUL TĂU VINE MAI SUS:

# Verificați dacă numărul 3 există în setul `numbers_set`

# CODUL TĂU VINE MAI JOS:
if 3 in numbers_set:
    print("True")
else:
    print("False")
# CODUL TĂU VINE MAI SUS:

# Verificați elementele comune din setul `numbers_set` și setul {4, 5, 6, 7}

#
numb_set = {4, 5, 6, 7}
num_inter = numbers_set.intersection(numb_set)
print(num_inter)
# CODUL TĂU VINE MAI SUS:

# Verificați elementele diferite din setul `numbers_set` și setul {4, 5, 6, 7}

# CODUL TĂU VINE MAI JOS:
numb_set = {1, 2, 3, 4, 5, 6, 7}
num_diff = numbers_set.symmetric_difference(numb_set)
print(num_diff)
# CODUL TĂU VINE MAI SUS:

# Verificați dacă setul `numbers_set` este un subset al setului {1, 2, 3, 4, 5, 6, 7}

# CODUL TĂU VINE MAI JOS:
if numbers_set.issubset(numb_set):
    print("True")
else:
    print("False")
# CODUL TĂU VINE MAI SUS:

# Verificați dacă setul {1, 2, 3, 4, 5, 6, 7} este un subset al setului `numbers_set`

# CODUL TĂU VINE MAI JOS:
if numb_set.issubset(numbers_set):
    print("True")
else:
    print("False")
# CODUL TĂU VINE MAI SUS:

# Verificați dacă setul `numbers_set` este un superset al setului {1, 2, 3, 4, 5, 6, 7}

# CODUL TĂU VINE MAI JOS:
if numbers_set.issuperset(numb_set):
    print("True")
else:
    print("False")
# CODUL TĂU VINE MAI SUS:

# Verificați dacă setul {1, 2, 3, 4, 5, 6, 7} este un superset al setului `numbers_set`

# CODUL TĂU VINE MAI JOS:
if numb_set.issuperset(numbers_set):
    print("True")
else:
    print("False")
# CODUL TĂU VINE MAI SUS:

# Afișați lungimea setului `numbers_set`

# CODUL TĂU VINE MAI JOS:
print(len(numbers_set))
# CODUL TĂU VINE MAI SUS:

# Ștergeți toate elementele din setul `numbers_set`

# CODUL TĂU VINE MAI JOS:
numbers_set.clear()
# CODUL TĂU VINE MAI SUS:

# Afișați setul `numbers_set` pentru a verifica dacă a fost șters

# CODUL TĂU VINE MAI JOS:
print({numbers_set})
# CODUL TĂU VINE MAI SUS:

# Asta a fost tot pentru a doua ta sarcină legată de seturi
