import json
import requests
import pandas as pd

TbIndex = pd.DataFrame(columns=['count'])
TbRanking = pd.DataFrame(columns=['userid','user_name','score','max_score','bonus','position','image'])

req = requests.get("https://87dyrojjxk.execute-api.us-east-1.amazonaws.com/dev/fiap/ranking?skip=1&take=20")
response = req.json()

print(response)

#Lê o json em formato de Array (por camadas) criando tabelas normalizadas para o desafio
#Camada de Usuário
for item in response:
    list1 = [item['count']]
    print(list1)
    # #Adiciona os usuários no DF TbUsuario
    # TbIndex.loc[len(TbIndex)] = list1
    
    # #Verifica se temos Missões para cada User
    results = item['results']

    #Camada de Missões
    for rd in results:
        list2 = [item['userid'],item['user_name'],item['score'],item['max_score'],item['bonus'],item['position'],item['image']]
        
        #Adiciona as missões no DF TbMissoes
        TbRanking.loc[len(TbRanking)] = list2

    #     activities = rd['activities']

    #     #Camada de Atividades
    #     for act in activities:
    #         list3 = [act['ID_USUARIO'],act['ID_ATIVIDADE'],act['NU_PESO']]
   
    #         #Adiciona os usuários no DF TbUsuario
    #         TbAtividades.loc[len(TbAtividades)] = list3
            
    #         #Verifica se temos respostas para as atividades
    #         answers = act['answers']

    #         for asw in answers:
    #             list4 = [asw['ID_USUARIO'],asw['ID_ATIVIDADE'],asw['DT_RESPOSTA'],asw['NU_PORCENTAGEM_ACERTOS']]
   
    #             #Adiciona os usuários no DF TbUsuario
    #             TbAnswers.loc[len(TbAnswers)] = list4

print(TbIndex)
print(TbRanking)
                

TbIndex.to_csv('TbIndex.txt')
TbRanking.to_csv('TbRanking.txt')
# TbAtividades.to_csv('TbAtividades.txt')
# TbAnswers.to_csv('TbAnswers.txt')

    