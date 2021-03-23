import socket
resp ='S'
while (resp == 'S'):
    url = input("DIgite um URL: ")
    ip=socket.gethostbyname(url)
    print("O IP referente à URL informada é: ", ip)
    resp=input("Digite <S> para continuar: ").upper