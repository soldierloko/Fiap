import pyodbc 

server = 'fiapsprints.cq4ssupaqc1d.us-east-2.rds.amazonaws.com' 
database = 'FIAP' 
username = 'admin' 
password = 'Fr30ota*' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


def calculo(user):
    #Faz a consulta no banco pelo número do User
    cursor.execute("""SELECT  
                        A.[ID_USUARIO]
                        ,A.[NU_PESO]
                        ,B.[NU_PORCENTAGEM_ACERTOS]
                    FROM [FIAP].[dbo].[TbAtividades] A WITH (NOLOCK) 
                    INNER JOIN [FIAP].[dbo].[TbAnswers] B WITH (NOLOCK)
                    ON A.[ID_ATIVIDADE] = B.[ID_ATIVIDADE]
                        AND A.[ID_USUARIO] = B.[ID_USUARIO]
                    WHERE A.[ID_USUARIO] = 255480
                            AND B.[NU_PORCENTAGEM_ACERTOS] > 0 ;""") 
    row = cursor.fetchone()

    tt_ponto = 0 
    #Faz o cálculo para o User
    while row:


        print(row)
        row = cursor.fetchone()


#Chama a Função
calculo(255480)



cnxn.close()


# Score = 80,2
# Atividade 1 = (100/10)*1*1 = 10
# Atividade 2 = (100/10)*1*1 = 10
# Atividade 3 = (100/10)*1*1 = 10
# Atividade 4 = (100/10)*1*1 = 10
# Atividade 5 = (100/10)*6*0,67 = 40,2
