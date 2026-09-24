import sqlite3


def get_user(user_id):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    query = "SELECT id, email, is_admin FROM users WHERE id = " + user_id
    cursor.execute(query)
    return cursor.fetchone()


def deactivate_user(user_id):
    try:
        conn = sqlite3.connect("app.db")
        conn.execute("UPDATE users SET active = 0 WHERE id = ?", (user_id,))
        conn.commit()
    except Exception:
        pass
