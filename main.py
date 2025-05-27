# Main
from stats import sort_alpha_chars
from stats import get_num_words
from stats import get_character_counts
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    book_path = sys.argv[1]
    print(f"Analyzing book found at {book_path}...")
    text = get_book_text(book_path)
    print("----------- Word Count -----------")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_char = get_character_counts(text)
    sort_alpha = sort_alpha_chars(num_char)
    for char_dict in sort_alpha:
        print(f"{char_dict['char']}: {char_dict['num']}")   
        
def get_book_text(path):
    with open(path) as f:
        return f.read()



main()
