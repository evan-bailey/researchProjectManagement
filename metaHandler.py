#!/usr/bin/python

#Script to save and retrieve project metadata for multiple projects

import os, pathlib, sqlite3
from sqlite3 import Error

#create an object class to generate the metadata database
class metaDB(object):
    #as input requires the directory for the db (Define in cli.py)
    #default name is 'meta.db'
    def __init__(self, db_dir):
        self.db_dir = db_dir
        self.filename = 'meta.db'
        self.full_path = self.db_dir + self.filename
        self.project = ""
        self.project_dir = ""

    def create_connection(full_path):
        """
        Create a database connection to the SQLite database
        specified by db_file
        :param full_path: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(full_path)
        except Error as e:
            print(e)

        return conn

    def isSQLite3_db(full_path):
        """
        Check existence of database
        :param full_path: path to database
        :return: True or False
        """

        from os.path import isfile, getsize

        if not isfile(full_path):
            return False

        if getsize(full_path) < 100 #SQLite DB header is 100 bytes
            return False

        with open(full_path, 'rb') as fd:
            header = fd.read(100)

        return header[:16] == 'SQLite format 3\x00' #returns true if SQLite format 3

    #initiate a database if no meta.db sqlite3 file is found
    def init_db(full_path):
        """
        Generate database if not present
        :param full_path: path to database
        :return: confirmation message
        """
        if not full_path.isSQLite3_db():
            print("Generating database for project metadata")

            meta_db = create_connection(full_path)
            cursor = meta_db.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS project_metadata
                           (Name TEXT, Directory TEXT, Date TEXT, Project_ID INTEGER)''')
            meta_db.commit()
            meta_db.close()

        elif:
            print("Project metadata database found")

    #function to write project metadata to the database table
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







#TO DO: generate a table for project metadata
#.
