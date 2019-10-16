import socket
s = socket.socket()
host = input(str("Host Adini Giriniz : "))
port = 1027
s.connect((host,port))
print("Baglantis kuruldu ... ")

filename = input(str("Gelecek Dosyanın Adini Giriniz : "))
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("Dosya Basarili Sekilde Alindi.")
