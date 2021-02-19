with open('texto.txt') as tudo:
    cc = 1
    listanomes = []
    for c in tudo:
        if str(cc)+'.'+' ' in c:
            cc += 1
            listanomes.append(c)
        with open('nomes.txt', 'w') as nomes:
            for ccc in listanomes:
                nomes.write(str(ccc).strip()+'\n')
