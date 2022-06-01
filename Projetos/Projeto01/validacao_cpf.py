cpf_principal = input('Digite o CPF que deseja validar(sem pontos): ')
cpf_temporario = cpf_principal[:-2]
total = 0
total2 = 0

for n, cpf in enumerate(cpf_temporario, -10):
    # Soma e multiplicação de cada dígito sem dígito verificador
    total += + ((-1 * n) * int(cpf))

total = 11 - (total % 11)  # fazendo o cálculo do primeiro dígito verificador
if total > 9:
    cpf_temporario += str(0)
else:
    cpf_temporario += str(total)

for n, cpf in enumerate(cpf_temporario, -11):
    # Soma e multiplicação de cada dígito com primeiro dígito verificador
    total2 += + ((-1 * n) * int(cpf))

total2 = 11 - (total2 % 11)  # fazendo o cálculo do segundo dígito verificador
if total2 > 9:
    cpf_temporario += str(0)
else:
    cpf_temporario += str(total2)

if cpf_principal == cpf_temporario:  # Comparação entre os CPFs
    print(f'{cpf_principal} é valido')
else:
    print(f'{cpf_principal} não é valido')
