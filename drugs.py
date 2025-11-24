import os

dict_drugs = {
    "name": [],
    "price_per_strip": [],
    "price_per_piece": [],
    "piece_per_box": [],
    "piece_per_strip": []
}

file_name = "drugs.txt"

def load_drugs_data():
    if not os.path.exists(file_name):
        return
    
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue

            name, price_per_strip, price_per_piece, piece_per_box, piece_per_strip = line.split(',')

            dict_drugs["name"].append(name)
            dict_drugs["price_per_strip"].append(price_per_strip)
            dict_drugs["price_per_piece"].append(price_per_piece)
            dict_drugs["piece_per_box"].append(piece_per_box)
            dict_drugs["piece_per_strip"].append(piece_per_strip)


def save_drugs():
    with open(file_name, "w") as f:
        for i in range(len(dict_drugs["name"])):
            f.write(
                dict_drugs["name"][i] + "," +
                dict_drugs["price_per_strip"][i] + "," +
                dict_drugs["price_per_piece"][i] + "," +
                dict_drugs["piece_per_box"][i] + "," +
                dict_drugs["piece_per_strip"][i] + "\n"
            )

def add_drugs():
    name = input("Drug Name: ").lower()
    
    if name in dict_drugs["name"]:
        piece_per_box = input("Add Strips to Box: ")
        i = dict_drugs["name"].index(name)
        dict_drugs["piece_per_box"][i] = str(int(dict_drugs["piece_per_box"][i]) + int(piece_per_box))

        save_drugs()
        print("✔ Drug updated successfully!\n")
    
    else:
        price_per_strip = input("Per Strip Price: ")
        price_per_piece = input("Per Piece Price: ")
        piece_per_strip = input("Pieces per Strip: ")
        piece_per_box = input("Strips per Box: ")

        dict_drugs["name"].append(name)
        dict_drugs["price_per_strip"].append(price_per_strip)
        dict_drugs["price_per_piece"].append(price_per_piece)
        dict_drugs["piece_per_strip"].append(piece_per_strip)
        dict_drugs["piece_per_box"].append(piece_per_box)

        save_drugs()
        print("✔ Drug added successfully!\n")

def show_all():
    print("\n=== All Drugs ===")
    for i in range(len(dict_drugs["name"])):

        total_pieces = int(dict_drugs["piece_per_box"][i]) * int(dict_drugs["piece_per_strip"][i])

        print(
            f"{dict_drugs['name'][i]} | Per Strip: {dict_drugs['price_per_strip'][i]} TK | "
            f"Per Piece: {dict_drugs['price_per_piece'][i]} TK | "
            f"Strips: {dict_drugs['piece_per_box'][i]} | "
            f"Pieces/Strip: {dict_drugs['piece_per_strip'][i]} | "
            f"Total Pieces: {total_pieces}"
        )
    print()


def add_discount(price):
    if price >= 2000:
        discount = price * 0.10
    elif price >= 500:
        discount = price * 0.07
    elif price >= 100:
        discount = price * 0.05
    else:
        discount = 0
    
    final_price = price - discount
    return discount, final_price


def drug_sell():
    name = input("Drug Name: ").lower()

    if name in dict_drugs["name"]:
        i = dict_drugs["name"].index(name)
        
        available_strips = int(dict_drugs["piece_per_box"][i])
        pieces_per_strip = int(dict_drugs["piece_per_strip"][i])
        price_per_piece = float(dict_drugs["price_per_piece"][i])

        available_pieces = available_strips * pieces_per_strip

        print(f"\nEach strip has {pieces_per_strip} pieces.")
        print(f"📦 Total available pieces: {available_pieces}")

        needed_pieces = int(input("How many pieces do you want?: "))

        if available_pieces <= 0:
            print("❌ Out of stock!")
            return

        if needed_pieces > available_pieces:
            print(f"⚠ Only {available_pieces} pieces are available.")

            while True:
                choice = input(f"Do you want to take all {available_pieces}? (yes/no): ").strip().lower()
                if choice == "yes":
                    sold = available_pieces
                    break
                elif choice == "no":
                    print("❌ Sale cancelled.")
                    return
                else:
                    print("⚠ Type only yes/no.")
        else:
            sold = needed_pieces

        total_price = sold * price_per_piece

        discount, final_price = add_discount(total_price)

        remaining_pieces = available_pieces - sold
        dict_drugs["piece_per_box"][i] = str(remaining_pieces // pieces_per_strip)

        save_drugs()

        print("\n✔ **Sale Complete!**")
        print(f"🧾 Sold Pieces: {sold}")
        print(f"💵 Total Price (Before Discount): {total_price} TK")
        print(f"🏷 Discount Given: {discount} TK")
        print(f"💰 Final Price (After Discount): {final_price} TK")
        print(f"📦 Remaining Pieces: {remaining_pieces}")

    else:
        print("❌ Drug Not Found!\n")


def drugs_manage():
    while True:
        print("""
    ====== Pharmacy Menu ======

1. Add Drug
2. Sell Drug
3. Show All Drugs
4. Exit
    """)

        choice = input("Choose Option: ")
        
        if choice == "1":
            add_drugs()
        elif choice == "2":
            drug_sell()
        elif choice == "3":
            show_all()
        elif choice == "4":
            break
        else:
            print("⚠ Invalid choice, try again.\n")
            
load_drugs_data()