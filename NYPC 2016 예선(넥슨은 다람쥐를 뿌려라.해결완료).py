import random

n=int(input())

list=[]
daram=0
caram=0
for i in range(n):
    a=input()
    list.append(a)
    daram=daram + list[i].count("D")
    caram=caram + list[i].count("C")

if daram>=caram*2:
    print(n)
    for i in range(n):
        print(list[i])
else:
    want=caram*2-daram
    while want>0:
        for i in range(want):
         rl=random.randint(1,n-1)
         rr=random.randint(1,n-1)
         hmm=list[rl]
         wantlist=[]
         for f in range(0,n):
             wantlist.append(hmm[f])
         if wantlist[rr]=="C":
             new=wantlist[rr]
         else:
             wantlist[rr]="D"
             new="".join(wantlist)
             
         list[rl]=new
         daram=list.count("D")
         caram=list.count("C")
        want=caram*2-daram
    print("\n")
    print(n)
    for i in range(n):
        print(list[i])

    


