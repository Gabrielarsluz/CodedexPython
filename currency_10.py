# User input

pesos = float(input("What do you have left in pesos? "))
soles = float(input("What do you have left in soles?" ))
reais = float(input("What do you have left in reais?" ))
amount = (reais/5.54) + (soles/3.62) + (pesos/4.121)
print(amount)