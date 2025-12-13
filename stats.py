import sys
def get_book_text():

    file_path = sys.argv[1]
    
    with open(file_path) as f:
        file_content = f.read()
        return file_content

    
def count_words():
    return len(get_book_text().split())


#was here sort by items
def sort_print():
    sorted_letter = count_letters()
    sorted_letter = sorted(sorted_letter.items(), key=lambda item: item[1], reverse=True)

    for i, j in sorted_letter:
        if i.isalpha():
            print(f"{i}: {j}")
    


def count_letters():
    words = get_book_text().lower()
    letter_dict = {}
    for l in words:
        letter_dict[l] = letter_dict.get(l, 0) + 1


    return letter_dict
        
