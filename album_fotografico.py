import csv

def carica_da_file(file_path):
    """Carica le foto dal file, creando un nuovo anno ogni volta che compare per la prima volta"""
    # TODO
    with open(file_path, 'r') as csvfile:
        album = {}
        reader = csv.DictReader(csvfile, skipinitialspace= True)    # Ora il file è una lista di dizionari
        for row in reader:          # Per ogni dizionario della lista
            #anno = int(row['anno']) # Trasforma la chiave in un intero
            if row['anno'] not in album:   # Se la chiave 'anno' non è presente nel dizionario album
                album[row['anno']] = []    # allora la chiave "valore della chiave 'row['anno']'" è una chiave il cui valore è una lista vuota
            album[row['anno']].append(row) # Una volta che la chiave è stata creata, aggiungi il dizionario row alla lista di valori
        print(row.keys())
    return album



def aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path):
    """Aggiunge una foto all'album, creando l'anno al volo se non è ancora presente"""
    # TODO

    '''
    with open(file_path, 'r') as csvfile:
        album = {}
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row[' anno'] not in album:
                album[row[' anno']] = []
            album[row[' anno']].append(row)
    '''

    foto = {
        'codice' : codice,
        'titolo' : titolo,
        'autore' : autore,
        'mese' : mese,
        'anno' : anno,
    }
    if foto['anno'] not in album:
        album[foto['anno']] = []
    album[foto['anno']].append(foto)

    with open(file_path, 'a', newline= '', encoding= 'utf-8') as csvfile:
        campi = ['codice', 'titolo', 'autore', 'mese', 'anno']
        writer = csv.DictWriter(csvfile, fieldnames=campi)
        writer.writerow(foto)




    return album



def cerca_foto(album, codice):
    """Cerca una foto nell'album dato il codice"""
    # TODO
    for anno in album: #Album è un dizionario, le chiavi sono gli anni
        for foto in album[anno]: #per ogni foto di ogni chiave del dizionario 'anno'
            if foto['codice'] == codice: #se il codice della foto è uguale al codice inserito
                '''for chiave in foto:
                    print(foto[chiave])'''
                print(f'{foto['codice']}, {foto['titolo']}, {foto['autore']}, {foto['mese']}, {foto['anno']}') #stampa la foto
                


def elenco_foto_anno_per_titolo(album, anno):
    """Ordina i titoli delle foto di un dato anno in ordine alfabetico"""
    # TODO
    for anno in album:
        album_ordinato = sorted(album[anno], key=lambda k: k['titolo'])
    print(f'{anno} : {album_ordinato}')
    return album_ordinato





def main():
    album = []
    file_path = "album_fotografico.csv"

    while True:
        print("\n--- MENU ALBUM FOTOGRAFICO ---")
        print("1. Carica album da file")
        print("2. Aggiungi una nuova foto")
        print("3. Cerca una foto per codice")
        print("4. Elenco foto di un anno (ordinato per titolo)")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                album = carica_da_file(file_path)
                if album is not None:
                    break

        elif scelta == "2":
            if not album:
                print("Prima carica l'album da file.")
                continue

            codice = input("Codice della foto: ").strip()
            titolo = input("Titolo: ").strip()
            autore = input("Autore: ").strip()
            try:
                mese = int(input("Mese (1-12): ").strip())
                anno = int(input("Anno: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per mese e anno.")
                continue

            foto = aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path)
            if foto:
                print(f"Foto aggiunta con successo!")
            else:
                print("Non è stato possibile aggiungere la foto.")

        elif scelta == "3":
            if not album:
                print("L'album è vuoto.")
                continue

            codice = input("Inserisci il codice della foto da cercare: ").strip()
            risultato = cerca_foto(album, codice)
            if risultato:
                print(f"Foto trovata: {risultato}")
            else:
                print("Foto non trovata.")

        elif scelta == "4":
            if not album:
                print("L'album è vuoto.")
                continue

            try:
                anno = int(input("Inserisci l'anno da consultare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_foto_anno_per_titolo(album, anno)
            if titoli is not None:
                print(f'\nFoto del {anno}:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))
            else:
                print(f"Nessuna foto trovata per l'anno {anno}.")

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()
