"""
Titre du Code: Gestion de Stock
Auteur: DANNOUNE Mohamed-Amine
Année: 2023

Ce programme permet de gérer un stock en enregistrant les produits, les ventes, les fournisseurs et les commandes.
Il utilise plusieurs modules distincts pour chaque fonctionnalité.

Modules:
- module_stock.py: Gère le stock des produits.
- module_ventes.py: Enregistre les ventes des produits.
- module_fournisseurs.py: Gère les informations sur les fournisseurs.
- module_commandes.py: Gère les commandes passées aux fournisseurs.

Le programme principal instancie les modules nécessaires et interagit avec l'utilisateur pour saisir les informations
sur les produits, les ventes, les fournisseurs et les commandes. Il met à jour le stock global en fonction des commandes
et des ventes, et enregistre les informations dans un fichier texte.

Pour exécuter le programme, exécutez la fonction main() dans ce fichier.

"""

import module_stock
import module_ventes
import module_fournisseurs
import module_commandes

class Main:
    def __init__(self):
        self.stock = module_stock.Stock()
        self.ventes = module_ventes.Ventes()
        self.fournisseurs = module_fournisseurs.Fournisseurs()
        self.commandes = module_commandes.Commandes()

    def run(self):
        # Demande à l'utilisateur d'entrer les informations
        product_name = input("Nom du produit: ")
        quantity = int(input("Quantité: "))
        price = float(input("Prix: "))
        supplier_name = input("Nom du fournisseur: ")
        contact_info = input("Informations de contact: ")

        self.stock.add_product(product_name)
        self.stock.update_stock(product_name, quantity)
        self.ventes.record_sale(product_name, quantity, price)
        self.fournisseurs.add_supplier(supplier_name, contact_info)
        self.commandes.place_order(product_name, quantity, supplier_name)

        # Mise à jour du stock global en fonction des commandes passées
        self.stock.adjust_stock_with_orders(self.commandes)

        # Mise à jour du stock global en fonction des ventes
        self.stock.adjust_stock_with_sales(self.ventes)

        # Demande à l'utilisateur d'entrer le stock total
        total_stock = int(input("Stock total: "))

        # Calcul du stock global
        stock_global = total_stock - self.stock.get_total_quantity()

        # Affiche les informations
        print("\nInformations sur le stock:")
        print("Stock par produit:")
        for product_name in self.stock.products:
            quantity = self.stock.get_stock_quantity(product_name)
            print(f"{product_name}: {quantity}")
        print("Stock global:", stock_global)
        print("Nombre total de commandes passées:", self.commandes.get_total_orders())

        # Enregistre les informations dans un fichier texte
        self.save_data(total_stock, stock_global)

    def save_data(self, total_stock, stock_global):
        with open('data.txt', 'w') as file:
            file.write("=====================================\n")
            file.write("Stock:\n")
            for product_name in self.stock.products:
                quantity = self.stock.get_stock_quantity(product_name)
                #file.write(f"{product_name}: {quantity}\n")

            file.write("\nStock total: {}\n".format(total_stock))
            file.write("\nVentes:\n")
            for record in self.ventes.sales_records:
                file.write(f"Produit: {record['product']}, Quantité: {record['quantity']}, Prix: {record['price']}\n")

            file.write("\nFournisseurs:\n")
            for supplier_name in self.fournisseurs.suppliers:
                contact_info = self.fournisseurs.get_supplier_contact(supplier_name)
                file.write(f"Nom: {supplier_name}, Contact: {contact_info}\n")

            file.write("\nCommandes:\n")
            for order in self.commandes.orders:
                file.write(f"Produit: {order['product']}, Quantité: {order['quantity']}, Fournisseur: {order['supplier']}\n")


if __name__ == '__main__':
    app = Main()
    app.run()
