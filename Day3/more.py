def filtered_words(words):
    result = []
    for word in words :
        if len(word) > 4 :
            result.append(word)
    return result

words = ['apple', 'cat', 'banana', 'dog', 'elephant', 'fish', 'grape', 'hat', 'ice', 'jacket']
print(filtered_words(words))


words = ['apple', 'cat', 'banana', 'dog', 'elephant', 'fish', 'grape', 'hat', 'ice', 'jacket']
result = list(filter(lambda word: len(word) > 4, words))
print(result)