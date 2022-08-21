price = float(input("Price: "))
discount = float(input("Discount percentage: "))
price_after_discount = price - (discount * price / 100)
federal_tax = price_after_discount * 0.05
provincial_tax = price_after_discount * 0.1
price_total = price_after_discount + federal_tax + provincial_tax

print(" ")
print(f"Original Price: {price:>8.2f}")
print(f"Discounted Price: {price_after_discount:>8.2f}")
print(f'Federal Tax:{federal_tax:>8.2f}')
print(f'Provincial Tax:{provincial_tax:>8.2f}')
print(f'Total Price: {price_total:>8.2f}')