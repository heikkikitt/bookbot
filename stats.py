def words(string):
    num_of_words = len(string.split())
    return num_of_words

def num_of_chars(string):
    num_of_chars = {}
    book = string.lower()
    for i in set(book):
        num_of_chars[i] = book.count(i)
    return num_of_chars

def sort_dict(character_counts):
    character_list = []
    for char, count in character_counts.items():
        character_list.append({"character": char, "count": count})
    
    character_list.sort(key=lambda x: x["count"], reverse=True)
    return character_list
