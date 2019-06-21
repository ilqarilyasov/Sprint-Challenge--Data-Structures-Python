import time

start_time = time.time()

# f = open('names_1.txt', 'r')
# names_1 = f.read().split("\n")  # List containing 10000 names
# f.close()
names_1 = ["a", "b", "c", "d"]

# f = open('names_2.txt', 'r')
# names_2 = f.read().split("\n")  # List containing 10000 names
# f.close()
names_2 = ["e", "f", "g", "h", "i", "j"]

duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# for i in range(0, len(names_1)):
#     j = 0
#     while j < (len(names_2) - 1):
#         if names_1[i] == names_2[j]:
#             duplicates.append(names_1[i])
#         elif names_1[i] == names_2[j+1]:
#             duplicates.append(names_1[i])
#         j += 2



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

