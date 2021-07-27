import pyodbc 
import pandas as pd
from  datetime import date

server = 'fiapsprints.cq4ssupaqc1d.us-east-2.rds.amazonaws.com' 
database = 'FIAP' 
username = 'admin' 
password = 'Fr30ota*' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


def calculo(user,round):
    #Faz a consulta no banco pelo número do User
    df = pd.read_sql_query("""SELECT  
                                A.[ID_USUARIO]
                                ,A.ROUNDID
                                ,A.[NU_PESO]
                                ,B.[NU_PORCENTAGEM_ACERTOS]
                            FROM [FIAP].[dbo].[TbAtividades] A WITH (NOLOCK) 
                            INNER JOIN [FIAP].[dbo].[TbAnswers] B WITH (NOLOCK)
                            ON A.[ID_ATIVIDADE] = B.[ID_ATIVIDADE]
                                AND A.[ID_USUARIO] = B.[ID_USUARIO]
                            INNER JOIN (SELECT TOP 1 [roundId]
                                            ,[approved]
                                        FROM [FIAP].[dbo].[TbMissoes] WITH (NOLOCK)) C
                            ON A.ROUNDID = C.ROUNDID
                            WHERE [approved] = 1
                                    AND A.[ID_USUARIO] = ?
                                    AND A.ROUNDID = ? """,con=cnxn, params=(user,round)) 
    
    
    scoremission = 0
    for index, row in df.iterrows():
        #Grava os Id's para gravação no redis
        ID_USUARIO = row['ID_USUARIO']
        ID_ROUND = row['ROUNDID']

        #Cálculo para score de missão
        val_Atividade = (100/10) * float(df['NU_PESO'][index]) * float(df['NU_PORCENTAGEM_ACERTOS'][index])

        scoremission =  scoremission + val_Atividade
    dia = date.today()
    return [ID_USUARIO,ID_ROUND,scoremission,dia]
#Chama a Função
print(calculo(255480,52472))


cnxn.close()


# Score = 80,2
# Atividade 1 = (100/10)*1*1 = 10
# Atividade 2 = (100/10)*1*1 = 10
# Atividade 3 = (100/10)*1*1 = 10
# Atividade 4 = (100/10)*1*1 = 10
# Atividade 5 = (100/10)*6*0,67 = 40,2
