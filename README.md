# Burrows-Wheeler Transform – Client/Server

## Description
School project developed in **Python** to implement the **Burrows-Wheeler Transform (BWT)** through a **Client-Server** architecture using TCP sockets.

The client allows the user to enter a word or sentence and sends it to the server. The server receives the text, calculates the Burrows-Wheeler Transform by creating and sorting the rotations of the string using **Bubble Sort**, and finally sends the result back to the client.

The project was personally developed as a laboratory exercise, with the aim of exploring both how the BWT works and how communication between a client and a server can be implemented using sockets.

---

## Technologies Used
* **Python**
* **TCP Sockets**
* **Visual Studio Code**
* **Bubble Sort**

---

## How It Works
The project consists of two Python programs:

### Client
The `client.py` file is responsible for:
1. Asking the user to enter a word or sentence.
2. Establishing a TCP connection with the server.
3. Sending the input to the server.
4. Receiving the transformed string.
5. Displaying the result to the user.

### Server
The `server.py` file is responsible for:
1. Creating and configuring the TCP socket.
2. Waiting for a client connection.
3. Receiving the input sent by the client.
4. Calculating the Burrows-Wheeler Transform.
5. Sending the transformed string back to the client.

## The client and server communicate through the local address `127.0.0.1` using port `65432`.
## Burrows-Wheeler Transform

The transformation is performed by:
1. Adding the special `$` character to the input string.
2. Generating all rotations of the resulting string.
3. Sorting the rotations lexicographically.
4. Taking the last character from each sorted rotation.
5. Returning the resulting string.

The implementation uses **Bubble Sort** to order the generated rotations.

---

## How to Run
Make sure **Python** is installed on your computer.

### 1. Start the server
Open a terminal in the project folder and run:

```bash
python server.py
```
The server will start listening for incoming client connections.

### 2. Start the client
Open a **second terminal** in the same project folder and run:

```bash
python client.py
```

Enter the word or sentence you want to transform.
The client will send the input to the server, which will calculate the BWT and return the result.

---

## Example
An example of the interaction is:
```text
Client:
Inserisci la parola da trasformare con la Trasformata Barrow Wheel
banana

Server:
Il server sta trasformando la parola...

Client:
La parola trasformata è: annb$aa
```

The exact output depends on the text entered by the user.

---

## 🎓 Project Context
This project was developed as a **school laboratory exercise** to put into practice concepts related to:

* Python programming
* Algorithms and data manipulation
* Sorting algorithms
* Client-Server architecture
* TCP socket communication
* Burrows-Wheeler Transform

The project was developed personally as part of an informatics laboratory assignment.

---

## 📄 Documentation
The repository also contains the project report:

**`Relazione Trasformata BW.pdf`**

## The report explains the development process, the Python implementation, the socket methods used, the Bubble Sort algorithm and the results obtained.

## 👤 Author

**Alberto Pelino**

School project – Istituto di Istruzione Superiore "Archimede", Treviglio.
