cont_for_out = []

with open('temporary/in.txt') as inp:
    cont = inp.read().splitlines()
    for i in range(1, len(cont) + 1):
        #print('i = ', i)
        i *= -1
        print(cont[i])
        cont_for_out.append(cont[i])

with open('temporary/out.txt', 'w') as out:
    out.write('\n'.join(cont_for_out))






