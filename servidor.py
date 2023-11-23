# CRIANDO UM SERVIDOR PYTHON
import socket
from datetime import *
 
host = '127.0.0.1'  # o mesmo que localhost
porta = 8800         # porta da conexão
 
soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #estou usando TCP/IP
recebe = (host, porta)
soquete.bind(recebe)
soquete.listen(2)
 
print('\nSERVIDOR INICIADO...IP: ', host, 'PORTA: ', porta,' EM: ',datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))
 
while True:
    conexao, enderecoIP = soquete.accept()
    print('\nSERVIDOR ACESSADO PELO CLIENTE:', enderecoIP, 'EM: ',datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))
 
    while True:
        mensagem = conexao.recv(2048)
        if not mensagem:
            break
        print('\nIP CLIENTE:', enderecoIP)
        print('MENSAGEN RECEBIDA: ', mensagem.decode(),' - ',datetime.now().strftime('%H:%M:%S'))
 
    print('CONEXÃO COM O CLIENTE FINALIZADA...', enderecoIP, ' EM: ',datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))
    conexao.close()