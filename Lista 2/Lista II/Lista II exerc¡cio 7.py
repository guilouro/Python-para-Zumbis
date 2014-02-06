m = int(input('Metros: '))
if m % 54 == 0:
  latas = m / 54
else:
  latas = int(m / 54) + 1

valor = latas * 80
print ('%d latas' %latas)
print ('Total: R$ %.2f' %valor)
