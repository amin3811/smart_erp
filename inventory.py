import json
import os

inventory_file = "data/inventory.json"

def load_inventory():
    if not os.path.exists(inventory_file):
        return []
    with open(inventory_file, "r", encoding="utf-8") as f:
        return json.load(f)

def save_inventory(data):
    with open(inventory_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_product(name, quantity, price):
    inventory = load_inventory()
    inventory.append({
        "name": name,
        "quantity": quantity,
        "price": price
    })
    save_inventory(inventory)

def show_inventory():
    inventory = load_inventory()
    if not inventory:
        print("📦 انباری وجود ندارد.")
        return
    for i, item in enumerate(inventory, start=1):
        print(f"{i}. 📌 {item['name']} - 📦 تعداد: {item['quantity']} - 💰 قیمت: {item['price']} تومان")

def edit_product(index, new_name, new_quantity, new_price):
    inventory = load_inventory()
    if 0 <= index < len(inventory):
        inventory[index] = {
            "name": new_name,
            "quantity": new_quantity,
            "price": new_price
        }
        save_inventory(inventory)

def delete_product(index):
    inventory = load_inventory()
    if 0 <= index < len(inventory):
        inventory.pop(index)
        save_inventory(inventory)
