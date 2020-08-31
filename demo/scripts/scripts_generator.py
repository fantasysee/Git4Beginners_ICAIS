fout = './son.txt'
times = 10000000
with open(fout, 'w+') as F:
    for i in range(times):
        F.write('UU Liang is my son.\n')
