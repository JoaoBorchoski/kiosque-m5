from menu import products


def get_product_by_id(id):
    if type(id) != int:
        raise TypeError("product id must be an int")
    return next((product for product in products if id == product["_id"]), {})


def get_products_by_type(type_prod: str):
    if type(type_prod) != str:
        raise TypeError("product type must be a str")
    arr = []
    for item in products:
        if item["type"] == type_prod:
            arr.append(item)
            continue
        else:
            continue
    return arr


def add_product(list: list, **prod):
    big_id = 0
    for item in list:
        if item["_id"] > big_id:
            big_id = item["_id"]
            continue
        else:
            continue

    id = 1
    if big_id != 0:
        id = big_id + 1

    prod["_id"] = id

    list.append(prod)

    return prod


def menu_report():
    product_count = len(products)

    price = 0
    for item in products:
        price += item["price"]
    avarege_price = round((price / product_count), 2)

    common_type = products[0]["type"]
    for item in products:
        if products.count(item["type"]) > products.count(common_type):
            common_type = item["type"]

    return f"Products Count: {product_count} - Average Price: ${avarege_price} - Most Common Type: {common_type}"
