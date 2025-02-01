def main():

    def get_book_text():
        with open("books/frankenstein.txt") as f:
            return f.read()
        
    def sort_on(dict):
        return dict["num"]

    book_text = get_book_text()
    
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
  
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(words, "words found in the document")
    print( )
            
    for char in char_list:
        if char["char"].isalpha():
            print(f"The '{char["char"]}' character was found '{char["num"]} times")

    print("--- End report ---")



main()


