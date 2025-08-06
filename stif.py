nome = input("qual o seu nome?")
nota1 = int (input("quanto vc tirou?"))
nota2 = int (input("quanto vc tirou?"))
nota3 = int (input("quanto vc tirou?"))
try:
    média = (nota1 + nota2 + nota3) / 3
    with open("pessoa.txt","a")as arquivo:
        arquivo.write(nome "+ " | " + f" {nota1} )" + " | " + f" {nota2} " + " | " + f"media: {media: 2f} \n"
except:
    print("digite as notas corretamentes")
