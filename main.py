from stats import *
import sys


def main():

    if len(sys.argv) != 2:
        print("Usage: python main.py <filename>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    lowered_text = book_text.lower()
    book_words = book_text.split()
    words = 0 

    for word in book_words:
        words += 1

    char_counts = {}
    for char in lowered_text:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    char_list = []
    for char, count in char_counts.items():
        char_list.append({"char": char, "num": count})

    char_list.sort(reverse=True, key=sort_on)
  
    
    print(f"--- Begin report of {sys.argv[1]} ---")
    print(words, "words found in the document")
    print( )
            
    for char in char_list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")

    print("--- End report ---")

    
    
main()


