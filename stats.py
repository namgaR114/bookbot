def get_book_text(book):
        with open(book) as f:
            return f.read()
        
def sort_on(dict):
    return dict["num"]
