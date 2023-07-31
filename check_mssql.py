import os

from textwrap import dedent

from sqlalchemy import create_engine, text

MSSQL_ADDRESS = os.environ["MSSQL_ADDRESS"]
MSSQL_PORT = os.environ["MSSQL_PORT"]
MSSQL_USER = os.environ["MSSQL_USER"]
MSSQL_PASSWORD = os.environ["MSSQL_PASSWORD"]
MSSQL_DB = os.environ["MSSQL_DB"]

URI = f"mssql+pymssql://{MSSQL_USER}:{MSSQL_PASSWORD}@{MSSQL_ADDRESS}:{MSSQL_PORT}/{MSSQL_DB}"

engine = create_engine(URI)
conn = engine.connect()

print(f"Connected to {MSSQL_ADDRESS}:{MSSQL_PORT}")

# Create the table
conn.execute(
    text(
        dedent(
            """
            CREATE TABLE IF NOT EXISTS test (
                id INT IDENTITY(1,1) PRIMARY KEY,
                name VARCHAR(50) NOT NULL
            )
            """,
        ),
    ),
)

print("Created table 'test'")

# Insert some data
conn.execute(
    text(
        dedent(
            """
            INSERT INTO test (name) VALUES ('foo')
            INSERT INTO test (name) VALUES ('bar')
            INSERT INTO test (name) VALUES ('baz')
            """,
        ),
    ),
)

print("Inserted data into 'test'")

# Query the data
result = conn.execute(
    text(
        dedent(
            """
            SELECT * FROM test
            """,
        ),
    ),
)

for row in result:
    print(row)
