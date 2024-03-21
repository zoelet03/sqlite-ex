#!/usr/bin/env python3

from tabulate import tabulate

from common import connect, disconnect


def tutor_count(connection):
    cur = connection.cursor()

    cur.execute('''
                select count(*)
                from tutor
                ''')

    count = cur.fetchone()

    cur.close()
    connection.commit()

    return count


if __name__ == '__main__':
    con = connect()

    staff_number = tutor_count(con)[0]

    print(f'There {"is" if staff_number == 1 else "are"} {staff_number} tutor'
          f'{"s" if staff_number != 1 else ""} in the database.')

    disconnect(con)
