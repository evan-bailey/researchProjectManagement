#!/usr/bin/python

"""
Script to save and retrieve project metadata for multiple projects
"""


import sqlite3
from sqlite3 import Error


class metaDB(object):
    """
    Object class to generate the metadata database and interact with it.
    Requires a directory as input, which is where the database will be built.
    Default database name for metadata is meta.db
    """

    def __init__(self, db_dir):
        self.db_dir = db_dir
        self.filename = 'meta.db'
        self.full_path = self.db_dir + self.filename
        self.project = ""
        self.project_dir = ""

    def create_connection(self):
        """
        Create a database connection to the SQLite database
        specified by db_file
        :param full_path: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(self.full_path)
        except Error as conn_err:
            print(conn_err)

        return conn

    def is_sqlite3_db(self):
        """
        Check existence of database
        :param full_path: path to database
        :return: True or False
        """

        from os.path import isfile, getsize

        if not isfile(self.full_path):
            return False

        if getsize(self.full_path) < 100:
            return False
            # SQLite DB header is 100 bytes

        with open(self.full_path, 'rb') as file_d:
            header = file_d.read(100)

        return header[:16] == 'SQLite format 3\x00'
        # returns true if SQLite format 3

    def init_db(self):
        """
        Generate database if not present
        :param full_path: path to database
        :return: confirmation message
        """
        if not self.full_path.isSQLite3_db():
            print("Generating database for project metadata")

            meta_db = create_connection(self, self.full_path)
            cursor = meta_db.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS project_metadata
                           (Name TEXT, Directory TEXT, Date TEXT,
                           Project_ID INTEGER)''')
            meta_db.commit()
            meta_db.close()

        else:
            print("Project metadata database found")

    def write_metadata(conn, project_data):
        """
        Write project metadata to database
        :param conn: connection object from create_connection()
        :param project_data: project_data (list with 4 elements)
        :return:
        """

        cursor = conn.cursor()

        sql = '''INSERT INTO project_metadata(Name,Directory,Date,Project_ID)
                          VALUES(?,?,?,?)'''

        cursor.execute(sql, project_data)
        conn.commit()

        return cursor.lastrowid

# TO DO: generate a table for project metadata
