# insert items

categories = {
    "1": ["Tomato (1kg - 30$ )", "Potato (1kg - 20$ )", "Onion(1kg - 50$ )"],
    "2": ["Apple (1kg - 100$ )", "Banana (1  - 5$ )", "Orange (1kg - 80$ )"],
    "3": ["Laptop 1000$ ", "Mobile 500$", "Headphones 100$"]
}
print("WELCOME TO MY SHOPMART")
print("1. VEGETABLES\n2. FRUITS\n3. ELECTRONICS")

# user to get

choice = input("CHOOSE YOUR CATEGORY (1/2/3): ")
if choice in categories:
    print("Items:", categories[choice])
else:
    print("Invalid choice!")
    
# add to cart and bill

cart = []
bill = 0

while True:
    user = input("ADD YOUR ITEMS IN CART or Buy or Exit : ").lower() #tomato ---> enter kg (per kg 30$)---> 2 ---> added your cart bill = 100
        
    if user == 'buy' and bill == 0:
        print("PLEACE ADD AN ITEMS")
        continue
        break
    if user =='exit':
        break
    
        
    if user == 'tomato':
        adding_item=int(input(f"{user} HOW MANY kg YOU WANT : "))
        bill = bill + adding_item * 30
        cart.extend(user.split())
        print(f"Added {user} in your cart - your Bill is {bill} $")
        
    elif user == 'potato':
        adding_item=int(input(f"{user} HOW MANY kg YOU WANT : "))
        bill = bill + adding_item* 20
        print(f"Added {user} in your cart - your Bill is {bill} $")
        
    elif user == 'onion':
        adding_item=int(input(f"{user} HOW MANY kg YOU WANT : "))
        bill = bill + adding_item * 50
        print(f"Added {user} in your cart - your Bill is {bill} $")
        
    elif user == 'apple':
        adding_item=int(input(f"{user} HOW MANY kg YOU WANT : "))
        bill = bill + adding_item * 100
        print(f"Added {user} in your cart - your Bill is {bill} $")
        
    elif user == 'banana':
        adding_item=int(input(f" HOW MANY {user} YOU WANT : "))
        bill = bill + adding_item * 20
        print(f"Added {user} in your cart - your Bill is {bill} $")
        
    elif user == 'orange':
        adding_item=int(input(f"{user} HOW MANY kg YOU WANT : "))
        bill = bill + adding_item * 80
        print(f"Added {user} in your cart - your Bill is {bill} $")
        
    elif user == 'laptop':
        adding_item=int(input(f"{user} HOW MANY items YOU WANT : "))
        bill = bill + adding_item * 1000
        print(f"Added {user} in your cart - your Bill is {bill} $")
        
    elif user == 'moblie':
        adding_item=int(input(f"{user} HOW MANY items YOU WANT : "))
        bill = bill + adding_item * 500
        print(f"Added {user} in your cart - your Bill is {bill} $")
        
    elif user == 'headphone':
        adding_item=int(input(f"{user} HOW MANY items YOU WANT : "))
        bill = bill + adding_item * 100
        print(f"Added {user} in your cart - your Bill is {bill} $")
        
    elif user == 'buy':
        # 0 != BILL --> RE-ENTER UNTILL USER GIVE CORRECT-->
        while True:
            
            buy=int(input(f"Your totall amount is {bill} BUY NOW...! = "))
            if buy == bill:
                print("YOUR ORDER IS SUCCESFULLY")
                break
            
            elif buy != bill:
                print("PLEACE GIVE THE ACTUAL AMOUNT , THEN ONLY ORDER WILL CONFORM ")
        
        break


