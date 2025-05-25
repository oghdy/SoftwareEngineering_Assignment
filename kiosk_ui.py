# kiosk_ui.py (메인 실행 파일)
from menu_manager import MenuManager
from order_processor import OrderProcessor
from payment_gateway import PaymentGateway
from beverage_maker import BeverageMaker

class KioskUI:
    def __init__(self, menu_manager, order_processor):
        self.menu_manager = menu_manager
        self.order_processor = order_processor

    def start(self):
        print("환영합니다! 카페 키오스크입니다.")
        while True:
            print("\n--- 메뉴 ---")
            for item, info in self.menu_manager.menu_items.items():
                print(f"{item}: {info['price']}원")

            menu_choice = input("주문할 메뉴를 입력하세요 (종료: 'q'): ")
            if menu_choice == 'q':
                print("키오스크를 종료합니다.")
                break

            menu_info = self.menu_manager.get_menu_info(menu_choice)
            if not menu_info:
                print("유효하지 않은 메뉴입니다. 다시 선택해주세요.")
                continue

            try:
                quantity = int(input(f"{menu_choice}을(를) 몇 개 주문하시겠습니까? "))
                if quantity <= 0:
                    raise ValueError
            except ValueError:
                print("유효하지 않은 수량입니다. 다시 입력해주세요.")
                continue

            order_details = self.order_processor.create_order(menu_choice, quantity, menu_info['price'])
            if order_details:
                order_id = order_details["order_id"]
                total_amount = order_details["total_amount"]
                print(f"총 결제 금액: {total_amount}원")
                payment_method = input("결제 방식을 선택하세요 (카드/현금): ")
                
                if self.order_processor.process_payment(order_id, payment_method):
                    print("주문이 성공적으로 처리되었습니다.")
                else:
                    print("주문 처리에 실패했습니다.")

if __name__ == "__main__":
    payment_gateway = PaymentGateway()
    beverage_maker = BeverageMaker()
    menu_manager = MenuManager()
    order_processor = OrderProcessor(payment_gateway, beverage_maker)
    
    kiosk_app = KioskUI(menu_manager, order_processor)
    kiosk_app.start()