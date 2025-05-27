def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

def sort_alpha_chars(char_dict):
    alpha_list=[]
    for char in char_dict:
        if char.isalpha() is True:
            alpha_list.append({"char": char, "num": char_dict[char]})
    alpha_list.sort(reverse=True, key=sort_on)
    return alpha_list

def get_character_counts(text):
    char_counts = {}
    for c in text:
        lowered = c.lower()
        if lowered in char_counts:
            char_counts[lowered] += 1
        else:
            char_counts[lowered] = 1
    return char_counts
