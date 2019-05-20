#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This will load the database from schema.sql"""

import sqlite3


def main():
    conn = sqlite3.connect('booklibrary.db')
    f = open('schema.sql', 'r')
    sql = f.read()
    conn.executescript(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
