from Billing import cal_bill, cal_total
from Menu import show_menu
from Order import add_order, show_orders


def main():
    while True:
        print("\n======[COFFEE SHOP]======")
        print("1. Today's Menu")
        print("2. Order")
        print("3. Display my order")
        print("4. Total Price")
        print("5. Bill & Discount")
        print("6. Exit")
        choice = input("Pls Select your entry: ")

        if choice == "1":
            show_menu()
        elif choice == "2":
            add_order()
        elif choice == "3":
            show_orders()
        elif choice == "4":
            print(f"TOTAL PRICE : {cal_total()} Tooman")
        elif choice == "5":
            cal_bill()
        elif choice == "6":
            print("Bye , see you soon :)")
        else:
            print("Pls recheck your entry and try again : ")


if __name__ == "__main__":
    main()
        
