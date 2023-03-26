from menu import products


def calculate_tab(list):
    total = 0
    for item_product in products:
        for item in list:
            if item["_id"] == item_product["_id"]:
                total += item_product["price"] * item["amount"]
            else:
                continue
    obj = {"subtotal": f"${round(total, 2)}"}

    return obj
