a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
if a >= b and a >= c:
    print ('Maior: %d' %a)
elif b >= c:
    print ('Maior: %d' %b)
else:
    print ('Maior: %d' %c)

if a <= b and a <= c:
    print ('Menor: %d' %a)
elif b <= c:
    print ('Menor: %d' %b)
else:
    print ('Menor: %d' %c)
