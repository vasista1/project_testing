class ShoppingCart:
    def __init__(self, limit):
        self.cart_list = []
        self.cart_limit = limit
    def add(self, items):
        if self.cart_limit>self.size():
            if type(items) == str:
                self.cart_list.append(items)
                return self.cart_list[-1]
            else:
                for item in items:
                    if self.cart_limit<=self.size():
                        raise OverflowError
                    self.cart_list.append(item)
                return self.cart_list[-(len(items)):]
        else:
            raise OverflowError
    def size(self):
        return len(self.cart_list)
    def total_price(self,price_map):
        total_price=0
        for item in self.cart_list:
            total_price+=price_map[item]
        return total_price