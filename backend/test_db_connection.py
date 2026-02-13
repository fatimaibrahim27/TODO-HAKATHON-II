"""
Database connection test script
Run this to verify your Neon PostgreSQL connection works
"""
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

print("=" * 60)
print("DATABASE CONNECTION TEST")
print("=" * 60)

if not DATABASE_URL:
    print("[ERROR] DATABASE_URL not found in .env file")
    exit(1)

# Show sanitized URL (hide password)
if "@" in DATABASE_URL:
    parts = DATABASE_URL.split("@")
    user_part = parts[0].split("://")[1].split(":")[0]
    host_part = "@".join(parts[1:])
    sanitized_url = f"postgresql://{user_part}:****@{host_part}"
else:
    sanitized_url = DATABASE_URL

print(f"\n[INFO] Connecting to: {sanitized_url}\n")

try:
    # Create engine
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)

    # Test connection
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        version = result.fetchone()[0]
        print("[SUCCESS] Connection successful!")
        print(f"\n[INFO] PostgreSQL version:\n{version}\n")

        # Check if tables exist
        result = conn.execute(text("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
            ORDER BY table_name;
        """))
        tables = result.fetchall()

        if tables:
            print(f"[INFO] Existing tables ({len(tables)}):")
            for table in tables:
                print(f"   - {table[0]}")
        else:
            print("[INFO] No tables found (will be created on server startup)")

    print("\n" + "=" * 60)
    print("[SUCCESS] DATABASE CONNECTION TEST PASSED")
    print("=" * 60)

except Exception as e:
    print(f"\n[ERROR] Connection failed!")
    print(f"\nError: {str(e)}\n")
    print("=" * 60)
    print("[FAILED] DATABASE CONNECTION TEST FAILED")
    print("=" * 60)
    print("\nTroubleshooting:")
    print("1. Check your DATABASE_URL in backend/.env")
    print("2. Ensure your Neon database is active")
    print("3. Verify your IP is allowed in Neon dashboard")
    print("4. Check if psycopg2-binary is installed: pip install psycopg2-binary")
    exit(1)
