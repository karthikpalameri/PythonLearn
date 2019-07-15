"""
FIle I/O
w -> write only mode
r -> read only mode
r+ -> Read and write mode
a -> Append mode
"""

my_List = [1, 2, 3]

my_file_ref = open("firstFile.txt", "r+")

for item in my_List:
    my_file_ref.write(str(item) +"\n")

my_file_ref.close()
