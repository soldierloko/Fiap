# import cartolafc
# api = cartolafc.Api()
# mercado = api.mercado()
# print(mercado.rodada_atual)



import json, mechanize
 
# br será o objeto que simula o browser
br = mechanize.Browser()
 
# Abre a página de login Cartola através do mechanize
br.open('https://loginfree.globo.com/login/438')
 
#Na página, selecionamos o primeiro form presente. 'nr=0' indica que estamos selecionando o form de índice 0 dentre os encontrados.
#Analisando a página, vemos que realmente só há um form.
#Após selecionarmos o form, preenchemos os campos com username e senha que permitam fazer o login.
 
br.select_form(nr=0)
br.form['login-passaporte'] = 'SEU_EMAIL'
br.form['senha-passaporte'] = 'SUA_SENHA'
br.submit()