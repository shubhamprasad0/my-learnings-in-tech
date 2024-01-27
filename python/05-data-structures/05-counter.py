from collections import Counter

string = "hello world, my name is shubham and i am learning python data structures"
count_of_characters = Counter(string)
print(count_of_characters)
print(count_of_characters.most_common(5))

new_counter = Counter(['hello', "world", "hello", "world"])
print(new_counter)

