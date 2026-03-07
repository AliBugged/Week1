import string

text = input("Enter a text: ")  
text = text.lower()

clean_chars = []
for ch in text:
    if ch not in string.punctuation:
        clean_chars.append(ch)

clean_text = "".join(clean_chars)
words = clean_text.split()

print(words)  
