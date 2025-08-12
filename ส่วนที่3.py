import uuid  # สำหรับสร้างรหัสคำสั่งซื้อแบบไม่ซ้ำกัน

# ========================
# คลาสสินค้า
# ========================
class Product:
    def __init__(self, name, description, price, online_shop):
        self.name = name
        self.description = description
        self.price = price
        self.online_shop = online_shop

# ========================
# คลาสลูกค้า
# ========================
class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.cart = []         # ตะกร้าสินค้าที่เลือกไว้
        self.past_orders = []  # ประวัติการสั่งซื้อที่เคยสั่ง

# ========================
# คลาสร้านค้าออนไลน์
# ========================
class OnlineShop:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.products = []

    # เพิ่มสินค้าไปยังตะกร้าของลูกค้า
    def addingItemsToCart(self, customer, product, quantity):
        customer.cart.append({
            "product": product,
            "quantity": quantity
        })

    # ดำเนินการสั่งซื้อ
    def checkOut(self, customer):
        total = 0
        order_items = []

        for item in customer.cart:
            product = item["product"]
            quantity = item["quantity"]
            price = product.price * quantity
            total += price
            order_items.append({
                "product": product.name,
                "quantity": quantity,
                "price": price
            })

        order_id = str(uuid.uuid4())  # สร้างรหัสคำสั่งซื้อแบบสุ่ม
        order = {
            "order_id": order_id,
            "items": order_items,
            "total": total
        }

        customer.past_orders.append(order)
        customer.cart = []  # ล้างตะกร้าหลังชำระเงิน

        print("สั่งซื้อสำเร็จ! รหัสคำสั่งซื้อ:", order_id)
        return order_id

    # ตรวจสอบคำสั่งซื้อจากรหัส
    def orderTracking(self, customer, order_id):
        for order in customer.past_orders:
            if order["order_id"] == order_id:
                print("พบคำสั่งซื้อ:")
                for item in order["items"]:
                    print(f"- {item['product']} x {item['quantity']} = {item['price']} บาท")
                print("รวมทั้งหมด:", order["total"], "บาท")
                return
        print("ไม่พบคำสั่งซื้อนี้")


# ========================
# ส่วนทดสอบการทำงาน
# ========================

# สร้างร้านค้า
shop = OnlineShop("Seagull", "www.seagull.com")

# สร้างสินค้า
p1 = Product("หนังยาง", 30, shop)
p2 = Product("ถุงพลาสติก", 15, shop)

# เพิ่มสินค้าเข้าในร้าน
shop.products.extend([p1, p2])

# สร้างลูกค้า
customer = Customer("Kong", "kong@example.com", "123 Main St")

# ลูกค้าเพิ่มของลงตะกร้า
shop.addingItemsToCart(customer, p1, 2)  
shop.addingItemsToCart(customer, p2, 1)  

# ลูกค้าทำการสั่งซื้อ
order_id = shop.checkOut(customer)

# ลูกค้าตรวจสอบคำสั่งซื้อ
shop.orderTracking(customer, order_id)