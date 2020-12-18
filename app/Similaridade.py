from math import sqrt


def get_similaridade(usuario1, usuario2):
    si = {}
    for item in usuario1.opnioes:
        if item in usuario2.opnioes:
            si[item] = 1

    if len(si) == 0:
        return 0

    summation = sum([pow(usuario1.opnioes[item] - usuario2.opnioes[item], 2)
                     for item in usuario1.opnioes if item in usuario2.opnioes])

    result = 1 / (1 + sqrt(summation))
    result = "%.8f" % result
    result = float(result)

    return result
