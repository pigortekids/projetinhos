def acabou(campo):
    retorno = 0
    for i in range(3):
        if sum(campo[i]) in [3, -3]:
            retorno = sum(campo[i])
        if campo[0][i] + campo[1][i] + campo[2][i] in [3, -3]:
            retorno = campo[0][i] + campo[1][i] + campo[2][i]
    if campo[0][0] + campo[1][1] + campo[2][2] in [3, -3]:
        retorno = campo[0][0] + campo[1][1] + campo[2][2]
    if campo[2][0] + campo[1][1] + campo[0][2] in [3, -3]:
        retorno = campo[2][0] + campo[1][1] + campo[0][2]
    if retorno != 0:
        retorno = int(retorno / 3)
    return retorno

campo = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
jogador = 1
qnt_jogadas = 0

while acabou(campo) == 0 and qnt_jogadas != 9:
    jogada_valida = False
    while not jogada_valida:
        y = int(input('digite a linha a jogar: '))
        x = int(input('digite a coluna a jogar: '))
        if campo[x][y] != 0:
            print('campo inválido')
        else:
            jogada_valida = True

    campo[x][y] = jogador
    jogador = jogador * (-1)
    qnt_jogadas += 1

    for i in range(3):
        print(campo[i])

if qnt_jogadas == 9:
    print('deu velha')
elif acabou(campo) == 1:
    print('jogador 1 ganhou')
elif acabou(campo) == -1:
    print('jogador 2 ganhou')