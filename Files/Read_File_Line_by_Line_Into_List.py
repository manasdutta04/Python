with open("data_file.txt") as f:
    content_list = f.readlines()

# print the list
print(content_list)

# remove new line characters
content_list = [x.strip() for x in content_list]
print(content_list)



# create a txt File name "data_file.txt"

# data in the file:

#     honda 1948
#     mercedes 1926
#     ford 1903