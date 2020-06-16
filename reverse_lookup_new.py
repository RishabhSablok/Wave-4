def dictionary_creation():
    number_of_elements = int(input("Input the number of dictionary elements: "))
    dictionary = {}
    for i in range(a):
        hh = ("Input the name of the "+ str(i+1) + " key: ")
        jj = ("Input the name of the " + str(i+1) + " value: ")
        key = input(hh)
        value = input(jj)
        try:
            key = float(key)
            value = float(value)
        except:
            pass
        dictionary.__setitem__(key, value)
    return dictionary

def lookup(dictionary, value):
    values = []
    keys = []
    for i in dictionary.keys():
        keys.append(i)
    for i in dictionary.values():
        values.append(i)
    for i in range(len(keys)):
        if values[i] == value:
            print(keys[i], end=" ")

print("Many answers: ", end="")
lookup({"a": 1, "b": 1, "c": 1, "d": 2, "e": 4}, 1)
print()
print("One answers: ", end="")
lookup({"a": 1, "b": "hi", "c": "wow"},"hi")
print()
print("No answers: ", end="")
lookup({"a": 1, "b": "hi", "c": "wow"},"oo")
