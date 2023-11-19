import psycopg2
from flask import request
import json
class ItemRepository:

    def __init__(self, connection):
        self.connection = connection

    def load_items(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM my_schema.items")
        items = []
        for row in cursor:
            items.append({
                "SKU": row[0],
                "Name": row[1],
                "Description": row[2],
                "Price": row[3],
                "Quantity": row[4],
                "Expiration Date": row[5]
            })
        return items

    def get_items(self):
        return self.load_items()
    
    def add_item(self, item):
        row = item
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO my_schema.items (sku, name, description, price, quantity,  expiration_date) VALUES (%s, %s, %s, %s, %s, %s)", (row["SKU"], row["Name"], row["Description"], row["Price"], row["Quantity"], row["Expiration Date"]))
        self.connection.commit()
        return "Item added successfully" 
    """
    def add_item(self):
        item_data = request.data
        item = json.loads(item_data.decode('utf-8'))

        row = item
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO my_schema.items (sku, name, description, price, quantity, expiration_date) VALUES (%s, %s, %s, %s, %s, %s)", (row["SKU"], row["Name"], row["Description"], row["Price"], row["Quantity"], row["Expiration Date"]))
        self.connection.commit()

        return "Item added successfully"  """



    def delete_item(self, sku):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM my_schema.items WHERE sku=%s", (sku,))
        self.connection.commit()
        return "Item deleted successfully"
    
    def get_item(self, sku):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM my_schema.items WHERE sku=%s", (sku,))
        row = cursor.fetchone()
        if row:
            return {
                "SKU": row[0],
                "Name": row[1],
                "Description": row[2],
                "Price": row[3],
                "Quantity": row[4],
                "Expiration Date": row[5]
            }
        else:
            return None
