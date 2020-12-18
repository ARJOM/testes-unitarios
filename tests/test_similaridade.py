#!/usr/bin/env python
# -- coding: utf-8 --

from app.Usuario import Usuario
from app.Similaridade import get_similaridade


def test_similaridade():
    usuario1 = Usuario("Ricart", "ricart@email.com", "senha123")
    usuario2 = Usuario("Glaymar", "glaymar@email.com", "mudar123")

    usuario1.add_opniao("Matrix", 4)
    usuario2.add_opniao("Matrix", 5)

    usuario1.add_opniao("Ultimato", 4)
    usuario2.add_opniao("Ultimato", 3)

    usuario1.add_opniao("Rogue One", 5)

    usuario2.add_opniao("Efeito Borboleta", 3)

    usuario2.add_opniao("Tá dando onda", 1)
    usuario1.add_opniao("Tá dando onda", 5)

    assert get_similaridade(usuario1, usuario2) == 0.19074357


def test_similaridade_sem_itens_em_comum():
    usuario1 = Usuario("Ricart", "ricart@email.com", "senha123")
    usuario2 = Usuario("Glaymar", "glaymar@email.com", "mudar123")

    usuario1.add_opniao("Deu a louca na chapeuzinho vermelha", 3)
    usuario1.add_opniao("Rogue One", 5)

    usuario2.add_opniao("Cinderela baiana", 5)
    usuario2.add_opniao("A revolução dos bichos", 2)

    assert get_similaridade(usuario1, usuario2) == 0
