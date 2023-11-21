# # declaring a tuple
# t1 = ("hello", 2, "hello")  # with parens
# t2 = True, 1  # without parens
# print(type(t1), type(t2))  # both are tuples
# t1[0] = 1  # will crash, tuples are immutable once declared


# # declaring a set
# s1 = set([1, 2, 3, 1])  # uses the set keyword and square brackets
# s2 = {4, 4, 5}  # uses curly brackets, like dictionary
# print(type(s1), type(s2))
# s1.add(5)  # using the add method to add new items to a set
# s1.remove(1)  # using the remove method to get rid of the value 1
# print(s1)  # notice when printed it removed the second "1" at the end


# declaring a frozenset
# fset = frozenset([1, 2, 3, 4])
# print(type(fset))

# # Working with Text Files
# # opening/creating and writing to a text file
# f = open("Information.txt", "a")  # open file in writing and reading mode
# f.write("Dr. Ali" + "\n" + "University of Tehran" + "\n")
# f.close()
# # # reading from a text file
# f = open("Information.txt", "r")
# data = f.read()
# f.close()
# print(data)


# # Writing to CSV Files
# # opening/creating and writing to a csv file
# import csv
# with open("Information.csv", mode="w", newline="") as f:
#     writer = csv.writer(f, delimiter=",")
#     writer.writerow(["Name", "City"])
#     writer.writerow(["Craig Lou", "Taiwan"])


# # reading from csv files
# import csv
# with open("Information.csv", mode="r") as f:
#     reader = csv.reader(f, delimiter=",")
#     for row in reader:
#         print(row)

