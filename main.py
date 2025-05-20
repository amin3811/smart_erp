from inventory_manager import add_product, list_products, edit_product, delete_product
from invoice_processor import process_invoice

def show_menu():
    print("\n📌 منو:")
    print("1. افزودن کالا به انبار")
    print("2. نمایش کالاهای انبار")
    print("3. ویرایش کالا")
    print("4. حذف کالا")
    print("5. ثبت فاکتور خروجی")
    print("6. خروج")

def main():
    while True:
        show_menu()
        choice = input("انتخاب شما: ").strip()
        
        if choice == "1":
            add_product()
        elif choice == "2":
            list_products()
        elif choice == "3":
            edit_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            process_invoice()
        elif choice == "6":
            print("👋 خداحافظ رییس!")
            break
        else:
            print("❌ گزینه نامعتبر!")

if __name__ == "__main__":
    main()
