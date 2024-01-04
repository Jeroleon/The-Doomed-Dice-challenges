import random
dieA=[1,2,3,4,5,6]
dieB=[1,2,3,4,5,6]
die=[1,2,3,4,5,6]

def dice():
    dieA1=random.choice(die)
    dieB1=random.choice(die)
    sum=dieA1+dieB1 
    print(f'({dieA1},{dieB1})')
    print(sum)
dice()

def comb(die):
    length=len(die)
    print("Total combinations :",length*length)
comb(die)

def dis_comb(die):
    dis_arr=[[0]*len(die) for _ in range(len(die))]
    for diea in die:
        for dieb in die:
            dis_arr[diea-1][dieb-1]=diea,dieb
    for i in dis_arr:
        print(i)
    return dis_arr
print("All possible combinations")
dis_comb(die) 


def dis_poss_comb(dieA,dieB):
    comb_dis=[[0]*len(die) for _ in range(len(die))]
    for diea in dieA:
        for dieb in dieB:
            total=diea+dieb
            comb_dis[diea-1][dieb-1]=total

    for row in comb_dis:
        print(row)
print("sum distribution")
dis_poss_comb(dieA,dieB)

def prob(die):
    for i in range(2,13):
        count=0
        for j in die:
            for k in die:
                if j+k==i:
                    count+=1
        pro=count/36
        print(f" p(sum={i})={1/36}={pro:.3f}")
print("sum probability")
prob(die)

    
    




















        

 






        
