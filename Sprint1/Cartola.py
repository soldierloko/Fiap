import pandas as pd
import os
import sys
from tkinter import filedialog
from tkinter import *

def valida_arquivo():
    #Abre a janela FileDialog para selecionar o arquivo
    filename = filedialog.askdirectory(title="Selecione o Local dos Arquivos: ")
    #Verifica se o caminho foi selecionado 
    if filename == '':
        sys.exit()

    return filename


#Busca o caminho do diretório dos arquivos
caminho = valida_arquivo()


#Cria o DF de saída
df_final = pd.DataFrame(columns=('atletas.nome'
                        ,'atletas.slug'
                        ,'atletas.apelido'
                        ,'atletas.foto'
                        ,'atletas.atleta_id'
                        ,'atletas.rodada_id'
                        ,'atletas.clube_id'
                        ,'atletas.posicao_id'
                        ,'atletas.status_id'
                        ,'atletas.pontos_num'
                        ,'atletas.preco_num'
                        ,'G'
                        ,'I'
                        ,'RB'
                        ,'CA'
                        ,'PE'
                        ,'A'
                        ,'SG'
                        ,'DD'  
                        ,'FT'  
                        ,'GS'  
                        ,'CV'  
                        ,'GC'))

#Coloca o caminho dos arquivos um uma lista
for nome in os.listdir(caminho):

    #verifica se é um Excel
    if '.csv' in nome:
        
        #Atribui o arquivo ao DataFrame
        df = pd.read_csv(caminho + "/" + nome)

        #Faz o Merge entre os DataFrames
        frames = [df_final,df]
        df_final = pd.concat(frames)
        
df_final.to_csv(caminho + "/" +"Rodadas_2018.txt")  
print('Concluido com Sucesso!')    
