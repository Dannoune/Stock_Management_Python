class Fournisseurs:
    def __init__(self):
        self.suppliers = []
        self.contact_info = {}

    def add_supplier(self, supplier_name, contact_info):
        self.suppliers.append(supplier_name)
        self.contact_info[supplier_name] = contact_info

    def get_supplier_contact(self, supplier_name):
        return self.contact_info.get(supplier_name, "Contact information not available")
