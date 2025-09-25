from stats import get_num_words, get_char_freq,sort_dict
import sys
def get_book_text(file_path):
    with open(file_path,"r",encoding="utf8") as f:
        data = f.read()
        return data

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    book = get_book_text(book_path)
    print(f"Analyzing book found at {book_path}...")
    num_words = get_num_words(book)
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    chars = sort_dict(book)
    print(f"--------- Character Count -------")
    for char in chars:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
            
    
main()