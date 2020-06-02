from sqlalchemy import create_engine

engine = ("mysql+mysqlconnector://root:74Q50c$0rIZ&GDhp@localhost:3306/stocks", echo=False)

# Create table
engine.execute("""CREATE TABLE emp (
id INTEGER PRIMARY KEY,
name VARCHAR(50)
)""")

# Insert data (connectionless execution (via engine))
engine.execute("INSERT INTO emp (name) VALUES (:name)", name="Slavo")
engine.execute("INSERT INTO emp (name) VALUES (:name)", name="Jano")
engine.execute("INSERT INTO emp (name) VALUES (:name)", name="Vlado")

# Query data
result = engine.execute("select id, name from emp")
rows = result.fetchall()
result.close(); # should be done automatically

# Display data
for row in rows: # we could also iterate directly over result without need to call fetchall()
    print("DATA: " + repr(row))

print("done")

