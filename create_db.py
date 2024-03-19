#!/usr/bin/env python3


from common import connect, disconnect


def create_tutor_table(connection):
    connection.execute('''
                    create table if not exists tutor (
                    id integer primary key,
                    name text not null,
                    faculty integer not null,
                    room integer not null,
                    foreign key (faculty) references faculty(id),
                    foreign key (room) references room(id)
                    )
                    ''')


def create_faculty_table(connection):
    connection.execute('''
                    create table if not exists faculty (
                    id integer primary key,
                    name text not null,
                    dean text not null)
                    ''')


def create_room_table(connection):
    connection.execute('''
                    create table if not exists room (
                    id integer primary key,
                    number text not null,
                    building text not null)
                    ''')


def zap_database(connection):
    connection.execute('drop table if exists tutor')
    connection.execute('drop table if exists faculty')
    connection.execute('drop table if exists room')


def create_new_database():
    con = connect()

    zap_database(con)

    create_faculty_table(con)
    create_room_table(con)
    create_tutor_table(con)

    disconnect(con)


if __name__ == '__main__':
    create_new_database()
