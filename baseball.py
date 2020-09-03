import os
import random

def clear():
    os.system('cls')


def line():
    for _ in range(1,11):
        print('=',end=' ')

def printinfo():
    a=4
    while a!=-1:
        clear()
        print('--------------------------미니 야구 게임 설명---------------------------')
        print('본 게임은 야구의 룰을 일부 적용한 "미니 야구 게임" 입니다.')
        print('1. 게임은 총 3회로 이루어져 있습니다.')
        print('2.플레이어는 스윙 혹은 공을 거를 수 있습니다.')
        a=int(input('메인 메뉴로 돌아가기(-1):'))
    clear()

def print_score(score1,score2,ining):
    print("\n┌───────────────────────────────────────┐\n")
    print("│    1회 2회 3회 4회 5회 6회 7회 8회 9회│\n")
    print("│    %d   %d   %d   %d   %d   %d   %d    %d   %d│\n" %(score1[0],score1[1],score1[2],score1[3],score1[4],score1[5],score1[6],score1[7],score1[8]))
    print("│    1회 2회 3회 4회 5회 6회 7회 8회 9회│\n")
    print("│    %d   %d   %d   %d   %d   %d   %d    %d   %d│\n" %(score2[0],score2[1],score2[2],score2[3],score2[4],score2[5],score2[6],score2[7],score2[8]))
    print("└───────────────────────────────────────┘\n")

def swing_result():
    result=100
    ball=random.randrange(0,101)
    if ball>=0 and ball<14:#1루타
        result=1
    elif ball>=14 and ball<21:#2루타
        result=2
    elif 21 <= ball and ball < 26: #3루타
        result = 3
    elif 26<=ball and ball <29:#홈런
        result=4
    elif 29 <= ball and ball < 62:#플라이 아웃
        result = 5
    elif 62 <= ball and ball < 100 :#스트라이크
        result = 6
    return result

def pass_result():
    pass_result
    ball=random.randrange(0,101)
    if 0 <= ball and ball < 60:#볼
        pass_result = 1
    else:#스트라이크
        pass_result = 2
    return pass_result

def print_count(ball,strike,out):
    if ball==0:
        print("B ○○○\n")
    elif ball==1:
        print("B ●○○\n")
    elif ball==2:
        print("B ●●○\n")
    elif ball==3:
        print("B ●●●\n")
    if strike==0:
        print("S ○○\n")
    elif strike==1:
        print("S ●○\n")
    elif strike==2:
    	print("S ●●\n")
    if out==0:
    	print("O ○○\n")
    elif out==1:
    	print("O ●○\n")
    elif out==2:
    	print("O ●●\n")

