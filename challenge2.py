# Build a small Text Analyzer tool that:

# Reads a text file from resources/challenge1.txt (use a relative path).

# Counts word frequencies (case-insensitive, stripped punctuation).

# Prints:

# Total lines

# Total words

# Top 1 most frequent word and its count

# The longest word and its length

# Saves the frequency table to a CSV file resources/word_freq.csv.

import sys

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
                if not word:
                    continue
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1
                word_count += 1
        
    return line_count, word_count, word_freq



def find_statistics(word_freq):    
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

def save_word_freq(word_freq, output_path):
    with open(output_path, "w") as f:
        f.write("Word,Count\n")
        for word,count in word_freq.items():
            f.write(f'{word},{count}\n')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python challenge2.py <path-to-text-file>")
        print("Example: python challenge2.py Resources/challenge1.txt")
        sys.exit(1)
    
    input_file = sys.argv[1]
    line_count, word_count, word_freq = analyze_text(input_file)



    most_frequent_word, highest_count, longest_word = find_statistics(word_freq)
    save_word_freq(word_freq, "Resources/word_freq.csv")

    print(f'Total lines: {line_count}')
    print(f'Total words: {word_count}') 
    if most_frequent_word is not None:
        print(f'Most frequent word: {most_frequent_word} (Count: {highest_count})')
    else:
        print("Most frequent word: None (no words found)")

    if longest_word is not None:
        print(f'Longest word: {longest_word} (Length: {len(longest_word)})')
    else:
        print("Longest word: None (no words found)")

# default top value (print top 1 by default)
top_n = 1

if "--top" in sys.argv:
    idx = sys.argv.index("--top")

    if idx +1 < len(sys.argv):
        raw = sys.argv[idx + 1]
        try:
            val = int(raw)
            if val > 0:
                top_n = val
            else:
                print(f'Warning: --top must be a positive integer, got {raw}. Using default top={top_n}.')
        except ValueError:
            print(f"Warning: invalid number for --top: {raw}. Using default top={top_n}.")       
else:
    print("Warning: --top provided but no number given. Using default top=1.")

# compute and print top N words
top_list = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:top_n]
print(f"\nTop {top_n} words:")
for w, c in top_list:
    print(f"{w}: {c}")