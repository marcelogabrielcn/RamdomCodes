from random import shuffle, randrange


def make_maze(w=16, h=8):
    """ Cria um labirinto aleatório e o desenha na tela em ASCII Art
        Parâmetros:
            w - o número de colunas do labirinto (padrão: 16)
            h - o número de linhas do labirinto (padrão: 8)
    """

    # Matriz de células visitadas (0 = não visitada, 1 = visitada)
    # Delimitada por uma linha/coluna com todos visitados (fronteira)
    # Sofre overflow nos índices negativos
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]

    # Linhas contendo as células e linhas entre-células
    # Inicia-se com todas as células disjuntas (paredes entre todas elas)
    ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    hor = [["+--"] * w + ['+'] for _ in range(h + 1)]

    def walk(x, y):
        """ Visita uma célula e todas as suas células adjacentes,
            em profundidade, unindo-as ao labirinto corrente.
        """
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            # Remove a parede entre células
            if xx == x: hor[max(y, yy)][x] = "+  "
            if yy == y: ver[y][max(x, xx)] = "   "
            walk(xx, yy)

    # Visita a célula de origem
    walk(randrange(w), randrange(h))

    # Imprime o resultado na tela
    for (a, b) in zip(hor, ver):
        print(''.join(a + ['\n'] + b))


make_maze()