def print_base(base1, base2, base3):
    if base1 == 0 and base2 == 0 and base3 == 0:
        print("               ◇            \n")
        print("            ↙   ↖            \n")
        print("         ↙        ↖           \n")
        print("       ↙            ↖           \n")
        print("      ◇               ◇         \n")
        print("       ↘             ↗         \n")
        print("         ↘         ↗         \n")
        print("           ↘    ↗           \n")
        print("              ◇            \n")
    if base1 == 1 and base2 == 0 and base3 == 0:
        print("               ◇            \n")
        print("            ↙   ↖            \n")
        print("         ↙        ↖           \n")
        print("       ↙            ↖           \n")
        print("      ◇               ◆         \n")
        print("       ↘             ↗         \n")
        print("         ↘         ↗         \n")
        print("           ↘    ↗           \n")
        print("              ◇            \n")
    if base1 == 1 and base2 == 1 and base3 == 0:
        print("               ◆            \n")
        print("            ↙   ↖            \n")
        print("         ↙        ↖           \n")
        print("       ↙            ↖           \n")
        print("      ◇               ◆         \n")
        print("       ↘             ↗         \n")
        print("         ↘         ↗         \n")
        print("           ↘    ↗           \n")
        print("              ◇            \n")
    if base1 == 1 and base2 == 1 and base3 == 1:
        print("               ◆            \n")
        print("            ↙   ↖            \n")
        print("         ↙        ↖           \n")
        print("       ↙            ↖           \n")
        print("      ◆               ◆         \n")
        print("       ↘             ↗         \n")
        print("         ↘         ↗         \n")
        print("           ↘    ↗           \n")
        print("              ◇            \n")
    if (base1 == 1 and base2 == 0 and base3 == 1):
        print("               ◇            \n")
        print("            ↙   ↖            \n")
        print("         ↙        ↖           \n")
        print("       ↙            ↖           \n")
        print("      ◆               ◆         \n")
        print("       ↘             ↗         \n")
        print("         ↘         ↗         \n")
        print("           ↘    ↗           \n")
        print("              ◇            \n")
    if (base1 == 0 and base2 == 1 and base3 == 0 ):
        print("               ◆            \n")
        print("            ↙   ↖            \n")
        print("         ↙        ↖           \n")
        print("       ↙            ↖           \n")
        print("      ◇               ◇         \n")
        print("       ↘             ↗         \n")
        print("         ↘         ↗         \n")
        print("           ↘    ↗           \n")
        print("              ◇            \n")
    if (base1 == 0 and base2 == 1 and base3 == 1 ):
        print("               ◆            \n")
        print("            ↙   ↖            \n")
        print("         ↙        ↖           \n")
        print("       ↙            ↖           \n")
        print("      ◆               ◇         \n")
        print("       ↘             ↗         \n")
        print("         ↘         ↗         \n")
        print("           ↘    ↗           \n")
        print("              ◇            \n")
    if (base1 == 0 and base2 == 0 and base3 == 1 ):
        print("               ◇            \n")
        print("            ↙   ↖            \n")
        print("         ↙        ↖           \n")
        print("       ↙            ↖           \n")
        print("      ◆               ◇         \n")
        print("       ↘             ↗         \n")
        print("         ↘         ↗         \n")
        print("           ↘    ↗           \n")
        print("              ◇            \n")


def startgame():
    clear()
    line()
    print('\n게임을 시작 합니다\n')
    line()
    ining=1
    score1=[0,0,0,0,0,0,0,0,0]
    score2=[0,0,0,0,0,0,0,0,0]
    player1=player()
    player2=player()
    while(ining<10):
        score1[ining-1]=player1.startining(ining,score1,score2)
        score2[ining-1]=player2.startining(ining,score1,score2)
    if sum(score1)>sum(score2):
        print("player1 승리")
    elif sum(score1)==sum(score2):
        print("동점")
    else:
        print("player2 승리")

