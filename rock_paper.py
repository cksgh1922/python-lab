#가위바위보 게임 만들기

import random

#난수를 생성하여 리스트에서 요소를 선택
def computer_choices():
    choices = ['가위','바위','보']
    computer = random.choice(choices)
    
    if user not in choices:
        print("올바른 입력이 아닙니다.")
    else:
        if computer == choices[0]: #컴퓨터가 랜덤으로 가위를 선택했을 때
            if computer == user: # 입력값이 가위일경우
                print(f"컴퓨터의 선택: {computer}\n결과: 무승부입니다!")
            elif user == choices[1]: #입력값이 바위일때
                print(f"컴퓨터의 선택: {computer}\n결과: 당신이 이겼습니다!")
            else:#입력값이 보일때
                print(f"컴퓨터의 선택: {computer}\n결과: 당신이 졌습니다!")
        elif computer == choices[1]: #컴퓨터가 바위를 선택했을 때
            if computer == user: # 입력값이 바위일경우
                print(f"컴퓨터의 선택: {computer}\n결과: 무승부입니다!")
            elif user == choices[0]: #입력값이 가위일때
                print(f"컴퓨터의 선택: {computer}\n결과: 당신이 졌습니다!")
            else:#입력값이 보일때
                print(f"컴퓨터의 선택: {computer}\n결과: 당신이 이겼습니다!")   
        else: #컴퓨터가 보일경우
            if computer == user: # 입력값이 보일경우
                print(f"컴퓨터의 선택: {computer}\n결과: 무승부입니다!")
            elif user == choices[0]: #입력값이 가위일때
                print(f"컴퓨터의 선택: {computer}\n결과: 당신이 이겼습니다!")
            else: #입력값이 바위위
                print(f"컴퓨터의 선택: {computer}\n결과: 당신이 졌습니다!")
            
            

user = input("가위, 바위, 보 중 하나를 선택하세요: ")
computer_choices()