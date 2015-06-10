def strange_grid(row, col):
    num_sem_unidade = (row - 1)//2 * 10
    unidade = ((col - 1) * 2)
    if ((row - 1) % 2 == 1):
        unidade += 1

    return (num_sem_unidade + unidade)


def main():
    r, c = map(int, raw_input().split())
    print strange_grid(r, c)

if __name__ == "__main__":
    main()