class player:
    def startining(self,ining,score1,score2):
        base1,base2,base3,score,strike,ball,out=0,0,0,0,0,0,0
        while (out <= 2):
            x = 0
            while (x != 1 and x != 2):
                line()
                print("\n%d회" %ining)
                print_score(score1,score2,ining)
                print_base(base1,base2,base3)
                print_count(ball, strike, out)
                print("\n1. 스윙,    2.거르기\n")
                x=int(input("입력:"))
                if x == 1:#스윙시
                    swing = swing_result()
                    clear()
                    if swing == 1:#안타
                        clear()
                        print("안타 입니다.\n")
                        strike = 0
                        ball = 0
                        if base1 == 0:
                            base1 = 1
                        elif base1 == 1:
                            if base2 == 0:
                                base2 = 1
                            elif base2 == 1:
                                if base3 == 0:
                                    base3 = 1
                                elif base3 == 1:
                                    score+=1
                                    print("홈인! 점수를 한점 올립니다.\n")
                    if swing == 6:#스트라이크
                        clear()
                        print("스트라이크 입니다.\n")
                        strike+=1
                    if swing == 5:#플라이 아웃
                        clear()
                        print("플라이 아웃입니다.\n")
                        strike = 0#볼카운트 초기화
                        ball = 0
                        out+=1#아웃 카운트 1 추가
                    if swing == 4:#홈런
                        clear()
                        print("홈런입니다.\n")
                        strike = 0#볼카운트 초기화
                        ball = 0
                        if base3 == 1:#3루 주자 있으면
                            score+=1#1점 추가
                            print("3루 주자 홈인! 점수를 한점 올립니다.\n")
                            base3 = 0
                        if base2 == 1:#2루 주자 있으면
                            score+=1#1점 추가
                            print("2루 주자 홈인! 점수를 한점 올립니다.\n")
                            base2 = 0
                        if base1 == 1:#1루 ㅓ주자 있으면
                            score+=1#1점 추가
                            print("1루 주자 홈인! 점수를 한점 올립니다.\n")
                            base1 = 0
                        score+=1#타자가 1점 올림
                        print("타자 홈인! 점수를 한점 올립니다.\n")
                    if swing == 3:#3루타
                        clear()
                        print("3루타입니다.\n")
                        strike = 0#볼카운트 초기화
                        ball = 0
                        if base2 == 1:#2루에 주자 있으면
                            score+=1#1점 추가
                            print("2루 주자 홈인! 점수를 한점 올립니다.\n")
                            base2 = 0
                        if base3 == 1: #3루에 주자 있으면
                            score+=1
                            print("3루 주자 홈인! 점수를 한점 올립니다.\n")
                            base3 = 0
                        if base1 == 1:#1루에 주자있으면
                            score+=1#1점 추가
                            print("1루 주자 홈인! 점수를 한점 올립니다.\n")
                            base1 = 0
                        base3 = 1#3루 주자 추가
                    if swing == 2:#2루타
                        clear()
                        print("2루타 입니다.\n")
                        strike = 0#볼카운트 초기화
                        ball = 0
                        if base3 == 1:#3루 주자 있으면
                            score+=1#1점 추가
                            print("3루 주자 홈인! 점수를 한점 올립니다.\n")
                            base3 = 0
                        if base2 == 1:#2루 주자 있으면
                            score+=1#점수 추가
                            print("2루 주자 홈인! 점수를 한점 올립니다.\n")
                            base2 = 0
                        if base1 == 1:#1루 주자 있으면
                            base1 = 0
                            base3 = 1#3루로 이동
                        base2 = 1#2루 주자 추가
                elif x == 2:#거르기
                    pass0 = pass_result()
                    clear()
                    if pass0 == 1:#볼
                        print("볼입니다.\n")
                        ball+=1#볼 추가
                    if pass0 == 2:#스트라이크
                        print("스트라이크 입니다.\n")
                        strike+=1#스트라이크 추가
                else:#잘못 입력
                    clear()
                    print("숫자를 다시 입력하세요.\n")
                if ball == 4:#볼넷
                    print("볼넷 입니다.\n")
                    strike = 0#/볼카운트 초기화
                    ball = 0
                    if base1 == 0:#안타와 비슷
                        base1 = 1
                    elif base1 == 1:
                        if base2==0:
                            base2 = 1
                        elif base2 == 1:
                            if base3 == 0:
                                base3 = 1
                            elif base3 == 1:
                                score+=1
                                print("홈인! 점수를 한점 올립니다.\n")
                if strike == 3:#삼진 아웃
                    print("스트라이크 아웃!!\n")
                    strike = 0#볼카운트 초기화
                    ball = 0
                    out+=1#아웃 카운트 추가
        print("이닝이 종료되었습니다.\n")
        return score




def print_menu():
    menu=0
    while menu !=1 and menu !=2 and menu !=3:
        line()
        print('\n1.게임 시작')
        print('2.게임 설명')
        print('3.게임 종료')
        line()
        print('\n선택하고자 하는 메뉴를 선택해주세요.')
        menu=int(input())
        if menu == 1:
            clear()
            startgame()
        elif menu==2:
            printinfo()
            menu=100
        elif menu==3:
            print('프로그램 종료')
        else:
            print('다시 입력 하세요.')

print_menu()