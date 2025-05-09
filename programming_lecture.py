#별다방 고객의 주문을 받아 음료 가격과 혜택을 계산하는 프로그램을 작성

#음료 선택에 따라 가격을 추가하는 함수
def beverage_selection():
    price = 0
    if beverage == "coffee":
        price += 3000
    elif beverage == "latte":
        price += 4000
    else:
        price += 3500
    return price

#사이즈 선택에 따라 가격을 추가하는 함수
def size_selection():
    price = 0
    if size == "large":
        price += 1000
    elif size == "medium":
        price += 500
    return price

#멤버십 여부에 따라 가격 할인 적용 혹은 미적용
def membership_dis():
    price = 0
    global total_price
    if membership == "yes":
        price = int(total_price*0.1)
        total_price -= price
        price = "-"+ str(price)+"원"
    else:
        price = "없음"
    return price

#음료,크기,멤버십 여부를 입력 받습니다.
beverage = input("음료를 선택하세요 (coffee/latte/juice) : ")
size = input("크기를 선택하세요 (small/medium/large) : ")
membership = input("멤버십이신가요? (yes/no) : ")

#음료 선택 값을 beverage_price에 저장
beverage_price = beverage_selection()

#사이즈 선택값을 size_price에 저장
size_price = size_selection()

#total_price는 음료 + 사이즈 가격
total_price = (beverage_price + size_price)

#멤버십 적용 여부 함수를 호출하여 결과 값을 discount에 저장
discount_price = membership_dis()

#모든 값 출력
print(f'''
기본 가격 : {beverage_price}원
크기 추가 요금 : {size_price}원
할인 적용 : {discount_price}
최종 결제 금액 : {int(total_price)}원''')
#만약 멤버쉽이면서 , 커피/라떼 이고, 사이즈가 라지일 경우 무료 샷 제공 출력
if size == "large" and membership == "yes":
        if beverage == "coffee" or beverage == "latte":
            print("무료 샷이 제공됩니다!")