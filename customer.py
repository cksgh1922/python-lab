#우수고객, 위험고객 판단 함수
def customer():
    #반품률 50%이상 or 가입 개월 수 3개월 이하or 반품 횟수 10회 이상 일 경우 위험고객
    if return_rate >= 50 or customer_month >=30 or buy_amount <= 10000 or return_num >= 10:
        return "위험 고객"
    #위에 조건에 해당 안되며 구매금액 200만원 이상 and 반품률 10% 이하 , 구매횟수 30회 이상, 가입개월 12개월 이상이면 우수고객
    elif buy_amount >= 2000000 and return_rate <= 10 and buy_count >= 30 and customer_month >= 12:
        return "우수 고객"
    #위 조건에 모두 부합 할 경우 일반고객
    else:
        return "일반 고객"

# 구매금액,반품횟수,구매횟수,가입개월수 입력받기
buy_amount = int(input("총 구매 금액 : "))
return_num = int(input("총 반품 횟수 : "))
buy_count = int(input("총 구매 횟수 : "))
customer_month = int(input("가입 개월 수 : "))


# 구매횟수가 0인경우 오류 출력
if buy_count == 0:
    print('''
오류 : 구매 횟수가 0입니다. 반품률을 계산할 수 없습니다.
프로그램을 종료합니다.''')

# 아닐경우 반품횟수가 구매횟수보다 많은지 체크
elif return_num > buy_count:
    print('''
오류 : 반품 횟수가 구매 횟수보다 많을 수 없습니다.
프로그램을 종료합니다.''')

#아닐 경우 반품률을 계산하고 고객판단 함수 호출하여 리턴받은 결과값을 출력
else:
    #반품률 계산
    return_rate = (return_num/buy_count) * 100
    #고객판단 함수 호출
    customer_rank = customer()
    #리턴 값 출력
    print(f'''
반품률 : {return_rate:.1f}%
결과 : {customer_rank}''')