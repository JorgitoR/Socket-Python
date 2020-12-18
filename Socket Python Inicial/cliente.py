import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.26"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    mensaje = msg.encode(FORMAT)
    msg_length = len(mensaje)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(mensaje)
    print(client.recv(2048).decode(FORMAT))


send("Hola Mundo")
input()
send("Hello Everyone")
input()
send("Hola Jorgito")

send(DISCONNECT_MESSAGE)