"""
Manually create database tables
Run this if tables aren't being created automatically
"""
import os
import sys
from dotenv import load_dotenv

# Add the backend directory to the path
sys.path.insert(0, os.path.dirname(__file__))

# Load environment variables
load_dotenv()

print("=" * 60)
print("CREATING DATABASE TABLES")
print("=" * 60)

try:
    from src.database import create_db_and_tables, engine
    from sqlalchemy import inspect

    # Create tables
    create_db_and_tables()

    # Verify tables were created
    inspector = inspect(engine)
    tables = inspector.get_table_names()

    print(f"\n[SUCCESS] Tables created successfully!")
    print(f"\n[INFO] Available tables ({len(tables)}):")
    for table in tables:
        print(f"   - {table}")
        # Show columns
        columns = inspector.get_columns(table)
        for col in columns:
            print(f"      * {col['name']} ({col['type']})")

    print("\n" + "=" * 60)
    print("[SUCCESS] TABLE CREATION COMPLETE")
    print("=" * 60)

except Exception as e:
    print(f"\n[ERROR] Error creating tables: {e}")
    print("\n" + "=" * 60)
    print("[FAILED] TABLE CREATION FAILED")
    print("=" * 60)
    import traceback
    traceback.print_exc()
    exit(1)
