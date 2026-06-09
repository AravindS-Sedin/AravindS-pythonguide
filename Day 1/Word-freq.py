paragraph = input("Enter a paragraph: ")
paragraph = paragraph.lower()

for ch in ".,!?;:'\"()[]{}":
    paragraph = paragraph.replace(ch, "")

words = paragraph.split()
word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
print(sorted_words[:5])

