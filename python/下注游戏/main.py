#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
                赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束

"""
from random import randint
while True:
    try:
        money = int(input('请输入您要充值的金额：'))
        break
    except ValueError:
        print(" 输入错误，请重新输入准确数据  ")

def playgame (money):
    while money > 0:
        print('你的账户还有：', money)
        # xiazhu = int (input('请下注：'))
        while True:
            try:

                xiazhu = int(input('请下注：'))
                if xiazhu > 0 and money > 0 and money >= xiazhu :
                    break
                else :
                    xiazhu = int(input('余额不足，请重新下注：'))
                    break
            except ValueError:
                print(" 输入错误，请重新输入准确数据  ")


        i = randint(1, 6) + randint(1, 6)

        print('玩家摇出了:%d点' % i)
        keep_go_on = 0
        if i == 7 or i == 11:
            money = money + xiazhu
            print('玩家胜')
        elif i == 2 or i == 3 or i == 12:
            print('庄家胜')
            money = money - xiazhu
        else:
            keep_go_on = 1
        while keep_go_on:
            p = input('请按任继建继续')
            j = randint(1, 6) + randint(1, 6)
            print('玩家摇出了:%d点' % j)
            if j == 7:
                print('庄家胜')
                money = money - xiazhu
                keep_go_on = 0
            elif j == i:
                print('玩家胜')
                money = money + xiazhu
                keep_go_on = 0
    print('您已经破产了!')
    return money

playgame(money)









