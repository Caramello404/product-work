import uuid  # สำหรับสร้างรหัสคำสั่งซื้อ

# ========================
# คลาสสินค้า
# ========================
class Product:
    def __init__(self, name, description, price, quantity, online_shop):
        self.name = str(name)
        self.description = str(description)
        self.price = float(price)
        self.quantity = int(quantity)
        self.online_shop = online_shop

# ========================
# คลาสลูกค้า
# ========================
class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.cart = []         # ตะกร้าสินค้า
        self.past_orders = []  # ประวัติการสั่งซื้อ

# ========================
# คลาสร้านค้า
# ========================
class OnlineShop:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.products = {}  # เก็บสินค้าในรูปแบบ dict {ชื่อสินค้า: Product}

    # เพิ่มหรืออัปเดตสินค้าในสต็อก
    def add_product(self, name, description, price, quantity):
        if name in self.products:
            self.products[name].quantity += quantity
        else:
            self.products[name] = Product(name, description, price, quantity, self)

    # แสดงสินค้าทั้งหมดในร้าน
    def show_products(self):
        print(f"📦 สินค้าในร้าน {self.name}:")
        for product in self.products.values():
            print(f"- {product.name} ({product.description}): {product.quantity} ชิ้น, {product.price} บาท")

    # เพิ่มสินค้าลงตะกร้าลูกค้า
    def addingItemsToCart(self, customer, product_name, quantity):
        if product_name not in self.products:
            print("❌ ไม่มีสินค้านี้ในร้าน")
            return
        product = self.products[product_name]
        if quantity > product.quantity:
            print("❌ จำนวนสินค้าไม่พอในสต็อก")
            return
        customer.cart.append({"product": product, "quantity": quantity})

    # ทำการชำระเงิน
    def checkOut(self, customer):
        if not customer.cart:
            print("❌ ไม่มีสินค้าในตะกร้า")
            return None

        total = 0
        order_items = []
        for item in customer.cart:
            product = item["product"]
            quantity = item["quantity"]
            total += product.price * quantity
            order_items.append({
                "product": product.name,
                "quantity": quantity,
                "price": product.price * quantity
            })
            product.quantity -= quantity  # ตัดสต็อก

        order_id = str(uuid.uuid4())
        order = {
            "order_id": order_id,
            "items": order_items,
            "total": total
        }
        customer.past_orders.append(order)
        customer.cart.clear()

        print(f"✅ สั่งซื้อสำเร็จ! รหัสคำสั่งซื้อ: {order_id}")
        return order_id

    # ตรวจสอบคำสั่งซื้อ
    def orderTracking(self, customer, order_id):
        for order in customer.past_orders:
            if order["order_id"] == order_id:
                print("📜 รายการคำสั่งซื้อ:")
                for item in order["items"]:
                    print(f"- {item['product']} x {item['quantity']} = {item['price']} บาท")
                print(f"💰 รวมทั้งหมด: {order['total']} บาท")
                return
        print("❌ ไม่พบคำสั่งซื้อที่ระบุ")


# ========================
# ตัวอย่างการใช้งาน
# ========================

# สร้างร้าน
shop = OnlineShop("Seagull", "www.seagull.com")

# เพิ่มสินค้า
shop.add_product("โฟมล้างหน้า", "Smooth E Babyface Foam", 30, 50)
shop.add_product("ทิชชู่", "สก๊อตต์ คลีนแคร์ 3 ชั้น", 15, 100)
shop.add_product("แชมพู", "TRESemme'", 149, 40)

# แสดงสินค้า
shop.show_products()

# สร้างลูกค้า
customer = Customer("Kong", "kong@example.com", "123 Main St")

# เพิ่มสินค้าลงตะกร้า
shop.addingItemsToCart(customer, "โฟมล้างหน้า", 2)
shop.addingItemsToCart(customer, "ทิชชู่", 1)

# ชำระเงิน
order_id = shop.checkOut(customer)

# ติดตามคำสั่งซื้อ
if order_id:
    shop.orderTracking(customer, order_id)

# แสดงสินค้าอีกครั้งเพื่อตรวจสอบสต็อกหลังการซื้อ
shop.show_products()
