

def boostFound(vl, vs, t):
    a = (vl - vs)//t

    return f'Ускорение равно {a}'

@decorator
def wayFound(vs, t):
    s = vs + (boostFound * t**2)//2


print(boostFound(15, 10, 5))
print(wayFound(15,5))