from random import randint

game_num=0
game_list=[]

def set_number():
    global game_num
    game_num = randint(1000, 9999)
    for power in range(3,-1,-1):
        i = (game_num//10**power)%10
        game_list.append(i)
    return game_num



def bc_check(user_num):
    bc = {'bulls':0,'cows':0}
    user_list = []
    bulls = []
    flag = 0
    for power in range(3,-1,-1):
        i = (user_num//10**power)%10
        user_list.append(i)
    for user in range(4):
        for game in range(4):
            if user_list[user]==game_list[game]:
                if user==game:
                    bc['bulls'] +=1
                    bulls.append(user_list[user])
                else:
                    bc['cows'] +=1
                break
                break
    print(bc)
    return(bc['bulls'])
