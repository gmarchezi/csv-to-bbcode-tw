import sys

#Le o arquivo CSV e retorna uma lista
def Ler_CSV(arquivo,separador):
    arq_entrada = open(arquivo,'r')
    l_arquivo = arq_entrada.readlines()
    l_entrada = []

    for i in l_arquivo:
        i = i.rstrip()
        separado = i.split(separador)
        l_entrada.append(separado)
    arq_entrada.close()

    return l_entrada

#Recebe uma lista de lista, contendo os elementos do CSV de entrada e tem como saída um arquivo .txt contendo a tabela em BBCode
#Tabela Genérica
def CSV_to_BBCode(lista_entrada):
    arquivo_saida = open('tabela_bbcode.txt','w')
    arquivo_saida.write('[table]\n')
    arquivo_saida.write('[**]')

    for x in range(len(lista_entrada[0])):
        if x < len(lista_entrada[0])-1:
            arquivo_saida.write(lista_entrada[0][x]+'[||]')
        else:
            arquivo_saida.write(lista_entrada[0][x]+'[/**]\n')
            del(lista_entrada[0])

    for i in range(len(lista_entrada)):
        arquivo_saida.write('[*]')
        for y in range(len(lista_entrada[0])):
            if y < len(lista_entrada[0])-1:
                arquivo_saida.write(lista_entrada[i][y]+'[|]')
            else:
                arquivo_saida.write(lista_entrada[i][y]+'\n')
    arquivo_saida.write('[/table]')
    arquivo_saida.close()



def main():
    lista_entrada = Ler_CSV(sys.argv[1],sys.argv[2])
    CSV_to_BBCode(lista_entrada)



if __name__ == "__main__":
    main()