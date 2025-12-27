def sort_on(items):
    return items["num"]

def count_words(fulltext):
    words = fulltext.split()
    return len(words)

def count_characters(fulltext):
    all_char = {}
    text = fulltext.lower()
    for ch in text:
        if ch in all_char:
            all_char[ch] += 1
        else:
            all_char[ch] = 1
    return all_char

def sorted_char_count(character_data):
    sortable_char_list = []
    for ch , count in character_data.items():
        dicts = {}
        dicts["char"] = ch
        dicts["num"] = count
        sortable_char_list.append(dicts)
    sortable_char_list.sort(reverse=True, key=sort_on)
    return sortable_char_list