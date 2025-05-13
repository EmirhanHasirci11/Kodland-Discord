import sqlite3

db_name="discord_tasks.db"

def init_database():
    connection=sqlite3.connect(db_name)
    c = connection.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0
        )
    """)
    connection.commit()
    connection.close()

def add_task(description):
    connection = sqlite3.connect(db_name)
    c= connection.cursor()
    c.execute("INSERT INTO tasks (description) VALUES (?)", (description,))
    task_id = c.lastrowid
    connection.commit()
    connection.close()
    return task_id

def delete_task(task_id):
    connection = sqlite3.connect(db_name)
    c = connection.cursor()
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    changes = c.rowcount
    connection.commit()
    connection.close()
    return changes > 0

def get_tasks(filter_completed=None):
    connection = sqlite3.connect(db_name)
    c = connection.cursor()
    
    if filter_completed is None:
        c.execute("SELECT * FROM tasks")
    else:
        c.execute("SELECT * FROM tasks WHERE completed=?", (int(filter_completed),))
    
    tasks = c.fetchall()
    connection.close()
    return tasks

def get_completed_tasks():
    return get_tasks(filter_completed=True)

def get_uncompleted_tasks():
    return get_tasks(filter_completed=False)

def complete_task(task_id):
    connection = sqlite3.connect(db_name)
    c = connection.cursor()
    c.execute("UPDATE tasks SET completed = 1 WHERE id = ? AND completed = 0", (task_id,))
    changes = c.rowcount
    connection.commit()
    connection.close()
    return changes > 0

