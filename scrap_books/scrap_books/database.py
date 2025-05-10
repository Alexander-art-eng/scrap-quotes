import sqlite3

connection = sqlite3.connect('quotes.db')
cursor = connection.cursor()

cursor.execute(
    """create table if not exists quotes_table(
        title text,
        author text,
        tags text
        )"""
)

cursor.execute(
    """
        insert into quotes_tables
        values ()
    """
)
connection.commit()
connection.close()
