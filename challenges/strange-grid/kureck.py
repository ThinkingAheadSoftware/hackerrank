def strange_grid(row, col):
    num_sem_unidade = (row - 1)//2 * 10
    unidade = ((col - 1) * 2)
    unidade = unidade + 1 if ((row - 1) % 2 == 1) else unidade

    return (num_sem_unidade + unidade)


def run():
    r, c = map(int, raw_input().split())
    print strange_grid(r, c)

if __name__ == "__main__":
    run()
