import sqlite3
import time
from datetime import datetime
import json


class DB:
    def __init__(self, drop=False):
        self.conn = sqlite3.connect('database.sqlite3')
        self.cur = self.conn.cursor()

        if drop:
            self.cur.execute("drop table saves")
            self.conn.commit()

        # create the table with saves
        self.cur.execute("""create table if not exists saves (
        id integer primary key AUTOINCREMENT,
        last_time DATETIME,
        level_count integer,
        difficulty integer,
        level_asset text,
        last_room_id integer,
        coord_x integer,
        coord_y integer,
        terminals_completed integer,
        health integer,
        inventory string
        )""")
        self.conn.commit()

    def create_save(self, level_asset: str):
        try:
            level_asset = json.dumps(level_asset)
            self.cur.execute(f"""insert into saves (
            last_time,
            level_count,
            difficulty,
            level_asset,
            last_room_id,
            coord_x,
            coord_y,
            terminals_completed,
            health,
            inventory
            ) values (
            {', '.join(['?'] * 10)}
            )""", (datetime.now(), 0, 1, level_asset, 1, 200, 200, 0, 3, '',))
            self.conn.commit()
        except Exception as e:
            print(f'DB -> Error in create_save()\n{e}')

    def get_save_ids(self):
        try:
            data = [el[0] for el in self.cur.execute("""select id from saves""").fetchall()]
            return data
        except Exception as e:
            print(f'DB -> Error in get_save_ids()\n{e}')

    def get_save_info_by_id(self, id: int):
        try:
            data = self.cur.execute(
                """select id, last_time, level_count from saves where id=?""", (id,)).fetchone()
            return data
        except Exception as e:
            print(f'DB -> Error in get_save_info_by_id()\n{e}')

    def get_all_save_info_by_id(self, id: int):
        try:
            data = self.cur.execute(
                """select * from saves where id=?""", (id,)).fetchone()
            return data
        except Exception as e:
            print(f'DB -> Error in get_save_info_by_id()\n{e}')

    def update_completed_terminal_in_save(self, terminal_completed, level_asset, save_id):
        try:
            self.cur.execute("""update saves set terminals_completed=?, level_asset=? where id=?""",
                             (terminal_completed, json.dumps(level_asset), save_id))
            self.conn.commit()
        except Exception as e:
            print(f'DB -> Error in update_completed_terminal_in_save()\n{e}')


db = DB()
