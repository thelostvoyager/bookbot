import sys
from stats import count_words , count_characters , sorted_char_count

def get_book_text(filepath):
    #print(filepath)
    with open(filepath) as f:
        file_contents=f.read()
        return file_contents

def main():
    input = len(sys.argv)
    if(input != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = count_words(text)
    character_count = count_characters(text)
    sorted_char_list = sorted_char_count(character_count)
    #print(sorted_char_list)
    #print(len(sorted_char_list))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in range (0,len(sorted_char_list)):
        if(sorted_char_list[i]['char'].isalpha()):
            print(f"{sorted_char_list[i]['char']}: {sorted_char_list[i]['num']}")
    print("============= END ===============")

main()