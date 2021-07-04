import json
import requests
import pandas as pd

TbUsuario = pd.DataFrame(columns=['userid','userstatus','maxScore','score','image','position','myRanking','round'])
TbMissoes = pd.DataFrame(columns=['userid','roundId','name','status','roundscorebonus','lastattemptstatus','approved','waiting','answerdate','showstars','showscore','stars'])
TbAtividades = pd.DataFrame(columns=['userid','ID_USUARIO','ID_ATIVIDADE','NU_PESO'])
TbAnswers = pd.DataFrame(columns=['userid','ID_USUARIO','ID_ATIVIDADE','DT_RESPOSTA','NU_PORCENTAGEM_ACERTOS'])


req = requests.get("https://87dyrojjxk.execute-api.us-east-1.amazonaws.com/dev/fiap/raw")
response = req.json()

#Lê o json em formato de Array (por camadas) criando tabelas normalizadas para o desafio
#Camada de Usuário
for item in response:
    list1 = [item['userid'],item['userstatus'],item['maxScore'],item['score'],item['image'],item['position'],item['myRanking'],item['round']]
    
    userid = item['userid']
    #Adiciona os usuários no DF TbUsuario
    TbUsuario.loc[len(TbUsuario)] = list1
    
    #Verifica se temos Missões para cada User
    rounds = item['rounds']

    #Camada de Missões
    for rd in rounds:
        try:
            list2 = [userid,rd['roundId'],rd['name'],rd['status'],rd['roundscorebonus'],rd['lastattemptstatus'],rd['approved'],rd['waiting'],rd['answerdate'],rd['showstars'],rd['showscore'],rd['stars']]
        except:
            list2 = [userid,rd['roundId'],rd['name'],rd['status'],rd['roundscorebonus'],None,rd['approved'],rd['waiting'],rd['answerdate'],rd['showstars'],rd['showscore'],rd['stars']]

        #Adiciona as missões no DF TbMissoes
        TbMissoes.loc[len(TbMissoes)] = list2

        activities = rd['activities']

        #Camada de Atividades
        for act in activities:
            list3 = [userid,act['ID_USUARIO'],act['ID_ATIVIDADE'],act['NU_PESO']]
   
            #Adiciona os usuários no DF TbUsuario
            TbAtividades.loc[len(TbAtividades)] = list3
            
            #Verifica se temos respostas para as atividades
            answers = act['answers']

            for asw in answers:
                list4 = [userid,asw['ID_USUARIO'],asw['ID_ATIVIDADE'],asw['DT_RESPOSTA'],asw['NU_PORCENTAGEM_ACERTOS']]
   
                #Adiciona os usuários no DF TbUsuario
                TbAnswers.loc[len(TbAnswers)] = list4

                

TbUsuario.to_csv('TbUsuario.txt')
TbMissoes.to_csv('TbMissoes.txt')
TbAtividades.to_csv('TbAtividades.txt')
TbAnswers.to_csv('TbAnswers.txt')

    