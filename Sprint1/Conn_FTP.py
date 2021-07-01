from ftplib import *

ftp = FTP('ftp.ibiblio.org')

print(ftp.getwelcome())

usuario=input("Digite o usuário: ")
senha = input("Digite uma senha: ")
ftp.login(usuario,senha)

print("Diretório atual do trabalho: ", ftp.pwd())

ftp.cwb('pub')

print("Diretório corrente: ", ftp.pwd())

print(ftp.retrlines('LIST'))
ftp.quit

