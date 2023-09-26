import unittest
import sqlite3
import os


class TestSQLiteConnection(unittest.TestCase):
    def test_connection(self):
        conn = sqlite3.connect("pythonproject/src/data/happiness_database.db")
        self.assertIsNotNone(conn)
        conn.close()


if __name__ == "__main__":
    unittest.main()
