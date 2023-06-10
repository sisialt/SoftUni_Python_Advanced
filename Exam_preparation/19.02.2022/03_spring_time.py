def start_spring(**kwargs):
    result = []
    words = {}

    for kwarg in kwargs.items():
        if kwarg[1] not in words:
            words[kwarg[1]] = []
        words[kwarg[1]].append(kwarg[0])

    sorted_words = sorted(words.items(), key=lambda x: (-len(x[1]), x[0]))

    for word in sorted_words:
        result.append(f"{word[0]}:")  # there was space after :
        [result.append(f"-{s}") for s in sorted(word[1])]

    return '\n'.join(result)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
print()

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))
print()

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
