def printMove(fr, to):
    print("move " + str(fr) + ' to ' + str(to))


def Towers(n, fr, to, help):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr=fr, to=help, help=to)
        Towers(1, fr=fr, to=to, help=help)
        Towers(n-1, fr=help, to=to, help=fr)


if __name__ == "__main__":
    Towers(5, 'A', 'B', 'C')
