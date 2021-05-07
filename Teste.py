import cartolafc
api = cartolafc.Api()
mercado = api.mercado()
print(mercado.rodada_atual)