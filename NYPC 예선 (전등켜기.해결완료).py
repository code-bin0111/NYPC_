
x, y =input().split()

x=int(x)
y=int(y)

object=[]
outer=[]
for i in range(y+2):
    outer.append("0")
#mirror: 거울의 좌표
#one: 한 줄

object.append(outer)

i=0
while i <y:
    multi=[]
    multi.append("0")
    one=input()
    f=0
    while f <x:
        multi.append(one[f])
        f=f+1    
    multi.append("0")
    object.append(multi)
    i=i+1
object.append(outer)



#npx:현재 x좌표 진행위치
#npy:현재 y좌표 진행위치
#np:현재 실행 진행 횟수
#n[np]=[npx,npy]

#상황예시(x=5,y=4)
#0000000:object[0]6
#0..O./0:object[1]5
#0\....0:object[2]4
#0.....0:object[3]3
#0.../.0:object[4]2
#0000000:object[5]1
#0123456

#n[np][0]:x
#n[np][1]:y

npy=y
where=y
n=100
while n==100:
    k=2
    np=0
    n=[]
    npx=1

    if object[npy][npx]=="O":
        print("L",y-where+1)
        k=1
        break
    
    n.append([npx,npy])
    npx=npx+1

    if object[npy][npx]=="O":
        print("L",y-where+1)
        k=1
        break
    np=np+1
    n.append([npx,npy])
    while object[npy][npx]!="0":
        if object[npy][npx]=="O":
            print("L",y-where+1)
            k=1
            break
        elif n[np][0]-n[np-1][0]<0: #왼쪽으로 이동함
            if object[npy][npx-1]=="/": #45도 거울 봄
                npy=npy-1
            elif object[npy][npx-1]=="O"or"0"or".":
                npx=npx-1
            else:              #135도 거울 봄
                npy=npy+1 
            n.append([npx,npy])           
            np=np+1

        elif n[np][0]-n[np-1][0]>0: #오른쪽으로 이동함
            if object[npy][npx+1]=="/": #45도 거울 봄
                npy=npy+1
            elif object[npy][npx+1]=="O"or"0"or".":
                npx=npx+1
            else:              #135도 거울 봄
                npy=npy-1    
            n.append([npx,npy])           
            np=np+1

        elif n[np][1]-n[np-1][1]<0: #아래쪽으로 이동함
            if object[npy-1][npx]=="/": #45도 거울 봄
                npx=npx-1
            elif object[npy-1][npx]=="O"or"0"or".":
                npy=npy-1
            else:              #135도 거울 봄
                npx=npx+1    
            n.append([npx,npy])           
            np=np+1

        elif n[np][1]-n[np+1][1]>0: #위쪽으로 이동함
            if object[npy+1][npx]=="/": #45도 거울 봄
                npx=npx+1
            elif object[npy+1][npx]=="O"or"0"or".":
                npy=npy+1
            else:              #135도 거울 봄
                npx=npx-1    
            n.append([npx,npy])           
            np=np+1
    where=where-1
    npy=npy-1
    n=100
    if k==1: 
        break
    

