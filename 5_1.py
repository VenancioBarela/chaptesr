# infile_name = "./infle.txt"
# infile = open(file_name, "r")
# names = [line.rstrip() for line in infile]


# infile.close()

# def main():
#     display_with_forlooop(file_name)
#     print()
#     display_with)

# def display_with_forlooop(file_name):
#     infile = open_file(file_name, "r")
#     for line in infile:
#         print(line, end ="")
#     infile.close()


# def display_with_list_comprehension(file_name):
#     infile = open_file(file_name, "r")
#     items = [line.rstrip() for line in infile]
#     print("items:", items)
#     infile.close

#     def open(file_name,mode): open
#         return open(file_name,mode)


# # main()


# create file object in write mode

def main(:)
    save_to_outfile("./outfile.txt")

def open_file(file_name,mode):
    return open(file_name, mode)

outfile = open_file("./outfile.txt", "w")


for name in names:
    if "Doe" not in name:
        print("Name to be persisted:", name)
        outfile.write(name)
        outfile.write(name + "\n")
        data.appen(name)
    else:
        print("Names to be excluded:", name)
outfile.close()
