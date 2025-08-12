class Product:
    def init(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Store:
    def init(self):
        self.products = []

    def add_product(self, name, quantity):
        product = Product(name, quantity)
        self.products.append(product)

    def show_products(self):
        print("รายการสินค้าในร้าน:")
        for product in self.__products:
            print(f"- {product.name}: {product.quantity} ชิ้น")

my_store = Store()
my_store.add_product("หนังยาง", 30)
my_store.add_product("ถุงพลาสติก", 15)

my_store.show_products()