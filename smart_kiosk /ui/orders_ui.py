import streamlit as st
from services import kiosk_services


def add_new_order_render():
    inventory = st.session_state['inventory']
    orders = st.session_state['orders']

    item_names = kiosk_services.find_item_names(inventory)
    item_name = st.selectbox('Item', item_names, key = "select_item")
    quantity = st.text_input("Quantity", key = 'quantity_new_order"')

    if st.button("Save Order", key = "new_order", use_container_width = True):
        with st.spinner("saving..."):

            item_id = None
            for item in inventory:
                if item["name"] == item_name:
                    item_id = item["item_id"]
                    break

            new_order = kiosk_services.place_order(inventory, str(item_id), int(quantity), orders)
            st.success(f"new order {new_order['order_id']} is placed.")
