def tabel(lst):
    y = [['Nume', 'Prenume', 'Nota', 'Grupa']]
    rez = []
    a = []
    m = []
    f = []
    lun_max = 0
    for i in lst:
        y.append(i.split())
    for i in y:
        for j in i:
            if len(j) > lun_max:
                lun_max = len(j)
    for i in y:
        for j in i:
            if len(j) < lun_max+1:
                j = list(j)
                j.append((lun_max+1-len(j)) * ' ')
                j = ''.join(j)
                a.append(j)
    for i in range(len(a) - 1):
        rez.append(a[i:i+4])
    for i in rez:
        m = rez[:-2]
    f.append(m[0])
    for i in range(len(m)):
        if (m[i][2].strip()).isnumeric():
            f.append(m[i])
    return f

grupa1 = []
grupa2 = []
s = [i.strip() for i in open('Lista clasei 11D', 'r', encoding='utf-8')]
tab = tabel(lst=s)
tab[0] = ''.join(tab[0])
print(4 * ' ', tab[0], '\n')
for i in range(1, len(tab)):
    tab[i] = ''.join(tab[i])
    if i < 10:
        print(i,') ',tab[i])
    else:
        print(i, ')', tab[i])
media = [int(s[i].split()[2]) for i in range(len(s))]
print(f'Media: {sum(media) / (len(s))}')
for i in range(len(s)):
    j = s[i].split()
    if(j[3][-1]) == '1':
        grupa1.append(s[i])
    else:
        grupa2.append(s[i])
with open('grupa1.txt', 'w') as f:
    for i in grupa1:
        f.write(i)
        f.write('\n')
with open('grupa2.txt', 'w') as f:
    for i in grupa2:
        f.write(i)
        f.write('\n')
