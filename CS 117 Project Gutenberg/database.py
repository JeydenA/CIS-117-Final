"""
database.py
Handles database creation and book storage/retrieval.
"""

import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """Creates the books table if it doesn't exist."""
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS books (
                    title TEXT,
                    word TEXT,
                    frequency INTEGER,
                    PRIMARY KEY (title, word)
                )
            ''')

    def save_book(self, title, word_freqs):
        """Saves a book title and its word frequencies."""
        with self.conn:
            for word, freq in word_freqs.items():
                self.conn.execute(
                    "INSERT OR REPLACE INTO books (title, word, frequency) VALUES (?, ?, ?)",
                    (title, word, freq)
                )

    def get_book(self, title):
        """Fetches the top 10 most frequent words for a given title."""
        cursor = self.conn.execute(
            "SELECT word, frequency FROM books WHERE title = ? ORDER BY frequency DESC LIMIT 10",
            (title,)
        )
        return {row[0]: row[1] for row in cursor.fetchall()}
