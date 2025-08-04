def count_words(book_text):
    return len(book_text.split())

def count_characters(book_text):
    characters = {}
    text_to_count = book_text.lower()
    for c in text_to_count:
        if c not in characters:
            characters[c] = 1
        else:
            characters[c] +=1
    return characters

def sort_on(items):
    return items["num"]

def sort_characters(char_counted):
    character_list = []
    for item in char_counted:
        character_dict = {"char": item, "num": char_counted[item]}
        character_list.append(character_dict)
    character_list.sort(reverse=True, key=sort_on)
    return character_list