#Main
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
#    print(text)
    num_words = word_count(text)
    print(f"{num_words} words found in the document")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(book_text):
    words = book_text.split()
    return len(words)

main()
