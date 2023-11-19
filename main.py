import flask
from controller.item_resource import ItemController
from repository.item_repository import ItemRepository
import psycopg2
from flask import render_template, request, redirect
import json

connection = psycopg2.connect("host=localhost dbname=my_database user=my_user password=my_password")

item_repository = ItemRepository(connection)
item_controller = ItemController(item_repository)

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def show_items():
    items = item_repository.get_items()
    return render_template('index.html', items=items)

@app.route('/item/<sku>/convert?currency=<currency>', methods=['GET'])
def convert_currency(sku, currency):
    return item_controller.convert_currency(sku, currency)


@app.route('/item', methods=['GET'])
def get_items():
    return item_controller.get_items()

@app.route('/item', methods=['POST'])
def add_item():
    #item_data = json.loads(request.data)
    #item_repository.add_item(item_data)
    return item_controller.add_item()
    #return redirect('/item/add')

@app.route('/item/<sku>', methods=['DELETE'])
def delete_item(sku):
    item_repository.delete_item(sku)
    return redirect('/')

@app.route('/item/add', methods=['GET'])
def add_item_view():
    return render_template('add_item.html')

@app.route('/item/<sku>/edit', methods=['GET'])
def edit_item_view(sku):
    item = item_repository.get_item(sku)
    if item:
        return render_template('edit_item.html', item=item)
    else:
        return 'Item not found'

@app.route('/item/<sku>/delete', methods=['GET'])
def delete_item_view(sku):
    item = item_repository.get_item(sku)
    if item:
        return render_template('delete_item.html', item=item)
    else:
        return 'Item not found'    

if __name__ == '__main__':
    app.run(debug=True)
