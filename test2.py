a = int(input())
if a < 0:
    print("입력 값 오류")
else:
    if a >= 80:
        print("합격")
    else:
        print("불합격")
        if a >= 90:
            if a == 100:
                print("만점 축하")
            elif a >= 95:
                print("우수상")
            else: 
                print("A")
        elif a >= 80:
            print("B")
        elif a >= 70:
            print("C")
        else:
            print("D")

