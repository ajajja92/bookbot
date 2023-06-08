def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    d = count_letters(text)
    convert(book_path, d)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_book_words(text):
    words = text.split()
    return words

def count_letters(text):
    dictionary = {}
    for c in text:
        l = c.lower()
        if l in dictionary:
            dictionary[l] += 1
        else:
            dictionary[l] = 1
    return dictionary 

def convert(book, dictionary):
    print(f"--- Begin report of {book} ---")
    new_list = list(dictionary.items())
    new_list.sort()
    for i in new_list:
       if i[0].isalpha():
        print(f"The '{i[0]}' character was found '{i[1]}' times")
    print(f"--- End report ---")    

main()