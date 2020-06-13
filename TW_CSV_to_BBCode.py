from datetime import date
import sys

#Le o arquivo CSV e retorna uma lista
# Parametros --> (nome do arquivo CSV, separador do arquivo CSV)

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
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%d-%m-%Y')
    nome_arquivo = 'Tabela_Gen_' + data_atual_str +'.txt'
    arquivo_saida = open(nome_arquivo,'w')
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


#Recebe uma lista de lista, contendo os elementos do CSV de entrada e tem como saída um arquivo .txt contendo a tabela em BBCode
#Tabela HALL OF FAME
def CSV_to_HoF(lista_entrada):
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%d-%m-%Y')
    nome_arquivo = 'Tabela_HOF_' + data_atual_str +'.txt'
    arquivo_saida = open(nome_arquivo,'w')
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
        contador = 0
        for y in range(len(lista_entrada[0])):
            if y < len(lista_entrada[0])-1:
                if contador == 0:
                    if lista_entrada[i][y] == '1':
                        arquivo_saida.write('[b][color=#2eb92e]'+lista_entrada[i][y]+'st'+'[/color][/b]'+'[|]')
                    elif lista_entrada[i][y] == '2':
                        arquivo_saida.write('[b][color=#b9b92e]'+lista_entrada[i][y]+'nd'+'[/color][/b]'+'[|]')
                    elif lista_entrada[i][y] == '3':
                        arquivo_saida.write('[b][color=#b92e2e]'+lista_entrada[i][y]+'rd'+'[/color][/b]'+'[|]')
                    else:
                        arquivo_saida.write('[b]'+lista_entrada[i][y]+'th[/b]'+'[|]')
                else:
                    arquivo_saida.write('[player]'+lista_entrada[i][y]+'[/player]'+'[|]')
            else:
                if lista_entrada[i][0] == '1':
                    arquivo_saida.write('[b][color=#2eb92e]'+lista_entrada[i][y]+'[/color][/b]'+'\n')
                elif lista_entrada[i][0] == '2':
                    arquivo_saida.write('[b][color=#b9b92e]'+lista_entrada[i][y]+'[/color][/b]'+'\n')
                elif lista_entrada[i][0] == '3':
                    arquivo_saida.write('[b][color=#b92e2e]'+lista_entrada[i][y]+'[/color][/b]'+'\n')
                else:
                    arquivo_saida.write('[b]'+lista_entrada[i][y]+'[/b]'+'\n')
            contador = contador + 1 
    arquivo_saida.write('[/table]')
    arquivo_saida.close()


def main():
    lista_entrada = Ler_CSV(sys.argv[1],sys.argv[2])
    menu = input('1. Tabela Genérica\n2. Tabela HALL OF FAME \nDigite:')
    if menu == '1':
        CSV_to_BBCode(lista_entrada)
    elif menu == '2':
        CSV_to_HoF(lista_entrada)



if __name__ == "__main__":
    main()