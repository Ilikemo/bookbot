def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)             # get the text from the book
    word_count = count_words(text)              # count the words in the text
    character_result = character_count(text)     # count the characters in the text
    cleaned_result = cleanup_count(character_result)  # clean up the character count

    print("--- Beginning the report ---")
    print(f"The book contains {word_count} words.")
    for char in cleaned_result:
        print(f"The '{char['char']}' character was found {char['num']} times.")
    print("--- End of report ---")

def get_book_text(book_path):    
    with open(book_path) as f:                  # open the file
        return(f.read())                        # return the file contents as a string
        
def count_words(text):    
    words = text.split()                        # split the file contents into words
    return (len(words))                         # returns the number of words in the file 

def character_count(text):
    characters = {}
    lowered_text = text.lower()                 # convert the text to lowercase
    for character in lowered_text:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters                           # returns a dictionary of characters and their counts

def cleanup_count(character_result):
    character_list = []
    for char, count in character_result.items():     # iterate through the dictionary
        if char.isalpha():
            character_list.append({"char": char, "num": count})   # append the character and count to a list
    character_list.sort(key=sort_on, reverse=True)
    return character_list

def sort_on(dict):
    return dict["num"]


main()