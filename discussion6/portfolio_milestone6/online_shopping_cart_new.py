class ItemToPurchase:
    def __init__(self, name="none", price=0, quantity=0, description="none"):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, item_name):
        item_found = False
        for item in self.cart_items:
            if item.name == item_name:
                self.cart_items.remove(item)
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, ItemToPurchase):
        item_found = False
        for item in self.cart_items:
            if item.name == ItemToPurchase.name:
                if ItemToPurchase.description != "none":
                    item.description = ItemToPurchase.description
                if ItemToPurchase.price != 0:
                    item.price = ItemToPurchase.price
                if ItemToPurchase.quantity != 0:
                    item.quantity = ItemToPurchase.quantity
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.quantity
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.price * item.quantity
        return total_cost

    def print_total(self):
        total_cost = self.get_cost_of_cart()
        if total_cost == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                print(f"{item.name} {item.quantity} @ ${item.price} = ${item.price * item.quantity}")
            print(f"Total: ${total_cost}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.name}: {item.description}")

def print_menu(cart):
    menu = """
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: """

    while True:
        print(menu)
        choice = input().strip()

        if choice == 'a':
            # Add item to cart
            print("ADD ITEM TO CART")
            item_name = input("Enter the item name: ")
            item_price = float(input("Enter the item price: "))  # Capture price as float
            item_quantity = int(input("Enter the quantity of the item: "))
            item_description = input("Enter the item description: ")
            new_item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(new_item)

        elif choice == 'r':
            # Remove item from cart
            print("REMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove: ")
            cart.remove_item(item_name)

        elif choice == 'c':
            # Change item quantity
            print("CHANGE ITEM QUANTITY")
            item_name = input("Enter the item name: ")
            quantity = int(input("Enter the new quantity: "))
            # Find the item to update
            item_found = False
            for item in cart.cart_items:
                if item.name == item_name:
                    modified_item = ItemToPurchase(item_name, item.price, quantity, item.description)
                    cart.modify_item(modified_item)
                    item_found = True
                    break
            if not item_found:
                print("Item not found in cart. Nothing modified.")

        elif choice == 'i':
            # Output items' descriptions
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif choice == 'o':
            # Output shopping cart
            print("OUTPUT SHOPPING CART")
            cart.print_total()

        elif choice == 'q':
            # Quit
            print("Quit")
            break

        else:
            print("Invalid option, please try again.")

def main():
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)

if __name__ == "__main__":
    main()

