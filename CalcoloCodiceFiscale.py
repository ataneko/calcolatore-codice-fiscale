def calc_cognome(cognome):
    consonanti = ''.join([c for c in cognome.upper() if c.isalpha() and c not in 'AEIOU'])
    vocali = ''.join([v for v in cognome.upper() if v.isalpha() and v in 'AEIOU'])
    
    codice = (consonanti + vocali + 'XXX')[0:3]
    return codice

def calc_nome(nome):
    consonanti = ''.join([c for c in nome.upper() if c.isalpha() and c not in 'AEIOU'])
    vocali = ''.join([v for v in nome.upper() if v.isalpha() and v in 'AEIOU'])
    if len(consonanti) >= 4:
        codice = consonanti[0] + consonanti[2] + consonanti[3]
    else:
        codice = (consonanti + vocali + 'XXX')[0:3]
    return codice

def calc_data_nascita(data_nascita, sesso):
    mesi = {
        1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'H',
        7: 'L', 8: 'M', 9: 'P', 10: 'R', 11: 'S', 12: 'T'
    }
    
    giorno, mese, anno = map(int, data_nascita.split('/'))
    anno_codice = str(anno)[-2:]
    mese_codice = mesi[mese]
    
    if sesso.upper() == 'F':
        giorno += 40
    
    giorno_codice = f"{giorno:02d}"
    
    return anno_codice + mese_codice + giorno_codice

def calc_codice_comune(comune):
    codici= open("gi_comuni_nazioni_cf.csv","r")

    for line in codici:
        parts = line.strip().split(';')
        if parts[1].upper() == comune.upper():
            return parts[2]
        
    return ValueError("Comune non trovato nel database.")

def calc_codice_controllo(cf_parziale): 
    valori_dispari = {
        '0': 1, '1': 0, '2': 5, '3': 7, '4': 9,
        '5': 13, '6': 15, '7': 17, '8': 19, '9': 21,
        'A': 1, 'B': 0, 'C': 5, 'D': 7, 'E': 9,
        'F': 13, 'G': 15, 'H': 17, 'I': 19, 'J': 21,
        'K': 2, 'L': 4, 'M': 18, 'N': 20, 'O': 11,
        'P': 3, 'Q': 6, 'R': 8, 'S': 12, 'T': 14,
        'U': 16, 'V': 10, 'W': 22, 'X': 25, 'Y': 24,
        'Z': 23
    }
    
    valori_pari = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
        'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
        'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
        'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
        'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
        'Z': 25
    }
    valori_resto ={
        0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
        5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
        10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O',
        15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
        20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y',
        25: 'Z'
    }

    somma = 0
    for i in range(len(cf_parziale)):
        if (i + 1) % 2 == 0:
            somma += valori_pari[cf_parziale[i]]
        else:
            somma += valori_dispari[cf_parziale[i]]

    resto = somma % 26
    return valori_resto[resto]

def ask_for_text(prompt):
    in_text = input(prompt)
    while not(in_text.isalpha()):
        in_text = input(prompt)
    return in_text

def ask_date(prompt):
    in_date = input(prompt)
    while True:
        try:
            giorno, mese, anno = map(int, in_date.split('/'))
            if 1 <= giorno <= 31 and 1 <= mese <= 12 and anno > 0:
                return in_date
            else:
                in_date = input(prompt)
        except ValueError:
            in_date = input(prompt)

def main():
    cognome = ask_for_text("Inserisci il cognome: ")
    nome = ask_for_text("Inserisci il nome: ")
    data_nascita = ask_date("Inserisci la data di nascita (gg/mm/aaaa): ")
    sesso = input("Inserisci il sesso (M/F): ")
    comune = input("Inserisci il comune di nascita(completo): ")

    codice_cognome = calc_cognome(cognome)
    codice_nome = calc_nome(nome)
    codice_data = calc_data_nascita(data_nascita, sesso)
    codice_comune = calc_codice_comune(comune)

    cf_parziale = codice_cognome + codice_nome + codice_data + codice_comune
    codice_controllo = calc_codice_controllo(cf_parziale)

    codice_fiscale = cf_parziale + codice_controllo
    print("Il Codice Fiscale è:", codice_fiscale)

if __name__ == "__main__":
    main()

