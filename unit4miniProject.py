carpet_price = float(input())
room_width = int(input())
room_length = int(input())

room_area = room_width * room_length

carpet_cost = carpet_price * room_area * 1.2

labor_cost = room_area * 0.75

print(f"Room: {room_area} sq ft")
print(f"Carpet: ${carpet_cost:.2f}")
print(f"Labor cost: ${labor_cost:.2f}")