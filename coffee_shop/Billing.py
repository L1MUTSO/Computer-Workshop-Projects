from Order import orders


def cal_total():
    total = 0
    for order in orders:
        total += order["price"] * order["quantity"]
    return total

def cal_discount(total):
    if total > 100000:
        return total * 10/100
    return 0

def cal_bill():
    if not orders:
        print("Your order list is empty !!")
        return

    total = cal_total()
    discount = cal_discount(total)
    final_amount = total - discount

    print("\n======[BILL]======")
    print(f"YOUR TOTAL ORDER : {total}")
    print(f"YOUR DISCOUNT : {discount}")
    print(f"TOTAL WITH DISCOUNT : {final_amount}")
    print("\n==================")

