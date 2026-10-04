def calculate_item_total(quantity: int, price: int) -> int:
    return quantity * price


def combine_sales(file_name: str) -> dict:
    sales_data = {}

    with open(file_name, "r") as file:
        lines = file.readlines()

    index = 0
    while index < len(lines):
        line = lines[index].strip()
        fruit, qty_str, price_str = line.split(",")
        qty = int(qty_str)
        price = int(price_str)

        if fruit in sales_data:
            sales_data[fruit]["count"] += qty
        else:
            sales_data[fruit] = {"count": qty, "price": price}
        index += 1

    fruits = list(sales_data.keys())
    index = 0
    with open("receipt.txt", "w") as receipt:
        receipt.write("FRUIT   | COUNT | TOTAL\n")

        while index < len(fruits):
            name = fruits[index]
            count = sales_data[name]["count"]
            unit_price = sales_data[name]["price"]
            total_cost = calculate_item_total(count, unit_price)

            receipt.write(f"{name:<7} | {count:<5} | ${total_cost}\n")
            index += 1

    return sales_data


if __name__ == "__main__":
    combine_sales("sales.txt")