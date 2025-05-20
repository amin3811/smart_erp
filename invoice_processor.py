import os
import json

DATA_FILE = "data/products.json"

def process_invoice():
    if not os.path.exists(DATA_FILE):
        print("❌ انبار هنوز محصولی ندارد.")
        return

    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        products = json.load(f)

    invoice_id = input("🧾 شماره فاکتور را وارد کنید: ")
    items = []

    while True:
        code = input("📦 کد کالا (برای خروج بنویس 'exit'): ")
        if code == "exit":
            break
        quantity = int(input("🔢 تعداد: "))

        found = False
        for product in products:
            if product["code"] == code:
                if product["quantity"] >= quantity:
                    product["quantity"] -= quantity
                    items.append({"name": product["name"], "code": code, "quantity": quantity})
                    print(f"✅ {quantity} عدد از {product['name']} کم شد.")
                else:
                    print("⚠️ موجودی کافی نیست.")
                found = True
                break
        if not found:
            print("❌ کالا پیدا نشد.")

    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(products, f, indent=2, ensure_ascii=False)

    # ذخیره فاکتور
    invoice_data = {
        "invoice_id": invoice_id,
        "items": items
    }

    invoice_path = f"data/invoices/{invoice_id}.json"
    with open(invoice_path, 'w', encoding='utf-8') as f:
        json.dump(invoice_data, f, indent=2, ensure_ascii=False)

    print(f"🧾 فاکتور {invoice_id} ذخیره شد.")

