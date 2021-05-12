# import cartolafc
# api = cartolafc.Api()
# mercado = api.mercado()
# print(mercado.rodada_atual)



import cartolafc

api = cartolafc.Api(email='email@email.com', password='s3nh4', attempts=5, redis_url='redis://localhost:6379/0')

print(api.amigos())
print(api.clubes())
print(api.liga(nome='Virtus Premier League'))
print(api.liga(nome='Nacional', page=2))
print(api.liga(nome='Nacional', page=3, order_by=cartolafc.RODADA))
print(api.liga(slug='virtus-premier-league'))
print(api.ligas(query='Virtus'))
print(api.ligas_patrocinadores())
print(api.mercado())
print(api.mercado_atletas())
print(api.parciais())
print(api.partidas(1))
print(api.pontuacao_atleta(81682))
print(api.pos_rodada_destaques())
print(api.time(id=2706236))
print(api.time(id=2706236, as_json=True))
print(api.time(nome='ALCAFLA FC'))
print(api.time(nome='ALCAFLA FC', as_json=True))
print(api.time(slug='alcafla-fc'))
print(api.time(slug='alcafla-fc', as_json=True))
print(api.time_logado())
print(api.time_parcial(id=2706236))
print(api.time_parcial(nome='ALCAFLA FC'))
print(api.time_parcial(slug='alcafla-fc'))
print(api.times(query='Faly'))