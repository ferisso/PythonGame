
def colocar_missionario(margen1, margen2, barco, barco_switch):
    """
    coloca missionario no barco

    :param margen1: lista com missionarios ou canibais
    :param margen2: lista com missionarios ou canibais
    :param barco: lista com missionarios ou canibais
    :param barco_switch: valor boolean True = Esquerda, False = Direita
    :return: none
    """
    if barco_switch is True:
        if margen1.count('missionario') == 0:
            print('Nao ha missionarios na margem')
        else:
            margen1.remove('missionario')
            barco.append('missionario')
    if barco_switch is False:
        if margen2.count('missionario') == 0:
            print('Nao ha missionarios na margem')
        else:
            margen2.remove('missionario')
            barco.append('missionario')


def colocar_canibal(margen1, margen2, barco, barco_switch):
    """
    Coloca canibal no barco

    :param margen1: lista com missionarios ou canibais
    :param margen2: lista com missionarios ou canibais
    :param barco: lista com missionarios ou canibais
    :param barco_switch: valor boolean True = Esquerda, False = Direita
    :return: none
    """
    if barco_switch is True:
        if margen1.count('canibal') == 0:
            print('Nao ha canibais na margem')
        else:
            margen1.remove('canibal')
            barco.append('canibal')
    if barco_switch is False:
        if margen2.count('canibal') == 0:
            print('Nao ha canibais na margem')
        else:
            margen2.remove('canibal')
            barco.append('canibal')


def retirar_canibal(margen1, margen2, barco, barco_switch):
    """
    retira canibal do barco

    :param margen1: lista com missionarios ou canibais
    :param margen2: lista com missionarios ou canibais
    :param barco: lista com missionarios ou canibais
    :param barco_switch: valor boolean True = Esquerda, False = Direita
    :return: none
    """
    if barco_switch is True:
        if barco.count('canibal') == 0:
            print('Nao ha canibais no barco')
        else:
            barco.remove('canibal')
            margen1.append('canibal')
    if barco_switch is False:
        if barco.count('canibal') == 0:
            print('Nao ha canibais no barco')
        else:
            barco.remove('canibal')
            margen2.append('canibal')


def retirar_missionario(margen1, margen2, barco, barco_switch):
    """
    retira missionario do barco

    :param margen1: lista com missionarios ou canibais
    :param margen2: lista com missionarios ou canibais
    :param barco: lista com missionarios ou canibais
    :param barco_switch: valor boolean True = Esquerda, False = Direita
    :return: none
    """
    if barco_switch is True:
        if barco.count('missionario') == 0:
            print('Nao ha missionarios no barco')
        else:
            barco.remove('missionario')
            margen1.append('missionario')
    if barco_switch is False:
        if barco.count('missionario') == 0:
            print('Nao ha missionarios no barco')
        else:
            barco.remove('missionario')
            margen2.append('missionario')


def messages(margen1, margen2, barco, barco_switch):
    """
    Checa o estoque e caso haja estoque faz a venda

    :param margen1: lista com missionarios ou canibais
    :param margen2: lista com missionarios ou canibais
    :param barco: lista com missionarios ou canibais
    :param barco_switch: valor boolean True = Esquerda, False = Direita
    :return: none
    """
    if barco_switch is True:
        print('Barco na margem a esquerda')
    else:
        print('Barco na margem a direita')
    print(f'Margem a esquerda {margen1}')
    print(f'Margem a direita {margen2}')
    print(f'No barco {barco}')


def count(margen1, margen2, barco, barco_switch):
    """
    Checa o estoque e caso haja estoque faz a venda

    :param margen1: lista com missionarios ou canibais
    :param margen2: lista com missionarios ou canibais
    :param barco: lista com missionarios ou canibais
    :param barco_switch: valor boolean True = Esquerda, False = Direita
    :return: int 1
    """
    canibais_m1 = margen1.count('canibal')
    missionario_m1 = margen1.count('missionario')
    canibais_m2 = margen2.count('canibais')
    missionario_m2 = margen2.count('missionario')
    if barco_switch is True:
        canibais_m1 = canibais_m1 + barco.count('canibal')
        missionario_m1 = missionario_m1 + barco.count('missionario')
    else:
        canibais_m2 = canibais_m2 + barco.count('canibal')
        missionario_m2 = missionario_m2 + barco.count('missionario')
    if canibais_m1 > missionario_m1:
        if missionario_m1 == 0:
            pass
        else:
            return 1
    if canibais_m2 > missionario_m2:
        if missionario_m2 == 0:
            pass
        else:
            return 1


def win(margen2):
    """
    funcao de vitoria

    :param margen2: lista com missioraios ou canibais
    :return: Retorna um valor Boolean
    """
    if len(margen2) == 6:
        return True


def menu():
    """
    menu com as opcoes a serem escolhidas

    :return: none
    """
    print(35 * '*')
    print('1 - Colocar um canibal no barco')
    print('2 - Colocar um missionario no barco')
    print('3 - Retirar um canibal do barco')
    print('4 - Retirar um missionário do barco')
    print('5 - Mover o barco')
    print('0 - Para sair')
    print(35 * '*')


def main():
    """
    Programa principal

    :return: none
    """
    margen1 = ['missionario', 'missionario',
               'missionario', 'canibal', 'canibal', 'canibal']
    margen2 = []
    barco = []
    barco_switch = True
    while True:
        menu()
        messages(margen1, margen2, barco, barco_switch)
        count(margen1, margen2, barco, barco_switch)
        if count(margen1, margen2, barco, barco_switch) == 1:
            print('Voce perdeu!!!!')
            print('Numero de Canibais nao pode ser maior doq de missionarios')
            break
        if win(margen2) is True:
            print(f'Meus parabens voce resolveu o dilema')
            break
        op = int(input('Selecione uma opcao: '))
        if op == 1:
            colocar_canibal(margen1, margen2, barco, barco_switch)
        elif op == 2:
            colocar_missionario(margen1, margen2, barco, barco_switch)
        elif op == 3:
            retirar_canibal(margen1, margen2, barco, barco_switch)
        elif op == 4:
            retirar_missionario(margen1, margen2, barco, barco_switch)
        elif op == 5:
            if len(barco) > 2 or len(barco) == 0:
                print('O barco nao pode passar sozinho ou com mais de dois')
            else:
                # Transforma barco_switch em True or False
                barco_switch = not barco_switch
        elif op == 0:
            break


if __name__ == '__main__':
    main()
