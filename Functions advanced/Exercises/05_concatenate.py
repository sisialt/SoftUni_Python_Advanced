def concatenate(*args, **kwargs):
    result = ""

    for arg in args:
        result += arg

    for key in kwargs:
        if key in result:
            result = result.replace(key, kwargs[key])  # forgot to assign the result

    return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))

print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))