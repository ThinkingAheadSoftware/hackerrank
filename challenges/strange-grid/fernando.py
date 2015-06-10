def strange_grid(row, col):
    dezena, unidade = ((row//2 * 10 - 10), (col-1) * 2 + 1) if (row % 2 == 0) else ((row//2 * 10 - 5), (col-1)*2)
    return dezena+unidade


def main():
    r, c = map(int, raw_input().split())
    print strange_grid(r, c)

if __name__ == "__main__":
    main()
