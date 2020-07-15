print("")
print("----------------------------------------------------------------------------------------------------")
print("Função para o exercício 4")


def media(vetor):
    somador = 0
    for num in vetor:
        somador += num # somador = somador + num
    media = somador / len(vetor)
    return media

import numpy as np
def variancia(vetor):
    var=0
    med=np.mean(vetor)
    comp=len(vetor)
    for num in vetor:
        var = (var + ((num-med)**2)/comp)
    return var


