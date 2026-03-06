text = input("Введи текст: ")
words = text.split()

word_count = len(words)
char_count = len(text)

longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Слов:", word_count)
print("Символов:", char_count)
print("Самое длинное слово:", longest_word, f"({len(longest_word)} букв)")