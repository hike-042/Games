def process_text_file(file_name):
    with open(file_name, "r") as file:
        words = file.read().lower().split()

    unique_words = []
    seen_words = set()

    for word in words:
        if len(word) > 3 and word not in seen_words:
            unique_words.append(word)
            seen_words.add(word)

    sorted_words = sorted(unique_words)

    return sorted_words

file_name = "C:\\Users\\dhanu\\OneDrive\\Documents\\words.txt"  # Replace with the name of your input file
result = process_text_file(file_name)
for word in result:
    print(word)
