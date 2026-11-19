from Menu import menu

orders = []

def add_order():
    name = input("What's your order ?: ").strip().lower()

    if name not in menu:
        print("There's no such a thing our menu")
        return

    try:
        quantity = int(input("How many ?: "))
    except ValueError:
        print("You should enter valid quantity")
        return

    if quantity <= 0:
        print("You should order more than 0")
        return

    orders.append({"name": name, "price": menu[name], "quantity": quantity})
    print("Thanks for your order ; your order has confirmed")

def show_orders():
    if not orders:
        print("Order list is empty !!")
        return

    print("\n======[ORDERS]======")
    for order in orders:
        print("Product:", order["name"], "| Price", order["price"], "| quantity:", order["quantity"])
