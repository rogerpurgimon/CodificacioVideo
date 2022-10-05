def run_lenght(seq):
    '''
    :param seqüència de bytes
    :return: el nombre de 1's i 0's
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
run_lenght(str(inp)+'-') #afegeixo un caràcter per a que es conti l'últim element







