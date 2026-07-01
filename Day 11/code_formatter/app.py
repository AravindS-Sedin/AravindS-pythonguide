def calculate_total(items, discount=0, tax=0.18):
    total = 0

    for item in items:
        total = total + item["price"] * item["quantity"]

    if discount > 0:
        total = total - (total * discount / 100)

    return round(total, 2)


items = [{"price": 100, "quantity": 2}, {"price": 200, "quantity": 1}]

print(calculate_total(items))
