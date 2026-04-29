import uuid
from typing import List, Dict, Optional

#Query 1: Place a new order for an item and quantity

#Query 2: View all orders placed for a particular item

#Query 4: find how many orders placed for the item using item id

class OrderManagement:
    def __init__(self, inventory_items : List[Dict],order: List[Dict]) -> None:
        self.inventory_items = inventory_items
        self.orders = orders

    def place_order(self, item_id : str, quantity : int) -> Optional[Dict]:
        #find item and check the existing inventory for the item
        item = self.find_inventory_item_by_item_id(item_id)
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
            self.orders.append(new_order)
            return new_order 
            # if we have enough inventory then reduce the inventory
            # then place the order

        pass

    def find_item_names(self) -> List:
        item_names = []
        for item in inventory:
            item_names.append(item['name'])
        return item_names


    def find_orders_by_item_id(self):
        pass

    def count_orders_by_item_id(self):
        pass

    def find_inventory_item_by_item_id(self, item_id: str):
        for item in self:
            if item['id'] == item_id:
                return item
        
        return None

    def update_inventory_item(self):
        pass

    def add_new_item_to_inventory(self):
        pass

    def update_inventory_item(self):
        pass

    def cancel_order(self):
        pass