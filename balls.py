import random 
balls =[1,1,1,1,1,1,1,1,1,1,1]
place = random.randint(0,11)
num02 = (random.randint(0,1))*2
balls.insert((place),(num02))
print(balls)


ball_label=[["ball 1","normal"],["ball 2","normal"],["ball 3","normal"],["ball 4","normal"],["ball 5","normal"],["ball 6","normal"],
            ["ball 7","normal"],["ball 8","normal"],["ball 9","normal"],["ball 10","normal"],["ball 11","normal"],["ball 12","normal"]]
#passed through fucntion compare1 as n 

def compare1(n):
    add1 = balls[0]+balls[1]+balls[2]+balls[3]
    add2 = balls[4]+balls[5]+balls[6]+balls[7]
    if add1 == add2:
        for i in range(8,12):
            n[i][1] = "different" # more efficient
            compare2(ball_label)
    elif add

def compare2(n):
    if balls[8]+balls[9]+balls[10] > balls[0]+balls[1]+balls[2]:
        n[8][1], n[9][1], n[10][1] = "heavier","heavier","heavier"
        n[11][1] = "normal"
        if balls[8] > balls[9]:
            n[9][1], n[10][1] = "normal","normal"
        if balls[8] < balls[9]:
            n[8][1], n[10][1] = "normal","normal"
        elif balls[8] == balls[9]:
            n[8][1], n[9][1] = "normal","normal"
            
    elif balls[8]+balls[9]+balls[10] < balls[0]+balls[1]+balls[2]:
        n[8][1], n[9][1], n[10][1] = "lighter","lighter","lighter"
        n[11][1] = "normal"
        if balls[8] > balls[9]:
            n[8][1], n[10][1] = "normal","normal"
        if balls[8] < balls[9]:
            n[9][1], n[10][1] = "normal","normal"
        elif balls[8] == balls[9]:
            n[8][1], n[9][1] = "normal","normal"

    elif balls[8]+balls[9]+balls[10] == balls[0]+balls[1]+balls[2]:
        n[8][1], n[9][1], n[10][1] = "normal","normal","normal"
        if balls[0] > balls[11]:
            n[11][1] = "lighter"
        elif balls[0] < balls[11]:
            n[11][1] = "heavier"
compare1(ball_label) 

for i in ball_label:
    if i[1] == "heavier" or i[1] == "lighter":
        print(i[0],"is",i[1])
















