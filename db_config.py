import os
import mysql.connector
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Debugging: Print loaded environment variables
print("Loaded Environment Variables:")
print("MYSQLHOST:", os.getenv("MYSQLHOST"))
print("MYSQLUSER:", os.getenv("MYSQLUSER"))
print("MYSQLPASSWORD:", os.getenv("MYSQLPASSWORD"))
print("MYSQLDATABASE:", os.getenv("MYSQLDATABASE"))
print("MYSQLPORT:", os.getenv("MYSQLPORT"))

DB_CONFIG = {
    "host": os.getenv("MYSQLHOST"),
    "user": os.getenv("MYSQLUSER"),
    "password": os.getenv("MYSQLPASSWORD"),
    "database": os.getenv("MYSQLDATABASE"),
    "port": int(os.getenv("MYSQLPORT", 3306)),
    "use_pure": True  # Force TCP/IP connection
}

# Test MySQL Connection
def test_db_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        print("✅ Successfully connected to MySQL!")
        conn.close()
    except mysql.connector.Error as e:
        print(f"❌ Database connection failed: {e}")

if __name__ == "__main__":
    test_db_connection()
