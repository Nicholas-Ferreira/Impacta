def intercala(t1, t2):
    t3 = []
    for a, b in zip(t1, t2):
        t3.append(a)
        t3.append(b)
        
    return t3
