#!/usr/bin/env python3

import sqlite3

from tabulate import tabulate

from common import connect, disconnect


def get_staff_list(connection):
    cur = connection.cursor()

    cur.execute('''
                select t.name, f.name, r.number
                from tutor t, faculty f, room r
                where t.faculty = f.id
                and t.room = r.id
                order by 1
                ''')

    staff_data = cur.fetchall()

    cur.close()
    connection.commit()

    return staff_data


if __name__ == '__main__':
    con = connect()

    try:
        print(tabulate(get_staff_list(con), headers=['Name', 'Faculty', 'Room'], tablefmt='orgtbl'))

    except sqlite3.OperationalError:
        print('Error retrieving list. Most likely database is not created correctly.')

    finally:
        disconnect(con)
