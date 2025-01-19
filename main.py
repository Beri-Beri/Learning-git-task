shopping_list = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]}

print("Lista zakupów")
cap_shopping_list = {shop.capitalize(): [product.capitalize() for product in products] for shop, products in shopping_list.items()}
for shop, product in cap_shopping_list.items():
    print(f"Idę do {shop}, kupuję tu następujące rzeczy: {product}")

product_no = sum([len(shopping_list[product]) for product in shopping_list if isinstance(shopping_list[product], list)])
print(f"W sumie kupuję {product_no} produktów")

divided = [i for i in range(101) if i % 5 == 0]
print(divided)

cubes = [num**3 for num in divided]
print(cubes)