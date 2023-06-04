import os

root_dir = os.path.dirname(os.path.abspath(__file__))

words_file_name = "words.txt"
words_file_path = os.path.join(root_dir, words_file_name)

text_file_name = "text5.txt"
text_file_path = os.path.join(root_dir, text_file_name)

results_file_name = "results_from_word_count.txt"
results_file_path = os.path.join(root_dir, results_file_name)

with open(words_file_path, "r") as words:
    words_as_list = words.read().lower().split()

with open(text_file_path) as text:
    text_as_list = text.read().lower().split()
    cleared_text_as_list = [el.strip("-.,?!") for el in text_as_list]

occurrences = {}

for word in words_as_list:

    for word_in_text in cleared_text_as_list:

        if word == word_in_text:
            if word not in occurrences:
                occurrences[word] = 0
            occurrences[word] += 1

result = ""

for key, value in sorted(occurrences.items(), key=lambda kvp: -kvp[1]):
    result += f"{key} - {value}\n"

with open(results_file_path, "a") as results:
    results.write(result)
