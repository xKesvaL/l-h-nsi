from random import randint

def matrice(n,p):
    m = [[0 for j in range(n)] for i in range(p)]
    for i in range(p):
        black = True
        for j in range(n):
            if j%20 == 0:
                if black == True:
                    black = False
                else: 
                    black = True
            if black == True:
                m[i][j] = 0
            else:
                m[i][j] = 1
    return m

def fichier(matrx, fichier):
    i = "P1\n# Image exercice\n" + str(len(matrx[0])) + str(len(matrx)) + "\n"
    for l in matrx:
        for n in l:
            i += str(n)
        i += "\n"
    f = open(fichier + ".pbm", "w")
    f.write(i)
    f.close()


def hasard(n, p):
    m = [[0 for j in range(n)] for i in range(p)]
    for i in range(p): 
        for j in range(n):
            m[i][j] = randint(0, 1)
    return m

def chiffre(image, imageCle):
    m = [[0 for j in range(len(image[0]))] for i in range(len(image))]
    for i in range(len(imageCle)):
        for j in range(len(imageCle[0])):
            m[i][j] = image[i][j] ^ imageCle[i][j]
    return m


def lecture(fileName):
    f = open(fileName + ".pbm")
    l = f.read().split("\n")
    f.close()
    m = []
    l = l[3:]
    # ? m.append...

def chiffreOu(image, imageCle):
    m = [[0 for j in range(len(image[0]))] for i in range(len(image))]
    for i in range(len(imageCle)):
        for j in range(len(imageCle[0])):
            m[i][j] = image[i][j] | imageCle[i][j] # Ce chiffrement est non symétrique
    return m