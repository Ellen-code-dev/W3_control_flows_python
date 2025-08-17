# Part 1: Define the function
def calculate_discount(price, discount_percent):
    # If discount is 20% or higher, apply it
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Otherwise return the original price
        return price


# Part 2: Use the function
# Ask the user for inputs
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function
final_price = calculate_discount(price, discount_percent)

# Display result
print(f"The final price is: {final_price}")
