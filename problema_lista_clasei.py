f = [i.strip() for i in open('C:\\Users\\Statie-5-C100\\Desktop\\prob_lista\\Lista clasei 11D.txt', 'r', encoding='utf-8')]
for i in range(4):
    print(i+1, ')\t',f[i])
media = [int(i.split()[2]) for i in f]
print(f'Media: {sum(media) / len(f)}')