import socket 

#uguale al server
HOST = "127.0.0.1" 

PORT = 65432

parola = input("\nInserisci la parola da trasformare con la Trasformata Barrow Wheel\n")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) #il clinet si connette mentre il server si binda
    

    #il client scrive al server 
    s.sendall(parola.encode())

    data = s.recv(1024) #accetto eventuale risposta del server 

    print(f"\nLa parola trasformata è: {data.decode()}\n")    

