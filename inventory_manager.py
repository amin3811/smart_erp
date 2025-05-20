import json
import os

DATA_FILE = "data/inventory.json"

def load_inventory():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_inventory(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_product():
    print("➕ افزودن کالا:")
    name = input("نام کالا: ").strip()
    quantity = int(input("تعداد: "))
    price = int(input("قیمت (تومان): "))
    
    inventory = load_inventory()
    inventory.append({"name": name, "quantity": quantity, "price": price})
    save_inventory(inventory)
    print("✅ کالا با موفقیت افزوده شد.")

def list_products():
    print("📦 لیست کالاهای انبار:")
    inventory = load_inventory()
    if not inventory:
        print("⛔ هیچ کالایی وجود ندارد.")
        return
    for i, item in enumerate(inventory, 1):
        print(f"{i}. {item['name']} | تعداد: {item['quantity']} | قیمت: {item['price']} تومان")

def edit_product():
    inventory = load_inventory()
    list_products()
    index = int(input("شماره کالایی که می‌خواهید ویرایش کنید: ")) - 1
    if 0 <= index < len(inventory):
        name = input("نام جدید کالا (برای تغییر ندادن Enter بزنید): ").strip()
        quantity = input("تعداد جدید (برای تغییر ندادن Enter بزنید): ").strip()
        price = input("قیمت جدید (برای تغییر ندادن Enter بزنید): ").strip()

        if name:
            inventory[index]["name"] = name
        if quantity:
            inventory[index]["quantity"] = int(quantity)
        if price:
            inventory[index]["price"] = int(price)

        save_inventory(inventory)
        print("✅ کالا با موفقیت ویرایش شد.")
    else:
        print("❌ شماره نامعتبر!")

def delete_product():
    inventory = load_inventory()
    list_products()
    index = int(input("شماره کالایی که می‌خواهید حذف کنید: ")) - 1
    if 0 <= index < len(inventory):
        deleted = inventory.pop(index)
        save_inventory(inventory)
        print(f"🗑️ کالا '{deleted['name']}' حذف شد.")
    else:
        print("❌ شماره نامعتبر!")
