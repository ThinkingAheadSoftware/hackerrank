# Enter your code here. Read input from STDIN. Print output to STDOUT
def maxsubarray(lista):
    current_sum = 0
    best_sum = 0
    positive_sum = 0
    # used when the list contains only negative numbers
    greater_value = -1000
    # Only necessary if I want to know the list of greater sequence
    current_idx = -1
    best_start_idx = -1
    best_end_idx = -1

    for i in xrange(len(lista)):
        val = current_sum + lista[i]

        # find the greater value in sequence
        if (greater_value < lista[i]):
            greater_value = lista[i]
        if val > 0:
            if current_sum == 0:
                current_idx = i
            current_sum = val
        else:
            current_sum = 0

        # get the sum for positive numbers
        if (lista[i] > 0):
            positive_sum += lista[i]

        if (current_sum > best_sum):
            best_sum = current_sum
            best_start_idx = current_idx
            best_end_idx = i
    # if dont have positive numbers, show the highest integer.
    if (best_sum == 0):
        best_sum = greater_value
        positive_sum = greater_value

    return best_sum, positive_sum


def main():
    n_cases = int(raw_input())

    for i in xrange(n_cases):
        lista_size = int(raw_input())
        lista_i = map(int, raw_input().split())
        max_cont_sum, max_sum = maxsubarray(lista_i)
        print "{0} {1}".format(max_cont_sum, max_sum)

if __name__ == "__main__":
    main()
