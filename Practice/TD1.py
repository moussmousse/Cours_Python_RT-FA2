
#Exercice 1:

def impaire(n):
    """ Return tout les nombres impaires de 0 à n. """
    res = []
    for i in range (1,n,2):
        res.append(i)
    return res

def fibo(n):
    """ Return les n premiers termes de fibonacci."""
    a, b = 0, 1
    res = []
    for i in range (n):
        res.append(b)
        a, b = b, a+b
    return res

def fibo2(n):
    """ Return les n premiers termes de fibonacci multiple de 7. """
    a, b = 0, 1
    res = []
    for i in range (n):
        if b%7 == 0:
            res.append(b)
        a, b = b, a+b
    return res

#Exercice 2:

def diviseurs(n):
    """ Return la liste des diviseurs de n. """
    res = []
    stop = n+1 // 2
    for i in range(1,stop):
        if n%i == 0:
            res.append(i)
    res.append(n)
    return res

def is_first(n):
    """ Return ?n premier"""
    return (len(diviseurs(n))==2)

def list_first(n):
    """ Return la liste des nombres premiers de 0 à n"""
    res = []
    for i in range(n):
        if is_first(i):
            res.append(i)
    return res

#Exercice 3

def perfect(n,res = [],ind = 1):
    """
    Return la liste des n premiers nombres parfaits.
    Attention au test : le 5eme nombre est supérieur a 33 millions.
    """
    if len(res)>=n:
        return res
    sm = 0
    for i in diviseurs(ind):
        sm+=i
    if sm == ind*2:
        res.append(ind)
    ind+=1
    return perfect(n,res,ind)


#Exercice 4

def list_first_eratho(n):

    return
