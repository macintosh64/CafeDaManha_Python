def pedido():
    print("Quer fazer um pedido?")
    print("Por favor.")

def esperar():
    print ("Ok. Espere 15 minutos, por favor!")

def bomapetite():
    print ("Aproveite sua refeição!")

pedido()
print("1.Ovos")
print("2.Panquecas")
print("3.Waffles")
print("4.Mingau")
EscolhaPrincipal = int(input("Escolha um item do café: "))

if (EscolhaPrincipal == 2):
    Refeição = "Panquecas"
elif (EscolhaPrincipal == 3):
    Refeição = "Waffles"

if (EscolhaPrincipal == 1):
    print("1. Torradas")
    print("2. Massa fermentada")
    print("3.Pão de forma")
    print("4.Panquecas")
    Pão = int(input("Escolha um tipo de pão: "))
    
    if (Pão == 1):
        print("Você escolheu ovos com torradas")
    elif (Pão == 2):
        print("Você escolheu ovos com massa fermentada")
    elif (Pão == 3):
        print("Você escolheu ovos com pão de forma")
    elif (Pão == 4):
        print("Você escolheu ovoc com panquecas")
    else:
        print("Temos ovos, mas nenhum pão")

elif (EscolhaPrincipal == 2) or (EscolhaPrincipal == 3):
    print("1.Melado de cana")
    print("2.Frutas da estação")
    print("3.Polvilho doce")
    Cobertura = int(input("Escolha a cobertura: "))

    if (Cobertura == 1):
        print("Você escolheu " + Refeição + "com melado de cana.")
    elif (Cobertura == 2):
        print("Você escolheu " + Refeição + "com frutas da estação.")
    elif (Cobertura == 3):
        print("Você escolheu " + Refeição + "com polvilho doce.")
    else:
        print("Nós temos " + Refeição + ", mas nenhuma cobertura.")

elif (EscolhaPrincipal == 4):
    print("Você escolheu mingau")

else:
    print("Nós não servimos café da manhã")

esperar()

s = input("Os pratos chegaram? Se sim, tecle 1")
pratos = int(s)
if pratos == 1:
    bomapetite()
else:
    print("Vamos esperar")
