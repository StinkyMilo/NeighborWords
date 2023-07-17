keyboard = ["qwertyuiop","asdfghjkl","zxcvbnm"]
all_words = [i.lower() for i in open("dictionary.txt","r").read().split("\n")]
words_set = set(all_words)
def shift_word(word, count):
    output=""
    for letter in word:
        for row in keyboard:
            if letter not in row:
                continue
            index = row.index(letter)
            if index+count < 0 or index+count >= len(row):
                return None
            output+=row[index+count]
    return output

max_shift = min([len(i) for i in keyboard])
longest_words = ["" for _ in range(0,max_shift)]
longest_shifted_words = ["" for _ in range(0,max_shift)]
# Step one: See if we get a word by shifting another left
for i in range(1,max_shift):
    for word in all_words:
        shifted_word = shift_word(word,i)
        if shifted_word in words_set:
            print(word+" <--> "+shifted_word+" (" +str(i)+")")
            if len(word) > len(longest_words[i-1]):
                longest_words[i-1] = word
                longest_shifted_words[i-1] = shifted_word

print("\nLongest words of each type:")
for i in range(0, len(longest_words)):
    print(str(i+1) + ": " + longest_words[i] + " <--> " + longest_shifted_words[i])

            