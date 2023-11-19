import psycopg2
import csv



def main():
    connection = psycopg2.connect("host=localhost dbname=my_database user=my_user password=my_password")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE my_schema.items (sku VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, description VARCHAR(255) NOT NULL, price DECIMAL(10,2) NOT NULL, quantity INT NOT NULL, expiration_date DATE NOT NULL)")

    reader = csv.DictReader(open('D:/Documentos/docs/arqui/Grocery-Final/model/sample_grocery.csv', 'r'))
    for row in reader:
        cursor.execute("INSERT INTO my_schema.items (sku, name, description, price, quantity,  expiration_date) VALUES (%s, %s, %s, %s, %s, %s)", (row["SKU"], row["Name"], row["Description"], row["Price"], row["Quantity"], row["Expiration Date"]))

    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()
