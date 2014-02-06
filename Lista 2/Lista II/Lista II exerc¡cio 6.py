valor = float(input('Valor por hora: '))
horas = int(input('Horas tralhadas: '))
bruto = valor * horas
ir = bruto * 0.11
inss = bruto * 0.08
sind = bruto * 0.05
liquido = bruto - ir - inss - sind
print ('+Salário Bruto:\t\t R$ %10.2f' %bruto)
print ('-IR:\t\t\t R$ %10.2f' %ir)
print ('-INSS:\t\t\t R$ %10.2f' %inss)
print ('-Sindicato:\t\t R$ %10.2f' %sind)
print ('=Salário Líquido:\t R$ %10.2f' %liquido)

