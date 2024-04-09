numero = int(input("escolha o numero da tabuada:"))

for c in range(1,21):
    print ("{} x {:2} = {}".format(numero,c,numero*c))