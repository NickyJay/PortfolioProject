# numbers_set = {1, 2, 3, 4, 4} #duplicate values removed
#numbers_set = {1, 2, 3, 4, [5, 6]} # cannot use mutable data types
# numbers_set = {1, 2, 3, 4, (5, 6)} #tuples are imutable, OK to use!
# print(numbers_set)

words_set = {"Alpha", "Bravo", "Charlie"}

# abcd = ""
# for word in words_set:
#     abcd += word
# print(abcd)

words_set.add("Delta")
print(words_set)
words_set.discard("Bravo")
print(words_set)

userprofile = {"suspect" : "bill"}
print(userprofile)
userprofile["username"]="jdoe"