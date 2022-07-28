import re


def fomarta_string(cnpj):
    return re.sub(r'[^ 0-9]', '', cnpj)


def calcula_digito(cnpj):
    contador = 5
    while True:
        if len(cnpj) == 14:
            break
        total = 0
        for digitos in cnpj:
            total += + (int(digitos) * contador)
            contador = contador - 1
            if contador == 1:
                contador = 9
        total = 11 - (total % 11)
        if total > 9:
            cnpj += str(0)
            contador = 6
        else:
            cnpj += str(total)
            contador = 6
    return cnpj


def valida_cnpj(orinal, copia):
    if orinal == copia:
        print('O CNPj é valido')
    else:
        print('O CNPJ não é valido')


cnpj_original = input('Digite o CNPJ: ')
cnpj_original = fomarta_string(cnpj_original)
cnpj_copia = calcula_digito(cnpj_original[:-2])
valida_cnpj(cnpj_original, cnpj_copia)
