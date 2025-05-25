
import uuid

class OrderProcessor:
    def __init__(self, payment_gateway, beverage_maker):
        self.orders = {}
        self.payment_gateway = payment_gateway
        self.beverage_maker = beverage_maker

    def create_order(self, menu_name, quantity, price):
        order_id = str(uuid.uuid4())
        total_amount = price * quantity
        self.orders[order_id] = {
            "menu_name": menu_name,
            "quantity": quantity,
            "total_amount": total_amount,
            "status": "pending_payment"
        }
        print(f"주문이 생성되었습니다. 주문 ID: {order_id}, 총액: {total_amount}원")
        return {"order_id": order_id, "total_amount": total_amount}

    def process_payment(self, order_id, payment_method):
        order = self.orders.get(order_id)
        if not order:
            print("유효하지 않은 주문 ID입니다.")
            return False

        if order["status"] == "paid":
            print("이미 결제된 주문입니다.")
            return True

        print(f"결제 진행 중... 주문 ID: {order_id}, 결제 방식: {payment_method}")
        payment_success = self.payment_gateway.request_payment(order["total_amount"])

        if payment_success:
            order["status"] = "paid"
            print(f"결제 성공! 주문 ID: {order_id}")
            self.beverage_maker.make_beverage(order["menu_name"], order["quantity"])
            return True
        else:
            order["status"] = "payment_failed"
            print(f"결제 실패! 주문 ID: {order_id}")
            return False