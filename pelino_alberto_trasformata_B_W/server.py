# avvio prima il server


import socket #utiliziamo i socet TCP

# indirizzo dove il server è posizionato
HOST = "127.0.0.1"
# porta, si usa sempre una alta perché quelle basse sono gia utilzzate
PORT = 65432



def trasformata_barrow_wheel (stringa_analizzata: str):
    s = stringa_analizzata +"$"
    lista = []

    for i in range(len(s)):
        conta = s[0]
        nuova_Stringa = s + conta #banana$b
        nuova_Stringa = nuova_Stringa[1 :len(nuova_Stringa)]
        s = nuova_Stringa
        lista.append(nuova_Stringa)

    
    dimensione_lista = len(lista)

    for i in range(dimensione_lista-1):
        for j in range(0, dimensione_lista - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


    ultima_lettera =""
    for i in lista:
        ultima_lettera += i[-1]



    return ultima_lettera

# 1. aprire connessione al socket e assegnio un alias. Gli passo la famiglia e il tipo di socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
            # tupla
            
    s.bind((HOST,PORT)) # == bindo la tupla, assegnio al socket, l'IP e la PORTA 

    s.listen() #in ascolto per connessioni

    conn, addr = s.accept() #per accettare il collegamento, restituisce una tupla(due parametri) --> oggettto che rappresenta la connessione e ADDR è indirizzo del client

    # l'oggetto con è una risorsa è utilizzo il costrutto with per aprire 
    with conn:
        print(f"\nIl server sta trasformando la parola...")

        while True:
            data = conn.recv(1024) # in data metti quello che hai ricevuto (dimensione max che può ricevere)

            # se data è vuoto il client ha interrotto inaspettamente
            if not data:
                break

            risultato = trasformata_barrow_wheel(data.decode())

            conn.sendall(risultato.encode()) #per mandare a tutti la conferma delle lettura
            # con b iniziale mando il dato sotto forma di byte per rendere possibili l'invio tramite socket, la stessa cosa di f (= format) 
    print(f"\nIl server ha trasformato la parola.\n")


