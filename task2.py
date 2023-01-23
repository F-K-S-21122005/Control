

f = open('mat_dv.txt', 'r')

lst = [i for i in f]
eight = []
nine = []
ten = []
elevn= []


def winner_in_class(lst):
    summ = []
    for i in lst:
        a = i.split()
        summ.append(int(a[2]) + int(a[3]))
    for i in lst:
        if max(summ) == int(a[2]) + int(a[3]):
            print(a)



for i in lst:
    c = i.split()
    if int(c[2]) == 8:
        eight.append(i)
    elif int(c[2]) == 9:
        nine.append(i)
    elif int(c[2]) == 10:
        ten.append(i)
    else:
        elevn.append(i)
'''
for i in eight:
     summ = 0
     a = i.split()
     winner8 = ''
     if int(a[3]) + int(a[4]) >= summ:
        summ = int(a[3]) + int(a[4])
        winner8 = i

for i in eight:
     summ = 0
     a = i.split()
     winner8 = ''
     if int(a[3]) + int(a[4]) >= summ:
        summ = int(a[3]) + int(a[4])
        winner8 = i
 '''


print(winner_in_class(eight))
print(winner_in_class(nine))
print(winner_in_class(ten))
print(winner_in_class(elevn))

f.close()