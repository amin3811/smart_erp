import tkinter as tk
from tkinter import messagebox
from inventory_manager import add_product, list_products, edit_product, delete_product
from invoice_processor import process_invoice

def run_add():
    add_product()
def run_list():
    list_products()
def run_edit():
    edit_product()
def run_delete():
    delete_product()
def run_invoice():
    process_invoice()

root = tk.Tk()
root.title("سیستم مدیریت انبار هوشمند")
root.geometry("400x350")

tk.Label(root, text="منو اصلی", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="➕ افزودن کالا", command=run_add, width=30).pack(pady=5)
tk.Button(root, text="📋 نمایش کالاها", command=run_list, width=30).pack(pady=5)
tk.Button(root, text="✏️ ویرایش کالا", command=run_edit, width=30).pack(pady=5)
tk.Button(root, text="🗑️ حذف کالا", command=run_delete, width=30).pack(pady=5)
tk.Button(root, text="🧾 ثبت فاکتور خروجی", command=run_invoice, width=30).pack(pady=5)
tk.Button(root, text="🚪 خروج", command=root.quit, width=30).pack(pady=20)

root.mainloop()
