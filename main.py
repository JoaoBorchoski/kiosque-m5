from management.product_handler import (
    get_product_by_id,
    get_products_by_type,
    add_product,
    menu_report,
)
from management.tab_handler import calculate_tab
from menu import products


if __name__ == "__main__":
    print(get_product_by_id(28))
    print(get_products_by_type("drink"))
    print(
        add_product(
            products,
            **{
                "description": "description here",
                "price": 20,
                "rating": 5,
                "title": "title here",
                "type": "type here",
            },
        )
    )
    print(
        calculate_tab(
            [
                {"_id": 10, "amount": 3},
                {"_id": 20, "amount": 2},
                {"_id": 21, "amount": 5},
            ]
        )
    )
    print(menu_report())
