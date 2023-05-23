import module_stock
import module_ventes
import module_fournisseurs
import module_commandes

def main():
    stock = module_stock.Stock()
    ventes = module_ventes.Ventes()
    fournisseurs = module_fournisseurs.Fournisseurs()
    commandes = module_commandes.Commandes()

    # Demande à l'utilisateur d'entrer les informations
    product_name = input("Nom du produit: ")
    quantity = int(input("Quantité: "))
    price = float(input("Prix: "))
    supplier_name = input("Nom du fournisseur: ")
    contact_info = input("Informations de contact: ")

    # Utilisez les instances des modules pour interagir avec le programme
    stock.add_product(product_name)
    stock.update_stock(product_name, quantity)
    ventes.record_sale(product_name, quantity, price)
    fournisseurs.add_supplier(supplier_name, contact_info)
    commandes.place_order(product_name, quantity, supplier_name)

    # Mise à jour du stock global en fonction des commandes passées
    stock.adjust_stock_with_orders(commandes)

    # Mise à jour du stock global en fonction des ventes
    stock.adjust_stock_with_sales(ventes)

    # Demande à l'utilisateur d'entrer le stock total
    total_stock = int(input("Stock total: "))

    # Calcul du stock global
    stock_global = total_stock - stock.get_total_quantity()

    # Affiche les informations
    print("\nInformations sur le stock:")
    print("Stock par produit:")
    for product_name in stock.products:
        quantity = stock.get_stock_quantity(product_name)
        print(f"{product_name}: {quantity}")
    print("Stock global:", stock_global)
    print("Nombre total de commandes passées:", commandes.get_total_orders())

    # Enregistre les informations dans un fichier texte
    save_data(stock, ventes, fournisseurs, commandes, total_stock, stock_global)

def save_data(stock, ventes, fournisseurs, commandes, total_stock, stock_global):
    with open('data.txt', 'w') as file:
        file.write("=====================================\n")
        file.write("Stock:\n")
        for product_name in stock.products:
            quantity = stock.get_stock_quantity(product_name)
            #file.write(f"{product_name}: {quantity}\n")

        file.write("\nStock total: {}\n".format(total_stock))
        file.write("\nVentes:\n")
        for record in ventes.sales_records:
            file.write(f"Produit: {record['product']}, Quantité: {record['quantity']}, Prix: {record['price']}\n")

        file.write("\nFournisseurs:\n")
        for supplier_name in fournisseurs.suppliers:
            contact_info = fournisseurs.get_supplier_contact(supplier_name)
            file.write(f"Nom: {supplier_name}, Contact: {contact_info}\n")

        file.write("\nCommandes:\n")
        for order in commandes.orders:
            file.write(f"Produit: {order['product']}, Quantité: {order['quantity']}, Fournisseur: {order['supplier']}\n")

        file.write("=====================================\n")
        file.write("Stock Courant: {}\n".format(stock_global))
        file.write("=====================================\n")

if __name__ == '__main__':
    main()
