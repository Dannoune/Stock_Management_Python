class Ventes:
    def __init__(self):
        self.sales_records = []

    def record_sale(self, product_name, quantity, price):
        self.sales_records.append({'product': product_name, 'quantity': quantity, 'price': price})

    def get_total_sales(self):
        return sum(record['quantity'] * record['price'] for record in self.sales_records)

