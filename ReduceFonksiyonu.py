from functools import reduce

reduce(lambda x,y:x + y,[1,2,3,4,5])

########### reduce ile max fonksiyonu  ###########

def maksimum(x,y):
    if (x > y):
        return x
    else:
        return y

reduce(maksimum, [-2,1,100,35,32])
