def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    
    
def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)

main()
