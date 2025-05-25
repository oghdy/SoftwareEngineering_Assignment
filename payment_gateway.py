
class PaymentGateway:
    def request_payment(self, amount):
        print(f"외부 결제 시스템에서 {amount}원 결제 요청 처리 중...")
        # 실제 결제 로직 대신 간단히 True 반환
        return True