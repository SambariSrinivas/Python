import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('scoreboard.eks.centralqa.de', 443))
score_board = 'GET http://scoreboard.eks.centralqa.de/scoreboard HTTP/1.0\n\n'.encode()
mysocket.send(score_board)
while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
mysocket.close()
