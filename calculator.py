num1=input('num1 \n')
if (num1.isdigit()):
  print('num1 =', num1)
else:
  print('num1 must be a number')
  exit()

op=input('op (+ - * /)\n')
if (op == '+' or op == '-' or op == '*' or op == '/'):
  print('op', op)
else:
  print('operator must be (+ - * /)')
  exit()

num2=input('num2 \n')
if (num2.isdigit()):
  print('num2 =', num2)
else:
  print('num2 must be a number')
  exit()

print('total =', num1, op, num2)

if (op == '+'):
  print (int(num1) + int(num2))
elif(op == '-'):
  print (int(num1) - int(num2))
elif (op == '*'):
  print (int(num1) * int(num2))
elif (op == '/'):
  print (int(num1) / int(num2))
else:
  print('num1 and num2 must be numbers, and operator must be (+ - * or /)')