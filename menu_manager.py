
class MenuManager:
    def __init__(self):
        self.menu_items = {
            "아메리카노": {"price": 4000, "stock": 100},
            "카페라떼": {"price": 4500, "stock": 80},
            "카푸치노": {"price": 4500, "stock": 70}
        }

    def get_menu_info(self, menu_name):
        return self.menu_items.get(menu_name)