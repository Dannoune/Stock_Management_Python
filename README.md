# Repository_Python
Stock Management Program

This Python stock management program helps businesses track and manage their inventory. It allows for product tracking, sales recording, order placement, and supplier management, providing functionality to record, update, and monitor stock-related information.

The program is divided into several distinct modules:

    Stock Module (module_stock.py): Handles stock-related operations. It enables adding products, updating stock quantities, retrieving stock quantities for a given product, calculating the total quantity of all products in stock, and adjusting stock based on placed orders and recorded sales.

    Sales Module (module_ventes.py): Manages recorded sales. It allows for recording sale details, such as product name, quantity sold, and sale price.

    Suppliers Module (module_fournisseurs.py): Handles supplier management. It allows for adding suppliers and storing their contact information.

    Orders Module (module_commandes.py): Manages placed orders. It enables placing an order by specifying the product, quantity, and supplier.

The main program (main.py) serves as the entry point of the application. It creates instances of the modules and interacts with the user to gather information about products, sales, suppliers, and orders. It also updates the global stock based on placed orders and recorded sales. The user is prompted to provide the total stock, and the program calculates the global stock by subtracting the quantity from the total stock.

The program displays stock information, including stock quantities per product, global stock, and the total number of placed orders. It also saves all information to a text file named data.txt.

This Python stock management program provides a solid foundation for efficiently tracking and managing inventory for businesses. It can be extended and enhanced to meet specific business needs by adding new features or integrating additional functionality.


@DANNOUNE Mohamed-Amine
