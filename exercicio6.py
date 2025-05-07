def cadastrarfilmes (nomefilme,descricao,classificacao,genero1,genero2):
    filmes = []

    filme = {
            "nomefilme": nomefilme,
            "descricao": descricao,
            "classificacao": classificacao,
            "generos": [genero1,genero2]
    }

    filmes.append(filme)

    return filmes

print (cadastrarfilmes("Spider Man, No Way Home", "Peter Parker tem a sua identidade secreta revelada e pede ajuda ao Doutor Estranho. Quando um feitiço para reverter o evento não sai como o esperado, o Homem-Aranha e seu companheiro dos Vingadores precisam enfrentar inimigos de todo o multiverso.", 12, "Ação", "Aventura" ))
