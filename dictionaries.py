from collections import Counter 
def count_word_frequency(file_path):     
    with open(file_path, 'r') as file:         
        text = file.read().lower()        
        words = text.split()          
        word_count = Counter(words)       
    return word_count 

def print_most_common_words(word_count, n=5):     
    most_common = word_count.most_common(n)    
    for word, count in most_common:         
        print(f"{word}: {count}") 
    file_path = 'textfile.txt' 
    word_count = count_word_frequency(file_path) 
    print_most_common_words(word_count)

def read_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text


