def reverseLookup(dictionary, value):
    a = []
    for i, j in dictionary.items():
        if j == value:
            a += i
    return a

dictionary_1 = ({"a": 1, "b": 1, "c": 2})
dictionary_2 = ({"a": 99, "b": 1, "c": 2})
dictionary_3 = ({"a": 1, "b": 1, "c": 2})

print("More than one answers: ", reverseLookup(dictionary_1, 1))
print("One answer: ", reverseLookup(dictionary_2, 1))
print("No answer: ", reverseLookup(dictionary_3, 4))