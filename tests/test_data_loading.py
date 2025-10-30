import pytest
import mysql.connector

def test_mysql_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="yourpassword",
            database="churn_db"
        )
        assert conn.is_connected()
    except mysql.connector.Error:
        pytest.skip("MySQL not available in CI environment")
