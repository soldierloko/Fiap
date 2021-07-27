import pyodbc 
import pandas as pd
import boto3
from  datetime import date

server = 'fiapsprints.cq4ssupaqc1d.us-east-2.rds.amazonaws.com' 
database = 'FIAP' 
username = 'admin' 
password = 'Fr30ota*' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Engage')

def insLambda(ID_USUARIO,ID_ROUND,scoremission,dia):
    table.put_item(
        Item={
            "userId" : ID_USUARIO,
        	"roundId" : ID_ROUND,
        	"score" : scoremission,
        	"date" : dia
            
        }
    )
    return {
        'body': 'Item added'
    }

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
                            WHERE EXISTS (SELECT TOP 1 [roundId]
                                                    ,[approved]
                                                FROM [FIAP].[dbo].[TbMissoes] C WITH (NOLOCK)
                                                WHERE A.ROUNDID = C.ROUNDID
                                                        AND [approved] = 1)
                                                        AND A.[ID_USUARIO] = ?
                                                        AND A.ROUNDID = ? """,con=cnxn, params=(user,round)) 
                        
    
    #Muda o tipo de dado para inteiro
    df['NU_PESO'] = df['NU_PESO'].astype('int64')
    #Soma os pesos de casa Missão
    soma = df.pivot_table("NU_PESO", ["ID_USUARIO", "ROUNDID"], aggfunc="sum").reset_index()
    #Agrega a informação de count na tabela
    df = pd.merge(df,soma[['ID_USUARIO','ROUNDID','NU_PESO']], how='inner', on=['ID_USUARIO','ROUNDID'], suffixes=('t_1','t_2'))

    #Cálcula o Score Mission
    df['Score_Atividade'] = df.apply(lambda x: (100/x['NU_PESOt_2']) * float(x['NU_PESOt_1']) * float(x['NU_PORCENTAGEM_ACERTOS']),axis=1)

    #Agrega para saber a pontuação total por missões
    df = df.pivot_table("Score_Atividade", ["ID_USUARIO", "ROUNDID"], aggfunc="sum").reset_index()
    #Coloca a data de inserção
    df['Date'] = date.today() 

    ID_USUARIO = df.values.tolist()[0][0]
    ID_ROUND = df.values.tolist()[0][1]
    scoremission = df.values.tolist()[0][2]
    dia = df.values.tolist()[0][3]
    return [ID_USUARIO,ID_ROUND,scoremission,dia]

#Coloca os resultados em uma lista
list = calculo(255480,52472)

insLambda(list[0],list[1],list[2],list[3])


cnxn.close()
