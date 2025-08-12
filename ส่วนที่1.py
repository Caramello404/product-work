product_list = {}

def add_product(product_list):
    product_name = input("Enter product Name: ")
    product_quantity = int(input("Enter product Quantity: "))
    if product_name in product_list:
        product_list[product_name] += product_quantity
    else: 
        product_list[product_name] = product_quantity

def show_products(product_list):
    for key in product_list.keys():
        print(key+ " : " + str(product_list[key]))

add_product(product_list)
add_product(product_list)
add_product(product_list)
show_products(product_list)