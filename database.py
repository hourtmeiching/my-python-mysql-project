from db_config import DB_CONFIG
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

# Create a Table for Storing Users
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE
    )
""")
print("✅ Table 'users' created successfully!")

# Insert Data
def insert_user(name, email):
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        print(f"✅ User {name} added successfully!")
    except mysql.connector.Error as e:
        print(f"❌ Error inserting user: {e}")

# Test Insert
insert_user("John Doe", "johndoe@example.com")

cursor.close()
conn.close()
