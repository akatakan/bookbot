def get_num_words(book_content):
    return len(book_content.split())
        
        
def get_char_freq(book_content):
    content = book_content.lower()
    freq = {}
    for c in content:
        freq[c] = freq.get(c,0) + 1
    return freq

def sort_dict(book):
    freq = get_char_freq(book)
    chars = []
    for k,v in freq.items():
        chars.append({"char":k,"num":v})
    chars.sort(reverse=True,key=lambda items: items["num"])
    return chars