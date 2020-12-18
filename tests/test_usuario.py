from app.Usuario import Usuario


def test_chave_sendo_adicionadas_corretamente():
    usuario = Usuario("Testerson", "teste@teste.com", "123testando")

    usuario.add_opniao("axe", 5)
    usuario.add_opniao("gospel", 5)
    usuario.add_opniao("pagode", 1)
    usuario.add_opniao("axe", 5)

    assert len(usuario.opnioes) == 3



def test_senha_Crypto():
    usuario = Usuario("Jardilene", "teste@teste.com", "123testando")
    assert usuario.senha != "123testando"



def test_senha_correta():
    usuario = Usuario("Vanderlei", "teste@teste.br", "123testando")
    assert usuario.verifica_senha("123testando")