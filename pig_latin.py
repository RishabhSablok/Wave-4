sentence = str(input("Input an all lowercase sentence: ")).split()
aeiou = ["a", "e", "i", "o", "u"]

for word in sentence:
    last_part = []
    word = list(word)
    if word[0] in aeiou:
        word.append("way")
        word = "".join(word)
    else:
        a = 0
        try:
            while word[a] not in aeiou:
                last_part.append(word.pop(a))
        except:
            pass
        word = "".join(word) + "".join(last_part) + "ay"
    print(word, end = " ")