total_sales = 0
carpet_price = float(input())
room_width = int(input())
room_length = int(input())

room_area = room_width * room_length

carpet_cost = carpet_price * room_area * 1.2

labor_cost = room_area * 0.75

tax_rate = 0.07
sales_tax = (carpet_cost + labor_cost) * tax_rate

total_cost = carpet_cost + labor_cost + sales_tax

print("Order #1")
print(f"Room: {room_area} sq ft")
print(f"Carpet: ${carpet_cost:.2f}")
print(f"Labor: ${labor_cost:.2f}")
print(f"Tax: ${sales_tax:.2f}")
print(f"Cost: ${total_cost:.2f}\n")

total_sales = total_sales + total_cost

carpet_price = float(input())
room_width = int(input())
room_length = int(input())

room_area = room_width * room_length

carpet_cost = carpet_price * room_area * 1.2

labor_cost = room_area * 0.75

sales_tax = (carpet_cost + labor_cost) * tax_rate

total_cost = carpet_cost + labor_cost + sales_tax

print("Order #2")
print(f"Room: {room_area} sq ft")
print(f"Carpet: ${carpet_cost:.2f}")
print(f"Labor: ${labor_cost:.2f}")
print(f"Tax: ${sales_tax:.2f}")
print(f"Cost: ${total_cost:.2f}\n")

total_sales = total_sales + total_cost

carpet_price = float(input())
room_width = int(input())
room_length = int(input())

room_area = room_width * room_length

carpet_cost = carpet_price * room_area * 1.2

labor_cost = room_area * 0.75

sales_tax = (carpet_cost + labor_cost) * tax_rate

total_cost = carpet_cost + labor_cost + sales_tax

print("Order #3")
print(f"Room: {room_area} sq ft")
print(f"Carpet: ${carpet_cost:.2f}")
print(f"Labor: ${labor_cost:.2f}")
print(f"Tax: ${sales_tax:.2f}")
print(f"Cost: ${total_cost:.2f}\n")

total_sales = total_sales + total_cost

print(f"Total Sales: ${total_sales: .2f}")