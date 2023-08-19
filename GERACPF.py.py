import random

cpf_nove_dgt = ''
for i in range(9):
    cpf_nove_dgt += str(random.randint(0,9))

regressivo1 = 10
total_dig1 = 0

for i in cpf_nove_dgt:
    mult = int(i) * regressivo1
    total_dig1 = total_dig1 + mult
    
    regressivo1 -= 1

resutado_dig1 = (total_dig1*10) % 11

digito1 = resutado_dig1 if resutado_dig1 <= 9 else 0


cpf_dez_dgt = cpf_nove_dgt + str(digito1)

#print(cpf_dez_dgt)

regressivo2 = 11

total_dig2 = 0
for i in cpf_dez_dgt:
    total_dig2 += int(i) * regressivo2
    
    regressivo2 -= 1

digito2 =  (total_dig2 * 10) % 11

digito2 =  digito2 if digito2 <= 9 else 0

cpf_gerado = cpf_dez_dgt + str(digito2)

print(cpf_gerado)