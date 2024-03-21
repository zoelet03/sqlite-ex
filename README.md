# sqlite-example

Simple example of using:

* SQLite
* Python's DB API - via PySqlite3
* The ``tabulate`` package from PyPi

To run:

1. Create the database with ``populate_db.py``
2. Display the staff list with ``staff_list.py``

The above will create and populate the database, then pull the staff data from the database, and display 
it in a neatly formatted list via ``tabulate``.

To install ``tabulate``:

    $ pip install -r requirements.txt

ideally in a virtual environment. 

Details on changing the table format are in the docs for ``tabulate``, here: https://pypi.org/project/tabulate/ .

Note than on opening the project in PyCharm for the 
first time it will spot the ``requirements.txt`` and offer to create the Venv, install the dependency,
configure the interpreter, and so on.

For convenience, a copy of ``sqlite3.exe`` (the command-line tool for accessing an SQLite database on Windows) is included
in the repo. This is version 3.45.2. Newer versions may be found at https://sqlite.org/download.html . Docs on 
its use are at https://sqlite.org/cli.html .
