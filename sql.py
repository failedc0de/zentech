import sqlite3

db = sqlite3.connect('user.db')
sql = db.cursor()

def reg_bd():
    sql.execute(""" CREATE TABLE IF NOT EXISTS users (
                    chat_id,
                    username,
                    first_name,
                    password,
                    string_session
                    ) """)
    db.commit()

reg_bd()
