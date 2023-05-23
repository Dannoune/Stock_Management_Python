class Stock:
    def __init__(self):
        self.products = []
        self.stock_quantities = {}
        self.min_stock_threshold = 10
        self.max_stock_threshold = 100

    def add_product(self, product_name):
        self.products.append(product_name)
        self.stock_quantities[product_name] = 0

    def update_stock(self, product_name, quantity):
        if product_name in self.products:
            self.stock_quantities[product_name] += quantity

    def get_stock_quantity(self, product_name):
        if product_name in self.products:
            return self.stock_quantities[product_name]
        return 0

    def get_total_quantity(self):
        return sum(self.stock_quantities.values())

    def adjust_stock_with_orders(self, commandes):
        for order in commandes.orders:
            product_name = order['product']
            quantity = order['quantity']
            if product_name in self.products:
                self.stock_quantities[product_name] -= quantity

    def adjust_stock_with_sales(self, ventes):
        for record in ventes.sales_records:
            product_name = record['product']
            quantity = record['quantity']
            if product_name in self.products:
                self.stock_quantities[product_name] -= quantity
