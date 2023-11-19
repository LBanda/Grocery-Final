import json
import psycopg2
from repository.item_repository import ItemRepository
from flask import request

connection = psycopg2.connect("host=localhost dbname=my_database user=my_user password=my_password")
item_repository = ItemRepository(connection)

class ItemController:


    def __init__(self, item_repository):
        self.item_repository = item_repository

    def get_items(self):
        items = self.item_repository.get_items()
        json_items = []
        for item in items:
            json_item = {
                "SKU": item["SKU"],
                "Name": item["Name"],
                "Description": item["Description"],
                "Price": str(item["Price"]),
                "Quantity": item["Quantity"],
                "Expiration Date": str(item["Expiration Date"])
                }
            json_items.append(json_item)

        return json.dumps(json_items)
    """
    def add_item(self, item_data):
        item = json.loads(item_data)
        self.item_repository.add_item(item)
        return 'Item added successfully' """
    
    def add_item(self):
        item = json.loads(request.data)
        self.item_repository.add_item(item)
        return 'Item added successfully'


    def delete_item(self, sku):
        self.item_repository.delete_item(sku)
        return 'Item deleted successfully'

    def get_item(self, sku):
        item = self.item_repository.get_item(sku)
        if item:
            json_item = {
                "SKU": item["SKU"],
                "Name": item["Name"],
                "Description": item["Description"],
                "Price": item["Price"],
                "Quantity": item["Quantity"],
                "Expiration Date": str(item["Expiration Date"])
            }
            return json.dumps(json_item)
        else:
            return 'Item not found'

    def convert_currency(self, sku, currency):
        item = self.item_repository.get_item(sku)
        if item:
            exchange_rate_url = f"http://api.exchangeratesapi.io/v1/latest?access_key=6aa9ad73dc0b72c4d4fb809216daca2f&symbols={currency}"
            response = request.get(exchange_rate_url)
            exchange_rate_data = json.loads(response.content)

            exchange_rate = exchange_rate_data["rates"][currency]
            converted_price = item["Price"] * exchange_rate

            return json.dumps({
                "SKU": item["SKU"],
                "Name": item["Name"],
                "Description": item["Description"],
                "Price": str(converted_price),
                "Quantity": item["Quantity"],
                "Expiration Date": str(item["Expiration Date"])
            })
        else:
            return 'Item not found' 

