import flask
from controller.item_resource import ItemController
from repository.item_repository import ItemRepository
import psycopg2

# Conexión a la base de datos PostgreSQL
connection = psycopg2.connect("host=localhost dbname=my_database user=my_user password=my_password")

# Instanciación del repositorio y controlador
item_repository = ItemRepository(connection)
item_controller = ItemController(item_repository)

# Configuración de la aplicación Flask
app = flask.Flask(__name__)

# Rutas del REST API

@app.route('/item/<sku>/convert?currency=<currency>', methods=['GET'])
def convert_currency(sku, currency):
    return item_controller.convert_currency(sku, currency)


@app.route('/item', methods=['GET'])
def get_items():
    return item_controller.get_items()

@app.route('/item', methods=['POST'])
def add_item():
    return item_controller.add_item()

@app.route('/item/<sku>', methods=['DELETE'])
def delete_item(sku):
    return item_controller.delete_item(sku)
    

# Ejecución de la aplicación
if __name__ == '__main__':
    app.run(debug=True)
