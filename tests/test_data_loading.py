import pytest


def test_mysql_connection():
# Import inside the test so that CI environments without mysql-connector-python skip the test
try:
import mysql.connector
except ModuleNotFoundError:
pytest.skip("mysql.connector not installed in CI environment")


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
