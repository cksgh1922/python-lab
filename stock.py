#가상 주식거래 플랫폼을 만들어 보자!
#초기 자본금, 주식구매 가격, 구매 주식 개수, 판매주식 가격을 입력받고
#남은자본금과 , 주식 판매시 예상되는 이익 또는 손실을 계산

#주식 구매비용, 남은 자본금, 판매 예상 이익 계산 함수
def stock_profit_left(First_money,Stock_price,Stock_count,Stock_sell):
    left_money = First_money - (Stock_price*Stock_count) #남은 돈 값을 구하기
    total_profit = (Stock_sell*Stock_count)-(Stock_price*Stock_count) #총이익 구하기
    
    if Stock_price > Stock_sell: #구매가격이 판매가격보다 낮은지 확인하는 조건
        return f"구매후 남은 자본금:{left_money:.2f}\n예상 이익: {total_profit:.2f}\n예상되는 손실입니다."
    else: #아닐 경우우
        return f"구매후 남은 자본금:{left_money:.2f}\n예상 이익: {total_profit:.2f}\n예상되는 이익입니다."
    
#정보 입력받기
First_money = float(input("초기 자본금을 입력하세요: "))
Stock_price = float(input("주식 가격을 입력하세요: "))
Stock_count = float(input("구매할 주식의 수를 입력하세요: "))
Stock_sell = float(input("판매할 때의 주식 가격을 입력하세요: "))

#함수 실행 및 출력력
print(stock_profit_left(First_money,Stock_price,Stock_count,Stock_sell))