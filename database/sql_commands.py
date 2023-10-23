import sqlite3
from database import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()


    def sql_create_tables(self):
        if self.connection:
            print("Database connected successfully")

        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_BAN_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_USER_FORM_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_LIKE_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_DISLIKE_TABLE_QUERY)
        self.connection.commit()

    def sql_insert_user_query(self, telegram_id, username, first_name, last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, telegram_id, username, first_name, last_name,)
        )
        self.connection.commit()

    def sql_select_all_user_query(self):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            "telegram_id": row[1],
            "username": row[2],
            "first_name": row[3],
            "last_name": row[4],
        }
        return self.cursor.execute(
            sql_queries.SELECT_ALL_USERS_QUERY,
        ).fetchall()

    def sql_insert_ban_user_query(self, telegram_id, username):
        self.cursor.execute(
            sql_queries.INSERT_BAN_USER_QUERY,
            (None, telegram_id, username, 1)
        )
        self.connection.commit()

    def sql_update_ban_user_query(self, telegram_id):
        self.cursor.execute(
            sql_queries.UPDATE_BAN_USER_COUNT_QUERY,
            (telegram_id,)
        )
        self.connection.commit()

    def sql_select_user_query(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            "telegram_id": row[1],
            "username": row[2],
            "first_name": row[3],
            "last_name": row[4],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_QUERY,
            (telegram_id,)
        ).fetchall()

    def sql_select_ban_users(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            "telegram_id": row[1],
            "username": row[2],
            "count": row[3]
        }
        return self.cursor.execute(
            sql_queries.SELECT_BAN_USER,
            (telegram_id,)
        ).fetchall()

    def sql_insert_user_form_query(self, telegram_id, nickname,
                                   bio, age, occupation, budget, photo):
        self.cursor.execute(
            sql_queries.INSERT_USER_FORM_QUERY,
            (None, telegram_id, nickname, bio, age, occupation, budget, photo)
        )
        self.connection.commit()

    def sql_select_user_form_query(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "bio": row[3],
            "age": row[4],
            "occupation": row[5],
            "budget": row[6],
            "photo": row[7],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_FORM_QUERY,
            (telegram_id,)
        ).fetchall()

    def sql_select_all_user_form_query(self):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "bio": row[3],
            "age": row[4],
            "occupation": row[5],
            "budget": row[6],
            "photo": row[7],
        }
        return self.cursor.execute(
            sql_queries.SELECT_ALL_USERS_FORM_QUERY,
        ).fetchall()

    def sql_insert_like_query(self, owner, liker):
        self.cursor.execute(
            sql_queries.INSERT_LIKE_QUERY,
            (None, owner, liker,)
        )
        self.connection.commit()

    def sql_insert_dislike_query(self, owner, disliker):
        self.cursor.execute(
            sql_queries.INSERT_DISLIKE_QUERY,
            (None, owner, disliker,)
        )
        self.connection.commit()

    def sql_delete_form_query(self, owner):
        self.cursor.execute(
            sql_queries.DELETE_USER_FORM_QUERY,
            (owner,)
        )
        self.connection.commit()

    def sql_update_user_form_query(self, nickname, bio, age, occupation, budget, photo, telegram_id):
        self.cursor.execute(
            sql_queries.UPDATE_USER_FORM_QUERY,
            (nickname, bio, age, occupation, budget, photo, telegram_id,)
        )
        self.connection.commit()

    def get_liked_users(self, liker_telegram_id):
        liked_users = []
        self.cursor.execute(
            sql_queries.SELECT_LIKED_USER,
            (liker_telegram_id,)
        )
        rows = self.cursor.fetchall()
        for row in rows:
            liked_users.append(row[0])
        return liked_users

    def get_disliked_users(self, disliker_telegram_id):
        disliked_users = []
        self.cursor.execute(
            sql_queries.SELECT_DISLIKED_USER,
            (disliker_telegram_id,)
        )
        rows = self.cursor.fetchall()
        for row in rows:
            disliked_users.append(row[0])
        return disliked_users