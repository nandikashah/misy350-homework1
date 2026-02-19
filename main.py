inventory = [
{"item_id": 1, "name": "Espresso", "unit_price": 2.50, "stock": 40},
{"item_id": 2, "name": "Latte", "unit_price": 4.25, "stock": 25},
{"item_id": 3, "name": "Cold Brew", "unit_price": 3.75, "stock": 30},
{"item_id": 4, "name": "Mocha", "unit_price": 4.50, "stock": 20},
{"item_id": 5, "name": "Blueberry Muffin", "unit_price": 2.95, "stock": 18},
]

orders = [
    {"order_id" : "order_101", "item_id" : 2, "quantity" : 2, "status" : "placed", "total": 8.50},
    {"order_id" : "order_102", "item_id" : 3, "quantity" : 1, "status" : "placed", "total": 3.75}
]

#CREATE
#Query 1: Place a new order for an item and quantity.

#INPUT
item_id = int(input("Enter the Item ID to order: "))
quantity = int(input("Enter the quantity: "))

#PROCESS: find item ID and quantity in order, then remove a found item from stock and calculate the price
selected_item = None 

for inventory_item in inventory:
    if inventory_item["item_id"] == item_id:
        selected_item = inventory_item
        print("Item exists!")
        break

if selected_item is None:
        print("Item does not exist.")

if selected_item["stock"] < quantity:
    print("Not enough stock!")

else:
    selected_item["stock"] -= quantity
    total_price = quantity * selected_item["unit_price"]
    new_order_number = 101 + len(orders)
    new_order_id = f"order_{new_order_number}"

    new_order = {
        "order_id": new_order_id,
        "item_id": item_id,
        "quantity": quantity,
        "status": "Placed",
        "total": total_price
    }

    orders.append(new_order)

#OUTPUT
    print("Order successfully placed!")
    print(f"Order ID: {new_order_id}")
    print(f"Item: {selected_item['name']}")
    print(f"Quantity: {quantity}")
    print(f"Total: ${total_price:.2f}")

#READ
#Query 2: View all orders placed for a particular item -- prompt user to enter the item name

#INPUT
search_item = input("Enter the item name to search (e.g. 'Latte'): ")

#PROCESS: find items in search inside inventory
search_item_id = None

for item in inventory:
     if item['name'].lower() == search_item.lower():
          search_item_id = item['item_id']
          break
     
if search_item_id is None:
     print("Item not found.")

else:
    print(f"Order for {search_item}: ")

    orders_found = False
     
    for order in orders:
        if order['item_id'] == search_item_id:
            print(f"Order ID: {order['order_id']}, Quantity: {order['quantity']}, Status: {order['status']}, Total: {order['total']}")
            orders_found = True

    if orders_found is False:
         print("No orders found.")


#Query 3: Calculate and print the total number of orders placed for "Cold Brew"

#INPUT
order_count = 0
cold_brew_id = None

#PROCESS: find items and orders with Cold Brew
for item in inventory:
     if item["name"] == "Cold Brew":
          cold_brew_id = item['item_id']
          break
     
if cold_brew_id != None:
     for order in orders:
          if order["item_id"] == cold_brew_id:
               order_count += 1

else:
     print("Cold Brew not found in inventory.")

#OUTPUT
print(f"Total orders placed for Cold Brew: {order_count}")

#UPDATE
#Query 4: Update item stock quantity by item ID.

#INPUT
item_id = int(input("Enter ID of item to update: "))
new_stock = int(input("Enter new stock quantity: "))

#PROCESS: Validate and update stock
found = False

for item in inventory:
     if item_id == item['item_id']:
          item['stock'] = new_stock
          found = True
          break

#OUTPUT
if found:
     print('Stock updated successfully!')
else:
     print('Item ID not found.')

#REMOVE/DELETE
#Query 5: Cancel an order (and restore stock) using the steps below;

#INPUT
cancel_order_id = input('Enter Order ID to cancel: ')

#PROCESS: Cancel order
order_found = False

for order in orders:
     if order['order_id'] == cancel_order_id:
          order_found = True
          order['status'] = 'cancelled'

for item in inventory:
            if item['item_id'] == order['item_id']:
                item['stock'] += order['quantity']
                break

#OUTPUT
if order_found:
    print("Order cancelled successfully!")
else:
    print('Order not found.')