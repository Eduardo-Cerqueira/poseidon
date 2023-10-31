import psycopg2

# Connect to database
conn = psycopg2.connect(database="poseidon",
                        host="localhost",
                        user="app",
                        password="password",
                        port="5432")

# Permit database operations
cursor = conn.cursor()


# SELECT
def getAllCustomerFamily():
    cursor.execute("SELECT * FROM customer_family")
    return cursor.fetchall()


# SELECT by id
def getCustomerFamilyById(id):
    cursor.execute("SELECT * FROM customer_family WHERE id = %s", (id,))
    return cursor.fetchall()


# SELECT by code
def getCustomerFamilyByCode(code):
    cursor.execute("SELECT * FROM customer_family WHERE code = %s", (code,))
    return cursor.fetchall()


# INSERT
def insertIntoCustomerFamily(code, description):
    cursor.execute("INSERT INTO customer_family(code,description) VALUES(%s,%s)", (code, description))
    conn.commit()


# UPDATE
def updateCustomerFamily(id, code, description):
    cursor.execute("UPDATE customer_family SET code = %s, description = %s WHERE id = %s", (code, description, id))
    conn.commit()


# DELETE
def deleteCustomerFamily(id):
    cursor.execute("DELETE FROM customer_family WHERE id = %s", (id,))
    conn.commit()


cursor.close()
conn.close()
