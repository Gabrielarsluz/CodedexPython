print('ATM 2')

pin = int(input('Enter your PIN: '))

while pin != 1991:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1991:
  print('PIN accepted!')
