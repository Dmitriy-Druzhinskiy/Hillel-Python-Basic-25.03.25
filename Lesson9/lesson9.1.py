def popular_words(text, words):
    text_words = text.lower().split()
    result = {word: text_words.count(word) for word in words}
    return result

text = '''When I was One I had just begun When I was Two I was nearly new'''
words = ['i', 'I', 'was', 'Was', 'WAS', 'WAs', 'WaS', 'three', 'Three', 'THree', 'THRee',
         'nearly', 'Nearly', 'NeArly','NearlY']

popularity = popular_words(text, words)

for word, count in popularity.items():
    print(f"'{word}': {count}")
