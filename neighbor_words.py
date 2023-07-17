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

def shift_word_both_hands(word, count_left, count_right):
    output=""
    for letter in word:
        for row in keyboard:
            if letter not in row:
                continue
            index = row.index(letter)
            if index <= 4:
                count = count_left
            else:
                count = count_right
            if index+count < 0 or index+count >= len(row):
                return None
            output+=row[index+count]
    return output

# longest_words = ["" for _ in range(0,max_shift)]
# longest_shifted_words = ["" for _ in range(0,max_shift)]
# num_words = 0
# print("Both hands offset by x amount:")
# # Step one: See if we get a word by shifting another right with both hands equally
# for i in range(1,max_shift):
#     for word in all_words:
#         shifted_word = shift_word(word,i)
#         if shifted_word in words_set:
#             print(word+" <--> "+shifted_word+" (" +str(i)+")")
#             if len(word) > len(longest_words[i-1]):
#                 longest_words[i-1] = word
#                 longest_shifted_words[i-1] = shifted_word
#                 num_words+=1

# print("\nLongest words of each type:")
# for i in range(0, len(longest_words)):
#     if len(longest_words[i])==0:
#         print(str(i+1) +": None!")
#     else:
#         print(str(i+1) + ": " + longest_words[i] + " <--> " + longest_shifted_words[i] + " " + str(len(longest_words[i])))
# print("\nNumber of words:",num_words)

# 9 is the largest you can go and still have any writeable letters (tho the only letter you can write at that point is P)
max_shift = 10
longest_words={}
longest_shifted_words={}
number_of_words={}
num_total_words = 0
used_combos = set()
for i in range(-4, max_shift):
    # Right can't get any words past a shift of 4
    # Any more than i-2 and the hands will collide
    for x in range(i-2, 5):
        if i==0 and x==0:
            continue
        word_id = str(i)+","+str(x)
        longest_words[word_id]=""
        longest_shifted_words[word_id]=""
        number_of_words[word_id]=0
        for word in all_words:
            shifted_word = shift_word_both_hands(word,i,x)
            if word != shifted_word and shifted_word in words_set:
                print(word+" <--> " + shifted_word + " (" +word_id+ ")")
                if frozenset((word,shifted_word)) not in used_combos:
                    num_total_words+=1
                    used_combos.add(frozenset((word,shifted_word)))
                number_of_words[word_id]+=1
                if len(word) > len(longest_words[word_id]):
                    longest_words[word_id]=word
                    longest_shifted_words[word_id]=shifted_word

print("\nLongest words of each type:")
for i in longest_words:
    if len(longest_words[i])>0:
        print(i + ": " + longest_words[i] + " <--> " + longest_shifted_words[i] + " (" + str(len(longest_words[i])) + ")")
    else:
        print(i + ": None!")

print("\nTotal Number of Unique Word Combinations: " + str(num_total_words))
print("\nTotal Number of words for each potential finger shift:")
for i in number_of_words:
    print(i + ": " + str(number_of_words[i]))
print("(In case you're wondering why these numbers don't add to the total, it's because sometimes a combination is double counted. For example, shifting your right hand left by 1 and keeping your left hand where it is produces bitterweeds <--> butterweeds, but shifting your right hand right by one and keeping your left hand where it is produces butterweeds <--> bitterweeds. Both of these combinations are counted for the individual shifts, but they're only counted once for the overall total.)")