import itertools
import math
import random

#deklarasi kota kota dengan jarak yang dimiliki
ab = 6 ; bc = 3 ; cf = 10 ; ad = 7 ; be = 4 ; de = 1 ; ef = 4 ; dg = 4 ; ea = 4 ; ga = 2
ai = 1 ; fi = 8

#masukkan kota ke dalam array
kota = [ab,bc,cf,ad,be,de,ef,dg,ea,ga,ai,fi]

#hitung panjang kota dan masukkan ke dalam array tour
n=len(kota)
tour = random.sample(range(n),n)

def jarak(x,y):
    #menghitung jarak antara dua kota
    return math.sqrt(x+y)

def totaljarak(tour):
    #menghitung total jarak antara kota satu dengan banyak kota lainnya
    d=0
    for i in range(1,len(tour)):
        x = kota[tour[i-1]]
        y = kota[tour[i]]
        d=d+jarak(x,y)
        print("Jarak Sementara : ","Kota-",i-1,"Ke Kota",i,"adalah",d)
    x1=kota[tour[len(tour)-1]]
    y1=kota[tour[0]]
    d=d+jarak(x1,y1)
    return d

semuakemungkinan = list(itertools.permutations(tour))
lbest = 1000000
ibest = tour

for i in range (len(semuakemungkinan)):
    l= totaljarak(semuakemungkinan[i])
    if l<lbest:
        lbest = l
        ibest = i
    
print(ibest)
print(semuakemungkinan[ibest])