peso = float(input('Peso: '))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
else:
    multa = excesso = 0

print ('Multa de R$ %.2f' %multa)
print ('Excesso: %.2f' %excesso)
