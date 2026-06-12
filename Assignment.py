users ={
    "admin":("admin123","Admin"),
    "alice":("alice456","Customer"),
    "bob":("bob789","Cashier") 
}

#tax rates by location 
tax_rates = {
    "KAMPALA": 0.18,
    "JINJA": 0.17,
    "MBARARA": 0.175,
    "GULU":0.16,
    "MBALE":0.165
}

coupons = {
"SAVE10":0.10,
"SAVE20":0.20,
"WELCOME5":0.05
}


#LOGIN SYSTEM
print("E-COMMERCE PLATFORM")
username = input("Enter your username: ")
password = input("Enter your password: ")

if username in users and users[username][0] == password:
    role = users[username][1]
    print(f"\nWelcome, {username}! You are logged in as {role}.\n")

    #price calculation
    #inputs
    subtotal = float(input("Enter the subtotal amount: "))   
    location = input("Enter your location (KAMPALA, JINJA, MBARARA, GULU, MBALE): ").upper()
    coupon_code = input("Enter a coupon code (if any or press enter to skip): ").upper().strip()
    if coupon_code == "":
        coupon_code = None

    #level one: discount based on subtotal
    if subtotal >= 200000:
        discount_rate = 0.10
    elif subtotal >= 100000:
        discount_rate = 0.05
    elif subtotal >= 50000:
        discount_rate = 0.02
    else:
        discount_rate = 0.0
    price_after_subtotal_discount = subtotal * (1 - discount_rate)
    print(f"Subtotal discount: {discount_rate*100}% -> UGX {price_after_subtotal_discount:.2f}")

    #level two:coupon code handling(nested if)
    if coupon_code:
        if coupon_code in coupons:
            coupon_discount = coupons[coupon_code]
            price_after_coupon = price_after_subtotal_discount * (1 - coupon_discount)
            print(f"Coupon '{coupon_code}' valid: {coupon_discount*100}% off -> UGX {price_after_coupon:,.2f}")
        else:
            print(f"Invalid coupon '{coupon_code}'. No extra discount .")
            price_after_coupon = price_after_subtotal_discount
    else:    
        price_after_coupon = price_after_subtotal_discount

    #level three: tax calculation based on location
    if location in tax_rates:
        tax = price_after_coupon * tax_rates[location]
        final_price = price_after_coupon + tax
        print(f"Location: {location}  tax rate: {tax_rates[location]*100}% -> Tax =UGX {tax:,.2f}")
    else:
        print(f"Location '{location}' not recognized. Using default 18% VAT.")
        tax = price_after_coupon * 0.18
        final_price = price_after_coupon + tax
        print(f"\n FINAL PRICE = UGX {final_price:,.2f}")

    #role based access
    if role == "Admin":
        print("\nAdmin extra features nested inside role check.")
        modify = input("Do you want to modify tax rates or add coupon? (yes/no): ").lower()
        if modify == "yes":
            choice = input("Type 'tax' to modify tax rates or 'coupon' to add a coupon: ").lower()
            if choice == "tax":
                new_loc = input("District code:").upper()
                new_rate = float(input("New tax rate (decimal, e.g., 0.18): "))
                tax_rates[new_loc] = new_rate
                print(f"Tax rate for {new_loc} updated to {new_rate*100}%")
            elif choice == "coupon":
                new_code = input("New coupon code:").upper()
                new_disc = float(input("Discount decimal: "))
                coupons[new_code] = new_disc
                print(f"Coupon {new_code} added with {new_disc*100}% discount.")
            else:
                print("Invalid choice.")
        else:
            print("No modifications made.")
    elif role == "Cashier":
        print("\ncashier note")
        print("Cashier can recalculate price for another customer")
    else:
        print("\nCustomer note")
        print("Thank you for shopping with us.")
else:
    print("login failed.invalid username or password")

