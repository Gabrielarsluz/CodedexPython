# Random

import random

quest = input("Ask a question answered with yes or no: ")

num = random.randint(1, 9)

if num == 1:
    print(quest)
    print("Yes - definitely. / Sim – com certeza.")
elif num == 2:
    print(quest)
    print("It is decidedly so. / É decididamente assim.")
elif num == 3:
    print(quest)
    print("Without a doubt. / Sem dúvida.")
elif num == 4:
    print(quest)
    print("Reply hazy, try again. / Resposta nebulosa, tente novamente.")
elif num == 5:
    print(quest)
    print("Ask again later. / Pergunte novamente mais tarde.")
elif num == 6:
    print(quest)
    print("Better not tell you now. / Melhor não te contar agora.")
elif num == 7:
    print(quest)
    print("My sources say no. / Minhas fontes dizem que não.")
elif num == 8:
    print(quest)
    print("Outlook not so good. / A perspectiva não é muito boa.")
elif num == 9:
    print(quest)
    print("Very doubtful. / Muito duvidoso.")
