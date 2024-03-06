#Trabalhar com else

a = 27
b = 93

if a >= b:
  print(a)
else:
  print(b)


#Trabalhar com elif
c = 110
d = 10

if a < b:
  print('a é menor que b')
elif a == b:
  print('a é igual a b')
elif b == 100:
  print('b é igual a cem')
else:
  print('a é maior que b')

#Trabalhar com lógica condicional aninhada
e = 16
f = 25
g = 27

if e > f:
  if f > g:
    print ('e é maior que f e f é maior que g')
  else:
    print('e é maior que f e menor que g')
elif e == f:
  print('e é igual a f')
else:
  print('e é menor que f')