N=int(input())

mydek=[]

gold=0
mana=0
light=0
dark=0
nature=0

for i in range(0,N):
    el=input()
    if el=="gold":
        gold=1
    elif el=="mana":
        mana=1
    elif el=="light":
        light=1
    elif el=="dark":
        dark=1
    elif el=="nature":
        nature=1
    
total=gold+mana+light+dark+nature


if total<=3:
    print("valid")
else:
    print("invalid")