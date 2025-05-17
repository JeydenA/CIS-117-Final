"""
gutenberg.py
Downloads and processes books from Project Gutenberg.
"""

import requests
from utils import clean_text, get_top_words

def fetch_and_process_book(url):
    """
    Downloads a book and returns (title, top_word_frequencies)
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch the book. Check the URL.")

    text = response.text
    lines = text.splitlines()

    # Guess a title from the first non-empty line
    title = next((line.strip() for line in lines if line.strip()), "Unknown Title")

    # Strip headers/footers from Gutenberg
    start_idx, end_idx = 0, len(lines)
    for i, line in enumerate(lines):
        if "*** START OF" in line:
            start_idx = i + 1
        elif "*** END OF" in line:
            end_idx = i
            break
    content = "\n".join(lines[start_idx:end_idx])

    cleaned = clean_text(content)
    top_words = get_top_words(cleaned, 10)

    return title, top_words
