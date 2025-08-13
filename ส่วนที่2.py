class Product:
    def __init__(self, name, quantity):
        self.name = str(name)
        self.quantity = int(quantity)

class Store:
    def __init__(self):
        self.products = {}  # ใช้ dict เก็บสินค้า โดย key = ชื่อสินค้า

    def add_product(self, name, quantity):
        if name in self.products:
            self.products[name].quantity += quantity  # ถ้ามีอยู่แล้วให้บวกเพิ่ม
        else:
            self.products[name] = Product(name, quantity)  # ถ้ายังไม่มีให้สร้างใหม่

    def show_products(self):
        print("รายการสินค้าที่มีในร้าน:")
        for product in self.products.values():
            print(f"- {product.name}: {product.quantity} ชิ้น")

# ทดลองใช้งาน
my_store = Store()
my_store.add_product("หนังยาง", 30)
my_store.add_product("ถุงพลาสติก", 15)
my_store.add_product("หนังยาง", 20)  # เพิ่มสินค้าซ้ำ จะรวมจำนวนให้

my_store.show_products()
