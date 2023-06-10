def words_sorting(*args):
    words = {}
    result = ""

    for arg in args:
        words[arg] = sum(ord(ch) for ch in arg)

    if sum(words.values()) % 2 != 0:
        sorted_words = dict(sorted(words.items(), key=lambda x: -x[1]))
    else:
        sorted_words = dict(sorted(words.items(), key=lambda x: x[0]))

    for key, value in sorted_words.items():
        result += f"{key} - {value}\n"

    return result

# def words_sorting(*words):
#     words_dict = {word: sum(map(ord, word)) for word in words}
#
#     if sum(words_dict.values()) % 2 == 0:
#         return "\n".join([f"{w} - {s}" for w, s in sorted(words_dict.items(), key=lambda x: x[0])])
#
#     return "\n".join([f"{w} - {s}" for w, s in sorted(words_dict.items(), key=lambda x: -x[1])])


print(words_sorting('escape', 'charm', 'mythology'))

print(words_sorting('escape', 'charm', 'eye'))

print(words_sorting('cacophony', 'accolade'))
