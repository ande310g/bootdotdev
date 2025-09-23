import operator
def word_counter (content):
    content_splitted = content.split()
    number_of_words = len(content_splitted)
    return number_of_words
    
def get_book_text (path):
    with open(path) as f:
        file_content = f.read()
        return file_content
        
def amount_characters(content):
    content = content.lower()
    character_dict = {}
    for i in content:
        if character_dict.get(i) == None:
            character_dict[i] = 1
        else:
            value = character_dict[i] + 1 
            character_dict[i] = value
    return character_dict 
    
    
def dict_pretty_print(diction):
    return_str = ""
    diction = dict(sorted(diction.items(), key=operator.itemgetter(1), reverse=True))
    for key, value in diction.items():
        if key.isalpha():
            if len(return_str) == 0:
                return_str += f"{key}: {value}"
            else: 
                return_str += f"\n{key}: {value}"
    return return_str    
    
def pretty_print (path):
    content = get_book_text(path)
    character_dict = amount_characters(content)
    word_counter_var = word_counter(content)
    pretty_dict = dict_pretty_print(character_dict)
    print(f"""
============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {word_counter_var} total words
--------- Character Count -------
{pretty_dict}
============= END ===============
          """)
    