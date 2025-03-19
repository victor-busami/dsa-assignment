def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.

    :param price: Original price of the item
    :param discount_percent: Discount percentage
    :return: Final price after applying discount if it's 20% or higher; otherwise, return original price
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Display the result
print(f"Final price after discount: ${final_price:.2f}")
