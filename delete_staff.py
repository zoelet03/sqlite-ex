#!/usr/bin/env python3

import sqlite3

from common import connect, disconnect

if __name__ == '__main__':

    con = connect()

    id = int(input('Enter id to delete: '))

    cur = con.cursor()

    try:
        cur.execute('''
                    delete from tutor
                    where id = ?
                    ''', (id,))

    except sqlite3.OperationalError:
        print('Error deleting. Most likely database is not created correctly.')

    finally:
        cur.close()
        con.commit()

        disconnect(con)

