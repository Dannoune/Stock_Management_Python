class Commandes:
    def __init__(self):
        self.orders = []

    def place_order(self, product_name, quantity, supplier):
        self.orders.append({'product': product_name, 'quantity': quantity, 'supplier': supplier})

    def get_total_orders(self):
        return len(self.orders)
