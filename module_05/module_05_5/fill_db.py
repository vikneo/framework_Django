# -*- coding: utf-8 -*-

import os
import sqlite3
from random import choice, randint
from datetime import datetime


class TableBase:

    @staticmethod
    def connect_to_base():
        try:
            with sqlite3.connect(path) as client:
                return client
        except Exception as err:
            f'не удалось подключится к базе. Описание: {err}'

    @staticmethod
    def insert_to_base(client, response, data) -> None:
        try:
            cur = client.cursor()
            cur.execute(f"""{response}""", data)
            client.commit()
        except Exception as er:
            print(er)
            raise ValueError(f'Не удалось вставить данные в базу. Описание: {er}')


table = TableBase()

date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
path = os.path.abspath(os.path.join('board/db.sqlite3'))
list_announce = {'Продам': 'Мотоцикл', 'Сдам': 'Квартиру', 'Услуги': 'Выведение из запоя',
                 'Транспорт': 'Перевезу грузы', 'Недвижимость': 'Куплю Дом', 'Разное': 'Приму в дар кота',
                 'Бытовая техника': 'Ремонт стиральных машин', 'Оргтехника': 'Принтеры, копиры'}

_client = table.connect_to_base()

for i in range(3000, 500000):
    key = list_announce.keys()
    _select = choice(list(key))
    try:
        table.insert_to_base(_client, "INSERT INTO advertisements (id, title, descriptions, created_at, "
                                      "updated_at, price, view_count) VALUES (?, ?, ?, ?, ?, ?, ?)",
                             data=(i, _select, list_announce[_select], date, date, randint(500, 2000), 0))
    except Exception:
        print(f'Не удалось вставить данные в базу')
        break
else:
    print('Данные вставлены')
