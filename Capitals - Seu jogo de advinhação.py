

def jogar():

    inicio_regras()

    capital_italia= str("Roma").upper()
    capital_alemanha= str("Berlim").upper()
    capital_inglaterra= str("Londres").upper()
    capital_franca= str("Paris").upper()
    capital_estadosunidos = str("Washington").upper()
    capital_brasileira = str("Brasília").upper()
    capital_hermanos = str("Buenos Aires").upper()
    capital_mexicana = str("Cidade do Mexico").upper()
    escolha_continente = int(input("Escolha o Continente: "))

    if escolha_continente == 1:
        print("Digite o numero correspondente do País")
        print("[1]EUA  [2]Brasil  [3]Argentina [4]México")
        paises_americanos = int(input("Escolha o País: "))
        if paises_americanos == 1:
            print("Qual a Capital dos Estados Unidos da América?")
            capital_eua = str(input("Digite aqui a capital: ")).upper()
            if capital_eua == capital_estadosunidos:
                print("Você Acertou")
            while capital_eua != capital_estadosunidos and paises_americanos == 1:

                if capital_eua == capital_estadosunidos:
                    print("Você Acertou")
                if capital_eua != capital_estadosunidos:
                    print("Você Errou!! Você quer Tentar Novamente??")
                    print("[1]Sim  [2]Não")
                    escolha_de_continuidade = int(input("Digite aqui sua escolha: "))
                    continuidade = escolha_de_continuidade

                    if continuidade == 1:
                        print("Vamos tentar Novamente")
                        print("*******************")
                        capital_eua = str(input("Digite aqui a capital: ")).upper()
                        print("*******************")
                        if capital_eua == capital_estadosunidos:
                            print("Você Acertou")

                    if continuidade == 2:
                        print(" ")
                    break
        if paises_americanos == 2:
            print("Qual a Capital do Brasil?")
            capital_bra = str(input("Digite aqui a capital: ")).upper()
            if capital_bra == capital_brasileira:
                print("Você Acertou")
            while capital_bra != capital_brasileira and paises_americanos == 2:

                if capital_bra == capital_brasileira:
                    print("Você Acertou")
                if capital_bra != capital_brasileira:
                    print("Você Errou!! Você quer Tentar Novamente??")
                    print("[1]Sim  [2]Não")
                    escolha_de_continuidade= int(input("Digite aqui sua escolha: "))
                    continuidade = escolha_de_continuidade

                    if continuidade == 1:
                        print("Vamos tentar Novamente")
                        print("*******************")
                        capital_bra = str(input("Digite aqui a capital: ")).upper()
                        print("*******************")
                        if capital_bra == capital_brasileira:
                            print("Você Acertou")

                    if continuidade == 2:
                        print(" ")
                    break
        if paises_americanos == 3:
            print("Qual a Capital da Argentina?")
            capital_arg = str(input("Digite aqui a capital: ")).upper()
            if capital_arg == capital_hermanos:
                print("Você Acertou")
            while capital_arg != capital_hermanos and paises_americanos == 3:

                if capital_arg == capital_hermanos:
                    print("Você Acertou")
                if capital_arg != capital_hermanos:
                    print("Você Errou!! Você quer Tentar Novamente??")
                    print("[1]Sim  [2]Não")
                    escolha_de_continuidade = int(input("Digite aqui sua escolha: "))
                    continuidade = escolha_de_continuidade

                    if continuidade == 1:
                        print("Vamos tentar Novamente")
                        print("*******************")
                        capital_arg = str(input("Digite aqui a capital: ")).upper()
                        print("*******************")
                        if capital_arg == capital_hermanos:
                            print("Você Acertou")

                    if continuidade == 2:
                        print(" ")
                    break
        if paises_americanos == 4:
            print("Qual a Capital do México?")
            capital_mex = str(input("Digite aqui a capital: ")).upper()
            if capital_mex == capital_mexicana:
                print("Você Acertou")
            while capital_mex != capital_mexicana and paises_americanos == 4:

                if capital_mex == capital_mexicana:
                    print("Você Acertou")
                if capital_mex != capital_mexicana:
                    print("Você Errou!! Você quer Tentar Novamente??")
                    print("[1]Sim  [2]Não")
                    escolha_de_continuidade = int(input("Digite aqui sua escolha: "))
                    continuidade = escolha_de_continuidade

                    if continuidade == 1:
                        print("Vamos tentar Novamente")
                        print("*******************")
                        capital_mex = str(input("Digite aqui a capital: ")).upper()
                        print("*******************")
                        if capital_mex == capital_mexicana:
                            print("Você Acertou")

                    if continuidade == 2:
                        print(" ")
                    break
    if escolha_continente == 2:
        print("Digite o numero correspondente do País")
        print("[1]França  [2]Inglaterra  [3]Itália [4]Alemanha")
        paises_europeus = int(input("Escolha o País: "))
        if paises_europeus == 1:
            print("Qual a Capital da França?")
            capital_paris = str(input("Digite aqui a capital: ")).upper()
            if capital_paris == capital_franca:
                print("Você Acertou")
            while capital_paris != capital_franca and paises_europeus == 1:

                if capital_paris == capital_franca:
                    print("Você Acertou")
                if capital_paris != capital_franca:
                    print("Você Errou!! Você quer Tentar Novamente??")
                    print("[1]Sim  [2]Não")
                    escolha_de_continuidade = int(input("Digite aqui sua escolha: "))
                    continuidade = escolha_de_continuidade

                    if continuidade == 1:
                        print("Vamos tentar Novamente")
                        print("*******************")
                        capital_paris = str(input("Digite aqui a capital: ")).upper()
                        print("*******************")
                        if capital_franca == capital_franca:
                            print("Você Acertou")

                    if continuidade == 2:
                        print(" ")
                    break
        if paises_europeus == 2:
            print("Qual a Capital da Inglaterra?")
            capital_londres = str(input("Digite aqui a capital: ")).upper()
            if capital_londres == capital_inglaterra:
                print("Você Acertou")
            while capital_londres != capital_inglaterra and paises_europeus == 2:

                if capital_londres == capital_inglaterra:
                    print("Você Acertou")
                if capital_londres != capital_inglaterra:
                    print("Você Errou!! Você quer Tentar Novamente??")
                    print("[1]Sim  [2]Não")
                    escolha_de_continuidade = int(input("Digite aqui sua escolha: "))
                    continuidade = escolha_de_continuidade

                    if continuidade == 1:
                        print("Vamos tentar Novamente")
                        print("*******************")
                        capital_londres = str(input("Digite aqui a capital: ")).upper()
                        print("*******************")
                        if capital_londres == capital_inglaterra:
                            print("Você Acertou")

                    if continuidade == 2:
                        print(" ")
                    break
        if paises_europeus == 3:
            print("Qual a Capital da Itália?")
            capital_roma = str(input("Digite aqui a capital: ")).upper()
            if capital_roma == capital_italia:
                print("Você Acertou")
            while capital_roma != capital_italia and paises_europeus == 3:

                if capital_roma == capital_italia:
                    print("Você Acertou")
                if capital_roma != capital_italia:
                    print("Você Errou!! Você quer Tentar Novamente??")
                    print("[1]Sim  [2]Não")
                    escolha_de_continuidade = int(input("Digite aqui sua escolha: "))
                    continuidade = escolha_de_continuidade

                    if continuidade == 1:
                        print("Vamos tentar Novamente")
                        print("*******************")
                        capital_roma = str(input("Digite aqui a capital: ")).upper()
                        print("*******************")
                        if capital_roma == capital_italia:
                            print("Você Acertou")

                    if continuidade == 2:
                        print(" ")
                    break
        if paises_europeus == 4:
            print("Qual a Capital da Alemanha?")
            capital_berlim = str(input("Digite aqui a capital: ")).upper()
            if capital_berlim == capital_alemanha:
                print("Você Acertou")
            while capital_berlim != capital_alemanha and paises_europeus == 4:

                if capital_berlim == capital_alemanha:
                    print("Você Acertou")
                if capital_berlim != capital_alemanha:
                    print("Você Errou!! Você quer Tentar Novamente??")
                    print("[1]Sim  [2]Não")
                    escolha_de_continuidade = int(input("Digite aqui sua escolha: "))
                    continuidade = escolha_de_continuidade

                    if continuidade == 1:
                        print("Vamos tentar Novamente")
                        print("*******************")
                        capital_berlim = str(input("Digite aqui a capital: ")).upper()
                        print("*******************")
                        if capital_berlim == capital_alemanha:
                            print("Você Acertou")

                    if continuidade == 2:
                        print(" ")
                    break#al#  #

    fim_de_jogo()


def fim_de_jogo():
    print ( "********************" )
    print ( "Fim de Jogo" )
    print ( "********************" )
def inicio_regras():
    print ( "____________________________________________________________________________________________________" )
    print ( "JOGO ADVINHAÇÃO DE CAPITAIS" )
    print ( "____________________________________________________________________________________________________" )
    print ( "****************************************************************************************************" )
    print ( "                                 REGRA DO JOGO                                                      " )
    print ( "1 - Somente duas chances de acertar a capital, após isso o jogo se encerra" )
    print ( "****************************************************************************************************" )
    print("MENU")
    print("**********************")
    print("Digite o numero correspondente do continente")
    print("[1]Americano  [2]Europeu")




if(__name__ == "__main__"):
    jogar()