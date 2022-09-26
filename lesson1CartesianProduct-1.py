print('Cartesian Product of 2 sets')
X=[1,2,3,4,5,6,7,8,9,0]
Y=[11,12,13,14,15,16,17,18,19,20]
print('X x Y = {',end='')
for x in X:
  print(' ')
  for y in Y:
    print('(',x,',',y,'), ',end='')
print('}')