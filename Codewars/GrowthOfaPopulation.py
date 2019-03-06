### 1st solution ###
def nb_year(p0, percent, aug, p):
    ret = 0
    while p0 < p:
        ret += 1
        p0 = p0 + p0 * percent * 0.01 + aug
    return ret

### 2nd solution ###
#def nb_year(p0, percent, aug, p):
#   return (0 if p0 >= p else (1 + nb_year(p0 + p0 * percent * 0.01 + aug, percent, aug, p)))
