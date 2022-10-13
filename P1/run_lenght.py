def run_lenght(seq):
    '''
    :param sequence of bytes
    :return: the number of concurrences of an element
    '''
    n = len(seq)
    i = 0
    while i < n - 1:
        count = 1
        while (i < n - 1 and seq[i] == seq[i + 1]):
            count += 1
            i += 1
        i += 1

        print(seq[i - 1] + str(count), end=" ")

inp = input('Entra una seqüència: ')
run_lenght(str(inp)+'-') #adding a last character in order to count the last input element







