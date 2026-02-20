# Build a small Text Analyzer tool that:

# Reads a text file from resources/challenge1.txt (use a relative path).

# Counts word frequencies (case-insensitive, stripped punctuation).

# Prints:

# Total lines

# Total words

# Top 1 most frequent word and its count

# The longest word and its length

# Saves the frequency table to a CSV file resources/word_freq.csv.

def analyze_text(file_path):
    with open(file_path, "r") as f:
        line_count = 0
        word_count = 0
        word_freq = {}

        for line in f:
            line_count += 1
            line = line.lower()
            words = line.split()
            for word in words:
                word = word.strip('.,!?";()[]{}$') 
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1
            word_count += len(words)
        
    return line_count, word_count, word_freq



def find_statistics(a):    
    highest_count = 0
    most_frequent_word = None
    max_length = 0
    longest_word = None

    for word, count in word_freq.items():
        if count > highest_count:
            highest_count = count
            most_frequent_word = word
        if len(word) > max_length:
            max_length = len(word)
            longest_word = word
    
    return most_frequent_word, highest_count, longest_word

def save_word_freq(b, output_path):
    with open(output_path, "w") as f:
        for word,count in word_freq.items():
            f.write(f'{word},{count}\n')


line_count, word_count, word_freq = analyze_text("resources/challenge1.txt")
most_frequent_word, highest_count, longest_word = find_statistics(word_freq)
save_word_freq(word_freq, "resources/word_freq.csv")

print(f'Total lines: {line_count}')
print(f'Total words: {word_count}') 
print(f'Most frequent word: {most_frequent_word} (Count: {highest_count})')
print(f'Longest word: {longest_word} (Length: {len(longest_word)})')