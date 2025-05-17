"""
Book Search Tool
Author: Your Name
Date: YYYY-MM-DD

A tool to search Project Gutenberg for a book, count frequent words, and save data locally.
"""

import tkinter as tk
from tkinter import messagebox
from database import Database
from gutenberg import fetch_and_process_book
from utils import display_words

# Initialize DB
db = Database('books.db')

def search_local():
    title = title_entry.get().strip()
    if not title:
        messagebox.showwarning("Input Error", "Please enter a book title.")
        return

    result = db.get_book(title)
    if result:
        display_words(result, output_box)
    else:
        messagebox.showinfo("Not Found", "Book not found in local database.")

def fetch_from_gutenberg():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL.")
        return
    try:
        title, word_freqs = fetch_and_process_book(url)
        if word_freqs:
            db.save_book(title, word_freqs)
            display_words(word_freqs, output_box)
        else:
            messagebox.showinfo("No Data", "Book content could not be processed.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("Gutenberg Book Word Frequency")

tk.Label(root, text="Book Title:").pack()
title_entry = tk.Entry(root, width=50)
title_entry.pack()

tk.Button(root, text="Search Local", command=search_local).pack()

tk.Label(root, text="Gutenberg Book URL:").pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

tk.Button(root, text="Fetch & Save from Gutenberg", command=fetch_from_gutenberg).pack()

output_box = tk.Text(root, height=15, width=60)
output_box.pack()

root.mainloop()
