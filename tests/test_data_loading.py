import mysql.connector

def test_mysql_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="churn_db"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM customers;")
    result = cursor.fetchone()[0]
    conn.close()
    assert result > 0, "No data found in customers table!"
