"""
utils.py
Text cleaning, word frequency analysis, and UI helpers.
"""

import re
from collections import Counter

def clean_text(text):
    """
    Cleans text by removing punctuation, converting to lowercase,
    and filtering out short/common words if needed.
    """
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

def get_top_words(text, n=10):
    """
    Returns a dictionary of the n most common words.
    """
    words = text.split()
    filtered = [word for word in words if len(word) > 3]
    counter = Counter(filtered)
    return dict(counter.most_common(n))

def display_words(freq_dict, output_widget):
    """
    Clears and displays word frequencies in the Tkinter output box.
    """
    output_widget.delete('1.0', 'end')
    if not freq_dict:
        output_widget.insert('end', "No words to display.\n")
    else:
        for word, freq in freq_dict.items():
            output_widget.insert('end', f"{word}: {freq}\n")
