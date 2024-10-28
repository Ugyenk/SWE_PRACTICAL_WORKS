from collections import Counter

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return ""

# Existing functions
def count_lines(content):
    return len(content.split('\n'))

def count_words(content):
    return len(content.split())

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words) if words else 0

# New functions
def count_unique_words(content):
    words = set(content.lower().split())
    return len(words)

def find_longest_word(content):
    words = content.split()
    return max(words, key=len) if words else ""

def count_specific_word(content, word):
    words = content.lower().split()
    return words.count(word.lower())

def percentage_longer_than_avg(content):
    avg_length = average_word_length(content)
    words = content.split()
    longer_than_avg = [word for word in words if len(word) > avg_length]
    return (len(longer_than_avg) / len(words) * 100) if words else 0

# Analyze text function
def analyze_text(filename):
    content = read_file(filename)
    
    if not content:
        return  # Exit if the file was not read successfully

    num_lines = count_lines(content)
    num_words = count_words(content)
    unique_words = count_unique_words(content)
    common_word, common_count = most_common_word(content)
    avg_length = average_word_length(content)
    longest_word = find_longest_word(content)
    specific_word_count = count_specific_word(content, "example")  # Replace "example" with any target word
    percentage_longer = percentage_longer_than_avg(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Number of unique words: {unique_words}")
    print(f"Most common word: '{common_word}' (appears {common_count} times)")
    print(f"Average word length: {avg_length:.2f} characters")
    print(f"Longest word: '{longest_word}'")
    print(f"Occurrences of the specific word 'example': {specific_word_count}")
    print(f"Percentage of words longer than the average length: {percentage_longer:.2f}%")

# Run the analysis
analyze_text('C:\\Users\\User\\OneDrive\\Desktop\\SWE_Practical_Works\\Lab2\\Sample.text')
