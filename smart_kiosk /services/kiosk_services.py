import uuid
from typing import List, Dict, Optional

#Query 1: Place a new order for an item and quantity

#Query 2: View all orders placed for a particular item

#Query 4: find how many orders placed for the item using item id

def place_order(inventory_items : list, item_id : str, quantity : int, orders : list) -> Optional[Dict]:
    #find item and check the existing inventory for the item
    item = find_inventory_item_by_item_id(inventory_items, item_id)
    if item:
        if item['stock'] >= quantity:
            item['stock'] = item['stock'] - quantity #reduce stock
            total = quantity * item['unit_price']

            #create new order dict
            new_order = {
                "order_id" : str(uuid.uuid4()),
                "item_id" : item_id,
                "quantity" : quantity,
                "status" : "placed",
                "total": total
            }
        #add the new order to the orders
            
        # if we have enough inventory then reduce the inventory
        # then place the order

    pass

def find_item_names(inventory: List) -> List:
    item_names = []
    for item in inventory:
        item_names.append(item['name'])
    return item_names


def find_orders_by_item_id():
    pass

def count_orders_by_item_id():
    pass

def find_inventory_item_by_item_id(inventory_list: list, item_id: str):
    for item in inventory_list:
        if item['id'] == item_id:
            return item
    
    return None

def update_inventory_item():
    pass

def add_new_item_to_inventory():
    pass

def update_inventory_item():
    pass

def cancel_order():
    pass