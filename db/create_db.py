import sqlite3


def create_db(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        # cursor.execute("CREATE TABLE IF NOT EXISTS " + tableName + "(TaskID integer, Description text, PRIMARY KEY("
        #  "TaskID))")

        cursor.execute("""CREATE TABLE Tasks(
                            TaskID integer,
                            Description text,
                            PRIMARY KEY(TaskID));""")
        db.commit()
