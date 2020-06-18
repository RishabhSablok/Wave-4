sentence = str(input("Input the sentence: "))
sentence = sentence.split()
new_word = ""
new_sentence = []
for word in sentence:
    new_word = ""
    counter = 0
    length = len(word)
    if ("a" in word) or ("e" in word) or ("i" in word) or ("o" in word) or ("u" in word):
        if word[0] =="a" or word[0] == "i" or word[0] == "o" or word[0] == "u" or word[0] == "e":
            new_word = str(word + "way")
            new_sentence.append(new_word)
        else:
            for i in (word):
                if i =="a" or i == "i" or i == "o" or i == "u" or i == "e":
                    new_word = str(word[counter: length] + word[0: counter] + "ay")
                    new_sentence.append(new_word)
                    break
                counter += 1
    else:
        new_word = str(word + "ay")
        new_sentence.append(new_word)

for a in (new_sentence):
    print(a, end = " ")