# Esercitazione manipolazione stringhe in python

Questo esercizio ha lo scopo di utilizzare le conoscenze acquisite nello studio delle stringhe in python per crearea un piccolo script che
possa calcolare il codice fiscale di un cittadino italiano

# Strutturazione 

Le funzioni sono strutturate secondo i criteri per il calcolo del codice fiscale italiano e sono divise per tipo di calcolo:
- Cognome
- Nome
- Data di nascita e sesso
- Comune
alla fine di questi calcoli separati si prende il codicefiscale non completo per trovare l'ultima cifra ovvero il codice di controllo.

Sono presenti delle helper function per controllare l'input dell'utente e assicurarsi che siano corrette per la funzione in cui andranno inserite

# Cosa manca

- Helper function controllo data di nascita non controlla se l'anno sia bisestile o se il mese sia di 31 o 30 giorni
- Spostamento delle funzioni di calcolo codice fiscale in un modulo separato così da semplificare lo script di visualizzazione e input

# Utilizzo

Lo script non ha nessuna dipendenza, è importante avere il file csv dei codici di catasto dei comuni(presente nella repo) nella stessa cartella dello script e non modificarne il nome.

- Clona la repo

```bash
git clone
