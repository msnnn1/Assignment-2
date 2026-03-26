def key_value(sentence):
    result = {}
    for char in sentence:
        if char != " ":
            if char in result:
                result[char] += 1
            else:
                result[char] = 1
    return result

sentence = input("Enter sentence: ")
print(key_value(sentence))